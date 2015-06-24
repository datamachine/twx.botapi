import os
from socket import socket
import struct
from binascii import crc32 as original_crc32
from time import time

from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes, bytes_to_long

from twx.mtproto import rpc
from twx.mtproto import crypt
from twx.mtproto import prime

from hexdump import hexdump


def crc32(data):
    return original_crc32(data) & 0xffffffff

class MTProto:
    def __init__(self, api_secret, api_id):
        self.api_secret = api_secret
        self.api_id = api_id
        self.dc = Datacenter(0, Datacenter.DCs_test[1], 443)

class Datacenter:
    DATA_VERSION = 4

    DCs = [
        "149.154.175.50",
        "149.154.167.51",
        "149.154.175.100",
        "149.154.167.91",
        "149.154.171.5",
    ]

    DCs_ipv6 = [
        "2001:b28:f23d:f001::a",
        "2001:67c:4e8:f002::a",
        "2001:b28:f23d:f003::a",
        "2001:67c:4e8:f004::a",
        "2001:b28:f23f:f005::a",
    ]

    DCs_test = [
        "149.154.175.10",
        "149.154.167.40",
        "149.154.175.117",
    ]

    DCs_test_ipv6 = [
        "2001:b28:f23d:f001::e",
        "2001:67c:4e8:f002::e",
        "2001:b28:f23d:f003::e",
    ]

    def __init__(self, dc_id, ipaddr, port):
        self.ipaddr = ipaddr
        self.port = port
        self.datacenter_id = dc_id
        self.auth_server_salt_set = []
        self.sock = socket()
        self.sock.connect((ipaddr, port))
        self.sock.settimeout(5.0)
        self.message_queue = []

        self.last_msg_id = 0
        self.timedelta = 0
        self.number = 0

        self.authorized = False
        self.auth_key = None
        self.auth_key_id = None
        self.server_salt = None
        self.server_time = None

        self.MAX_RETRY = 5
        self.AUTH_MAX_RETRY = 5

        # TODO: Pass this in
        self.rsa_key = """-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAwVACPi9w23mF3tBkdZz+zwrzKOaaQdr01vAbU4E1pvkfj4sqDsm6
lyDONS789sVoD/xCS9Y0hkkC3gtL1tSfTlgCMOOul9lcixlEKzwKENj1Yz/s7daS
an9tqw3bfUV/nqgbhGX81v/+7RFAEd+RwFnK7a+XYl9sluzHRyVVaTTveB2GazTw
Efzk2DWgkBluml8OREmvfraX3bkHZJTKX4EQSjBbbdJ2ZXIsRrYOXfaA+xayEGB+
8hdlLmAjbCVfaigxX0CDqWeR1yFL9kwd9P0NsZRPsmoqVwMbMu7mStFai6aIhc3n
Slv8kg9qv1m6XHVQY3PnEw+QQtqSIXklHwIDAQAB
-----END RSA PUBLIC KEY-----"""

        # Handshake
        self.create_auth_key()
        print(self.auth_key)

    def create_auth_key(self):
        rand_nonce = os.urandom(16)
        req_pq = rpc.req_pq(rand_nonce).get_bytes()
        self.send_message(req_pq)
        resPQ = rpc.resPQ(self.recv_message())
        assert rand_nonce == resPQ.nonce

        public_key_fingerprint = resPQ.server_public_key_fingerprints[0]
        pq = bytes_to_long(resPQ.pq)

        [p, q] = prime.primefactors(pq)
        (p, q) = (q, p) if p > q else (p, q)
        assert p*q == pq and p < q

        print("Factorization %d = %d * %d" % (pq, p, q))

        p_bytes = long_to_bytes(p)
        q_bytes = long_to_bytes(q)
        key = RSA.importKey(self.rsa_key)
        new_nonce = os.urandom(32)

        p_q_inner_data = rpc.p_q_inner_data(pq=resPQ.pq, p=p_bytes, q=q_bytes,
                                            server_nonce=resPQ.server_nonce,
                                            nonce=resPQ.nonce,
                                            new_nonce=new_nonce)

        data = p_q_inner_data.get_bytes()
        assert p_q_inner_data.nonce == resPQ.nonce

        sha_digest = SHA.new(data).digest()
        random_bytes = os.urandom(255-len(data)-len(sha_digest))
        to_encrypt = sha_digest + data + random_bytes
        encrypted_data = key.encrypt(to_encrypt, 0)[0]

        req_DH_params = rpc.req_DH_params(p=p_bytes, q=q_bytes,
                                          nonce=resPQ.nonce,
                                          server_nonce=resPQ.server_nonce,
                                          public_key_fingerprint=public_key_fingerprint,
                                          encrypted_data=encrypted_data)
        data = req_DH_params.get_bytes()

        self.send_message(data)
        data = self.recv_message(debug=False)

        server_DH_params = rpc.server_DH_params(data)
        assert resPQ.nonce == server_DH_params.nonce
        assert resPQ.server_nonce == server_DH_params.server_nonce

        encrypted_answer = server_DH_params.encrypted_answer

        tmp_aes_key = SHA.new(new_nonce + resPQ.server_nonce).digest() + SHA.new(resPQ.server_nonce + new_nonce).digest()[0:12]
        tmp_aes_iv = SHA.new(resPQ.server_nonce + new_nonce).digest()[12:20] + SHA.new(new_nonce + new_nonce).digest() + new_nonce[0:4]

        answer_with_hash = crypt.ige_decrypt(encrypted_answer, tmp_aes_key, tmp_aes_iv)

        answer_hash = answer_with_hash[:20]
        answer = answer_with_hash[20:]

        server_DH_inner_data = rpc.server_DH_inner_data(answer)
        assert resPQ.nonce == server_DH_inner_data.nonce
        assert resPQ.server_nonce == server_DH_inner_data.server_nonce

        dh_prime_str = server_DH_inner_data.dh_prime
        g = server_DH_inner_data.g
        g_a_str = server_DH_inner_data.g_a
        server_time = server_DH_inner_data.server_time
        self.timedelta = server_time - time()

        dh_prime = bytes_to_long(dh_prime_str)
        g_a = bytes_to_long(g_a_str)

        assert prime.isprime(dh_prime)
        retry_id = 0
        b_str = os.urandom(256)
        b = bytes_to_long(b_str)
        g_b = pow(g, b, dh_prime)

        g_b_str = long_to_bytes(g_b)

        client_DH_inner_data = rpc.client_DH_inner_data(nonce=resPQ.nonce,
                                        server_nonce=resPQ.server_nonce,
                                        retry_id=retry_id,
                                        g_b=g_b_str)

        data = client_DH_inner_data.get_bytes()

        data_with_sha = SHA.new(data).digest()+data
        data_with_sha_padded = data_with_sha + os.urandom(-len(data_with_sha) % 16)
        encrypted_data = crypt.ige_encrypt(data_with_sha_padded, tmp_aes_key, tmp_aes_iv)

        for i in range(1, self.AUTH_MAX_RETRY): # retry when dh_gen_retry or dh_gen_fail
            set_client_DH_params = rpc.set_client_DH_params(nonce=resPQ.nonce,
                                                            server_nonce=resPQ.server_nonce,
                                                            encrypted_data=encrypted_data)
            self.send_message(set_client_DH_params.get_bytes())
            Set_client_DH_params_answer = rpc.set_client_DH_params_answer(self.recv_message())

            # print Set_client_DH_params_answer
            auth_key = pow(g_a, b, dh_prime)
            auth_key_str = long_to_bytes(auth_key)
            auth_key_sha = SHA.new(auth_key_str).digest()
            auth_key_aux_hash = auth_key_sha[:8]

            new_nonce_hash1 = SHA.new(new_nonce+b'\x01'+auth_key_aux_hash).digest()[-16:]
            new_nonce_hash2 = SHA.new(new_nonce+b'\x02'+auth_key_aux_hash).digest()[-16:]
            new_nonce_hash3 = SHA.new(new_nonce+b'\x03'+auth_key_aux_hash).digest()[-16:]

            assert Set_client_DH_params_answer.nonce == resPQ.nonce
            assert Set_client_DH_params_answer.server_nonce == resPQ.server_nonce

            if Set_client_DH_params_answer.status == 'ok':
                assert Set_client_DH_params_answer.new_nonce_hash == new_nonce_hash1
                print("Diffie Hellman key exchange processed successfully")

                self.server_salt = strxor(new_nonce[0:8], resPQ.server_nonce[0:8])
                self.auth_key = auth_key_str
                self.auth_key_id = auth_key_sha[-8:]
                print("Auth key generated")
                return "Auth Ok"
            elif Set_client_DH_params_answer.status == 'retry':
                assert Set_client_DH_params_answer.new_nonce_hash == new_nonce_hash2
                print ("Retry Auth")
            elif Set_client_DH_params_answer.status == 'fail':
                assert Set_client_DH_params_answer.new_nonce_hash == new_nonce_hash3
                print("Auth Failed")
                raise Exception("Auth Failed")
            else:
                raise Exception("Response Error")

    def generate_message_id(self):
        msg_id = int(time() * 2**32)
        if self.last_msg_id > msg_id:
            msg_id = self.last_msg_id + 1
        while msg_id % 4 is not 0:
            msg_id += 1

        return msg_id

    def send_message(self, message_data):
        message_id = self.generate_message_id()
        message = (b'\x00\x00\x00\x00\x00\x00\x00\x00' +
                   struct.pack('<Q', message_id) +
                   struct.pack('<I', len(message_data)) +
                   message_data)

        message = struct.pack('<II', len(message)+12, self.number) + message
        msg_chksum = crc32(message)
        message += struct.pack('<I', msg_chksum)

        self.sock.send(message)
        self.number += 1

    def recv_message(self, debug=False):
        """
        Reading socket and receiving message from server. Check the CRC32.
        """
        if debug:
            packet = self.sock.recv(1024)  # reads how many bytes to read
            hexdump(packet)

        packet_length_data = self.sock.recv(4)  # reads how many bytes to read

        if len(packet_length_data) < 4:
            raise Exception("Nothing in the socket!")
        packet_length = struct.unpack("<I", packet_length_data)[0]
        packet = self.sock.recv(packet_length - 4)  # read the rest of bytes from socket

        # check the CRC32
        if not crc32(packet_length_data + packet[0:-4]) == struct.unpack('<I', packet[-4:])[0]:
            raise Exception("CRC32 was not correct!")
        x = struct.unpack("<I", packet[:4])
        auth_key_id = packet[4:12]
        if auth_key_id == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            # No encryption - Plain text
            (message_id, message_length) = struct.unpack("<QI", packet[12:24])
            data = packet[24:24+message_length]
        elif auth_key_id == self.auth_key_id:
            pass
            message_key = packet[12:28]
            encrypted_data = packet[28:-4]
            aes_key, aes_iv = self.aes_calculate(message_key, direction="from server")
            decrypted_data = crypt.ige_decrypt(encrypted_data, aes_key, aes_iv)
            assert decrypted_data[0:8] == self.server_salt
            assert decrypted_data[8:16] == self.session_id
            message_id = decrypted_data[16:24]
            seq_no = struct.unpack("<I", decrypted_data[24:28])[0]
            message_data_length = struct.unpack("<I", decrypted_data[28:32])[0]
            data = decrypted_data[32:32+message_data_length]
        else:
            raise Exception("Got unknown auth_key id")
        return data

    def __del__(self):
        # cleanup
        self.sock.close()



if __name__ == "__main__":
    mtp = MTProto("FFFFFFFFF", "EEEEEEEE")