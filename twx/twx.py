from .mtproto import mtproto
from .mtproto import rpc

from datetime import datetime
import random
import hashlib

class TWX:
    def __init__(self, api_key, app_id, rsa_cert):
        self._mtproto = mtproto.MTProto(api_key, app_id, rsa_cert)
        self._peer_cache = []
        self._contact_list = []
        self._dialog_list = []
        self.id = None

        # Callbacks
        self.on_binlog_replay_end = None
        self.on_get_difference_end = None
        self.on_msg_receive = None
        self.on_user_update = None
        self.on_chat_update = None
        self.on_secret_chat_update = None

    def send_message(self, peer, text, reply=None, link_preview=None, callback=None):
        """
        Send message to peer.
        :param peer: Peer to send message to.
        :param text: Text to send.
        :param reply: Message object or message_id to reply to.
        :param link_preview: Whether or not to show the link preview for this message
        :param callback: Callback to call when call is complete.
        """

        # messages.sendMessage#fc55e6b5 flags:# peer:InputPeer reply_to_msg_id:flags.0?int message:string random_id:long
        # reply_markup:flags.2?ReplyMarkup = messages.SentMessage;
        self._mtproto.rpc_call(rpc.messages.sendMessage(message=text, peer=peer,
                                                        reply_to_msg_id=reply, reply_markup=link_preview,
                                                        random_id=int(random.random())),
                               callback)

    def get_contact_list(self, callback=None):
        """
        Retrieve contact list.
        :param callback: Callback to call when server returns of contacts. If not specified, just load the local version
        """
        if callback is None:
            return self.contact_list
        else:
            self._mtproto.rpc_call(rpc.contacts.getContacts(hash=self._get_contact_list_hash()), callback=callback)

    def add_contact(self, phone, first_name, last_name=None, callback=None):
        """
        Add contact by phone number and name (last_name is optional).
        :param phone: Valid phone number for contact.
        :param first_name: First name to use.
        :param last_name: Last name to use. Optional.
        :param callback: Callback to call when adding, will contain success status and the current contact list.
        """
        self._mtproto.rpc_call(rpc.contacts.importContacts(contacts=[rpc.InputContact(client_id=self.id, phone=phone,
                                                                                      first_name=first_name,
                                                                                      last_name=last_name)]),
                               callback=callback)

    def del_contact(self, peer, callback=None):
        """
        Delete peer from contact list
        :param peer: Peer to delete
        :param callback: Callback to call when deleting, will contain success status and the current contact list.
        """
        self._mtproto.rpc_call(rpc.contacts.deleteContact(id=rpc.InputUser(user_id=peer.id)), callback)

    def message_search(self, text, callback, peer=None, min_date=None, max_date=None, max_id=None, offset=0, limit=255):
        """
        Search for messages.
        :param text: Text to search for in messages
        :param callback: Callback to call containing all the matching messages.
        :param peer: Peer to search, if None, search all dialogs.
        :param min_date: Start search from this datetime.
        :param max_date: Send search at this datetime.
        :param max_id: Don't return any messages after this Message or message_id.
        :param offset: Number of messages to skip.
        :param limit: How many messages to return.
        :return:
        """
        if max_date:
            max_date = int((max_date - datetime(1970, 1, 1)).total_seconds())

        if min_date:
            min_date = int((min_date - datetime(1970, 1, 1)).total_seconds())

        if peer:
            if peer.type == Group:
                peer = rpc.inputPeerChat(chat_id=peer.id)
            elif peer.type == User:
                peer = rpc.inputPeerContact(user_id=peer.id)
            else:
                raise TWXException("Searching a non-supported peer type")

        self._mtproto.rpc_call(rpc.messages.search(peer=peer or rpc.inputPeerEmpty,
                                                   q=text,
                                                   filter=rpc.inputMessagesFilterEmpty,
                                                   min_date=min_date or -1,
                                                   max_date=max_date or -1,
                                                   max_id=max_id or -1,
                                                   offset=offset,
                                                   limit=limit), callback)

    def set_profile_photo(self, file_path, callback=None):
        pass

    def create_secret_chat(self, user, callback=None):
        pass

    def create_group_chat(self, user_list, name, callback=None):
        pass

    def restore_msg(self, message, callback=None):
        pass

    def status_online(self):
        pass

    def status_offline(self):
        pass

    def _get_contact_list_hash(self):
        return hashlib.md5(','.join(sorted([contact.id for contact in self.contact_list]))).hexdigest()


class Peer:
    def __init__(self, twx, peer_type=None):
        """
        :param twx: twx.TWX instance associated with this peer.
        :param peer_type: Peer type as a class
        :return: New generic peer
        """
        self.twx = twx
        self._id = None
        self._type = peer_type or Peer
        self.name = None

    def send_message(self, text, reply=None, link_preview=None, callback=None):
        """
        Send message directly to peer. Async
        :param text: Unicode string to send to peer, required.
        :param reply: Message object or message_id to reply to.
        :param link_preview: Whether or not to show the link preview for this message
        :param callback: Callback to call when call is complete.
        """
        self.twx.send_message(self, text, reply, link_preview, callback)

    def message_search(self, text, callback, min_date=None, max_date=None, max_id=None, offset=0, limit=255):
        self.twx.message_search(text, callback, self, min_date=min_date, max_date=max_date,
                                max_id=max_id, offset=offset, limit=limit)

    def get_history(self, callback, offset=0, limit=255):
        pass

    def send_typing(self):
        pass

    def send_typing_abort(self):
        pass

    def fwd_msg(self, message_ids=None, callback=None):
        pass

    def send_photo(self, file, callback=None):
        pass

    def send_video(self, file, callback=None):
        pass

    def send_text(self, file, callback=None):
        pass

    def send_location(self, latitude, longitude, callback=None):
        pass

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type


class Group(Peer):
    def __init__(self, twx):
        super().__init__(twx, Group)
        self.user_list = []

    def rename_chat(self, name):
        pass

    def add_user(self, user, callback=None):
        pass

    def del_user(self, user, callback=None):
        pass

class User(Peer):
    def __init__(self, twx):
        super().__init__(twx, User)
        self.user_status = {'online': None, 'when': None}
        self.phone = None
        self.first_name = None
        self.last_name = None

class SecretChat(Peer):
    def __init__(self, twx):
        super().__init__(twx, SecretChat)
        self.user_id = None

class Message:
    def __init__(self):
        self.id = None
        self.flags = None
        self.mention = None
        self.out = None
        self.unread = None
        self.service = None
        self.src = None
        self.dest = None
        self.text = None
        self.media = {}
        self.date = None
        self.fwd_src = None
        self.fwd_date = None
        self.reply = None
        self.action = None

    def load_photo(self, callback):
        pass

    def load_video(self, callback):
        pass

    def load_video_thumb(self, callback):
        pass

    def load_audio(self, callback):
        pass

    def load_document(self, callback):
        pass

    def load_document_thumb(self, callback):
        pass

    def delete_msg(self):
        pass


class TWXException(Exception):
    pass