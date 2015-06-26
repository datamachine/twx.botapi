from abc import ABCMeta
import struct
from io import BytesIO
from hexdump import hexdump

def vis(bs):
    """
    Function to visualize byte streams. Split into bytes, print to console.
    :param bs: BYTE STRING
    """
    bs = bytearray(bs)
    symbols_in_one_line = 8
    n = len(bs) // symbols_in_one_line
    i = 0
    for i in range(n):
        print(str(i*symbols_in_one_line)+" | "+" ".join(["%02X" % b for b in bs[i*symbols_in_one_line:(i+1)*symbols_in_one_line]])) # for every 8 symbols line
    if not len(bs) % symbols_in_one_line == 0:
        print(str((i+1)*symbols_in_one_line)+" | "+" ".join(["%02X" % b for b in bs[(i+1)*symbols_in_one_line:]])+"\n") # for last line

class TLObject():
    @staticmethod
    def tl_bool(condition):
        if condition:
            return 0x997275b5
        else:
            return 0xbc799737

class initConnection(TLObject):
    constructor = 0x69796de9

    def __init__(self):
        self.api_id = None
        self.device_model = None
        self.system_version = None
        self.app_version = None
        self.lang_code = None
        self.query = None

    def get_bytes(self):
        return struct.pack(">iissss", initConnection.constructor, self.api_id,
                                      self.device_model, self.system_version,
                                      self.app_version, self.lang_code) + self.query.get_bytes()

    def set_params(self, data):
        (self.api_id, self.device_model,
         self.system_version, self.app_version,
         self.lang_code) = struct.unpack(">issss", data)

class invokeWithLayer(TLObject):
    constructor = 0xda9b0d0d

    def __init__(self):
        self.layer = 27
        self.query = None

    def get_bytes(self):
        return struct.pack(">ii", invokeWithLayer.constructor, self.layer) + self.query.get_bytes()

class checkPhone(TLObject):
    constructor = 0x6fe51dfb

    def __init__(self, phone_number=None):
        self.response_class = checkedPhone.__class__
        self.phone_number = phone_number

    def get_bytes(self):
        return struct.pack(">is", checkPhone.constructor, self.phone_number)

    def set_params(self, data):
        (self.phone_number) = struct.unpack(">s", data)

class checkedPhone(TLObject):
    constructor = 0x811ea28e

    def __init__(self):
        self.phone_registered = False
        self.phone_invited = False

    def get_bytes(self):
        return struct.pack(">i??", checkedPhone.constructor, self.phone_registered, self.phone_invited)

    def set_params(self, data):
        (self.phone_registered, self.phone_invited) = struct.unpack(">??", data)

class req_pq(TLObject):
    constructor = 0x60469778

    def __init__(self, nonce):
        self.nonce = nonce

    def get_bytes(self):
        return struct.pack("<I16s", req_pq.constructor, self.nonce)

class resPQ:
    constructor = 0x05162463

    def __init__(self, data=None):
        self.nonce = None
        self.server_nonce = None
        self.pq = None
        self.server_public_key_fingerprints = []
        if data:
            self.set_params(data)

    def set_params(self, data):
        """ resPQ#05162463 nonce:int128 server_nonce:int128 pq:string server_public_key_fingerprints:Vector long = ResPQ """
        bytes_io = BytesIO(data)

        assert struct.unpack('<I', bytes_io.read(4))[0] == resPQ.constructor

        self.nonce = bytes_io.read(16)
        self.server_nonce = bytes_io.read(16)

        self.pq = deserialize_string(bytes_io)

        assert struct.unpack('<I', bytes_io.read(4))[0] == 0x1cb5c415  # long vector
        count = struct.unpack('<l', bytes_io.read(4))[0]
        for _ in range(count):
            self.server_public_key_fingerprints.append(struct.unpack('<q', bytes_io.read(8))[0])


class p_q_inner_data:
    constructor = 0x83c95aec

    def __init__(self, nonce=None, server_nonce=None, new_nonce=None, pq=None, p=None, q=None):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce = new_nonce
        self.pq = pq
        self.p = p
        self.q = q

    def get_bytes(self):
        """ p_q_inner_data#83c95aec pq:bytes p:bytes q:bytes nonce:int128 server_nonce:int128 new_nonce:int256 = P_Q_inner_data """

        pq_io = BytesIO()
        serialize_string(pq_io, self.pq)
        serialize_string(pq_io, self.p)
        serialize_string(pq_io, self.q)

        print("\nPQ")
        hexdump(self.pq)

        print("\nP")
        hexdump(self.p)

        print("\nQ")
        hexdump(self.q)

        print("\nPQ_io")
        hexdump(pq_io.getvalue())

        print("\nnonce")
        hexdump(self.nonce)

        print("\nserver_nonce")
        hexdump(self.server_nonce)

        print("\nnew_nonce")
        hexdump(self.new_nonce)

        ret = struct.pack("<I28s16s16s32s", p_q_inner_data.constructor, pq_io.getvalue(),
                           self.nonce, self.server_nonce, self.new_nonce)

        print("\np_q_inner_data")
        hexdump(ret)

        return ret

class req_DH_params:
    constructor = 0xd712e4be

    def __init__(self, nonce=None, server_nonce=None, p=None, q=None,
                 public_key_fingerprint=None, encrypted_data=None):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.p = p
        self.q = q
        self.public_key_fingerprint = public_key_fingerprint
        self.encrypted_data = encrypted_data

    def get_bytes(self):
        """req_DH_params#d712e4be nonce:int128 server_nonce:int128 p:bytes q:bytes public_key_fingerprint:long encrypted_data:bytes = Server_DH_Params"""

        pq_io = BytesIO()
        serialize_string(pq_io, self.p)
        serialize_string(pq_io, self.q)

        ret = struct.pack("<I16s16s16sq", req_DH_params.constructor, self.nonce, self.server_nonce,
                          pq_io.getvalue(), self.public_key_fingerprint)

        bytes_io = BytesIO()
        bytes_io.write(ret)

        serialize_string(bytes_io, self.encrypted_data)

        return bytes_io.getvalue()

class server_DH_params:
    constructor_ok = 0xd0e8075c
    constructor_fail = 0x79cb045d

    def __init__(self, data):
        self.nonce = None
        self.server_nonce = None
        self.new_nonce_hash = None
        self.encrypted_answer = None
        self.ok = True

        self.set_params(data)

    def set_params(self, data):
        bytes_io = BytesIO(data)
        constructor = struct.unpack('<I', bytes_io.read(4))[0]

        self.nonce = bytes_io.read(16)
        self.server_nonce = bytes_io.read(16)

        if constructor == server_DH_params.constructor_ok:
            self.encrypted_answer = deserialize_string(bytes_io)
        elif constructor == server_DH_params.constructor_fail:
            self.new_nonce_hash = bytes_io.read(16)
            self.ok = False
        else:
            assert False

class server_DH_inner_data:
    constructor = 0xb5890dba

    def __init__(self, data):
        self.nonce = None
        self.server_nonce = None
        self.g = None
        self.dh_prime = None
        self.g_a = None
        self.server_time = None
        self.set_params(data)

    def set_params(self, data):
        """server_DH_inner_data#b5890dba nonce:int128 server_nonce:int128 g:int dh_prime:bytes g_a:bytes server_time:int = Server_DH_inner_data"""
        bytes_io = BytesIO(data)

        assert struct.unpack("<I", bytes_io.read(4))[0] == 0xb5890dba

        self.nonce = bytes_io.read(16)
        self.server_nonce = bytes_io.read(16)

        self.g = struct.unpack("<I", bytes_io.read(4))[0]

        self.dh_prime = deserialize_string(bytes_io)
        self.g_a = deserialize_string(bytes_io)

        self.server_time = struct.unpack("<I", bytes_io.read(4))[0]


class client_DH_inner_data:
    constructor = 0x6643b654

    def __init__(self, nonce=None, server_nonce=None, retry_id=None, g_b=None):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.retry_id = retry_id
        self.g_b = g_b

    def get_bytes(self):
        """client_DH_inner_data#6643b654 nonce:int128 server_nonce:int128 retry_id:long g_b:string = Client_DH_Inner_Data"""

        ret = struct.pack("<I16s16sQ", client_DH_inner_data.constructor, self.nonce, self.server_nonce,
                           self.retry_id)

        bytes_io = BytesIO()
        bytes_io.write(ret)
        serialize_string(bytes_io, self.g_b)

        return bytes_io.getvalue()

class set_client_DH_params:
    constructor = 0xf5045f1f

    def __init__(self, nonce=None, server_nonce=None, encrypted_data=None):
        self.nonce = nonce
        self.server_nonce = server_nonce
        self.encrypted_data = encrypted_data

    def get_bytes(self):
        """set_client_DH_params#f5045f1f nonce:int128 server_nonce:int128 encrypted_data:bytes = Set_client_DH_params_answer"""

        ret = struct.pack("<I16s16s", set_client_DH_params.constructor, self.nonce, self.server_nonce)

        bytes_io = BytesIO()
        bytes_io.write(ret)
        serialize_string(bytes_io, self.encrypted_data)

        return bytes_io.getvalue()

class set_client_DH_params_answer:
    constructor_ok = 0x3bcbf734
    constructor_retry = 0x46dc1fb9
    constructor_fail = 0xa69dae02

    def __init__(self, data):
        self.nonce = None
        self.server_nonce = None
        self.new_nonce_hash = None
        self.status = "ok"

        self.set_params(data)

    def set_params(self, data):
        bytes_io = BytesIO(data)

        constructor = struct.unpack("<I", bytes_io.read(4))[0]
        self.nonce = bytes_io.read(16)
        self.server_nonce = bytes_io.read(16)
        self.new_nonce_hash = bytes_io.read(16)

        if constructor == set_client_DH_params_answer.constructor_ok:
            self.status = "ok"
        elif constructor == set_client_DH_params_answer.constructor_retry:
            self.status = "retry"
        else:
            self.status = "fail"


def serialize_string(bytes_io, value):
    l = len(value)
    if l < 254: # short string format
        bytes_io.write(struct.pack('<b', l))  # 1 byte of string
        bytes_io.write(value)   # string
        bytes_io.write(b'\x00'*((-l-1) % 4))  # padding bytes
    else:
        bytes_io.write(b'\xfe')  # byte 254
        bytes_io.write(struct.pack('<i', l)[:3])  # 3 bytes of string
        bytes_io.write(value) # string
        bytes_io.write(b'\x00'*(-l % 4))  # padding bytes

def deserialize_string(bytes_io):
    l = struct.unpack('<B', bytes_io.read(1))[0]
    assert l <= 254  # In general, 0xFF byte is not allowed here
    if l == 254:
        # We have a long string
        long_len = struct.unpack('<I', bytes_io.read(3)+b'\x00')[0]
        string = bytes_io.read(long_len)
        bytes_io.read(-long_len % 4)  # skip padding bytes
    else:
        # We have a short string
        string = bytes_io.read(l)
        bytes_io.read(-(l+1) % 4)  # skip padding bytes
    assert isinstance(string, bytes)

    return string

def print_bytes(data):
    """
    Function to visualize byte streams. Split into bytes, print to console.
    :param bs: BYTE STRING
    """
    bs = bytearray(data)
    symbols_in_one_line = 8
    n = len(bs) // symbols_in_one_line
    i = 0
    for i in range(n):
        print(str(i*symbols_in_one_line)+" | "+" ".join(["%02X" % b for b in bs[i*symbols_in_one_line:(i+1)*symbols_in_one_line]])) # for every 8 symbols line
    if not len(bs) % symbols_in_one_line == 0:
        print(str((i+1)*symbols_in_one_line)+" | "+" ".join(["%02X" % b for b in bs[(i+1)*symbols_in_one_line:]])+"\n") # for last line


