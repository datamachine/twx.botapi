from enum import Enum
import botapi

import mimetypes
from datetime import datetime
from abc import ABCMeta, abstractmethod
import collections


class TWX(metaclass=ABCMeta):
    def __init__(self):
        self._on_msg_receive = None
        self._on_user_update = None
        self._on_chat_update = None
        self._on_secret_chat_update = None

    @property
    @abstractmethod
    def bot_id(self):
        """
        :returns: The telegram ID of the current bot.
        """
        pass

    @property
    def on_msg_receive(self):
        return self._on_msg_receive

    @on_msg_receive.setter
    def on_msg_receive(self, callback):
        self._on_msg_receive = callback

    @property
    def on_user_update(self):
        return self._on_user_update

    @on_user_update.setter
    def on_user_update(self, callback):
        self._on_user_update = callback

    @property
    def on_chat_update(self):
        return self._on_chat_update

    @on_chat_update.setter
    def on_chat_update(self, callback):
        self._on_chat_update = callback

    @property
    def on_secret_chat_update(self):
        return self._on_secret_chat_update

    @on_secret_chat_update.setter
    def on_secret_chat_update(self, callback):
        self._on_secret_chat_update = callback

    @abstractmethod
    def send_message(self, peer: Peer, text: str, reply: int=None, link_preview: bool=None, callback: callable=None):
        """
        Send message to peer.
        :param peer: Peer to send message to.
        :param text: Text to send.
        :param reply: Message object or message_id to reply to.
        :param link_preview: Whether or not to show the link preview for this message
        :param callback: Callback to call when call is complete.
        """
        pass

    @abstractmethod
    def forward_message(self, peer: Peer, message: Message):
        """
        Use this method to forward messages of any kind.

        :param peer: Peer to send forwarded message too.
        :param message: Message to be forwarded.

        :returns: On success, the sent Message is returned.
        """
        pass

    @abstractmethod
    def send_photo(self, peer: Peer, photo: str, caption: str=None, reply: int=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send photo to peer.
        :param peer: Peer to send message to.
        :param photo: File path to photo to send.
        :param caption: Caption for photo
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_audio(self, peer: Peer, audio: str, reply: int=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send audio clip to peer.
        :param peer: Peer to send message to.
        :param audio: File path to audio to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_document(self, peer: Peer, document: str, reply: int=None, callback: callable=None,
                      reply_markup: botapi.ReplyMarkup=None):
        """
        Send document to peer.
        :param peer: Peer to send message to.
        :param document: File path to document to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_sticker(self, peer: Peer, sticker: str, reply: int=None, callback: callable=None,
                     reply_markup: botapi.ReplyMarkup=None):
        """
        Send sticker to peer.
        :param peer: Peer to send message to.
        :param sticker: File path to sticker to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_video(self, peer: Peer, video: str, reply: int=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send video to peer.
        :param peer: Peer to send message to.
        :param video: File path to video to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_location(self, peer: Peer, latitude: float, longitude: float, reply: int=None, callback: callable=None,
                      reply_markup: botapi.ReplyMarkup=None):
        """
        Send location to peer.
        :param peer: Peer to send message to.
        :param latitude: Latitude of the location.
        :param longitude: Longitude of the location.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        pass

    @abstractmethod
    def send_chat_action(self, peer: Peer, action: botapi.ChatAction, callback: callable=None):
        """
        Send status to peer.
        :param peer: Peer to send status to.
        :param action: Type of action to send to peer.
        :param callback: Callback to call when call is complete.

        """
        pass

    @abstractmethod
    def get_user_profile_photos(self, peer: Peer, callback: callable, offset: int=None, limit: int=None):
        """

        :param peer:
        :param callback: Callback with the requested photos
        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned
        :param limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        """
        pass

    @abstractmethod
    def get_contact_list(self, callback: callable=None):
        """
        Retrieve contact list.
        :param callback: Callback to call when server returns of contacts. If not specified,
                         just load the local version
        """
        pass

    @abstractmethod
    def add_contact(self, phone_number: str, first_name: str, last_name: str=None, callback: callable=None):
        """
        Add contact by phone number and name (last_name is optional).
        :param phone: Valid phone number for contact.
        :param first_name: First name to use.
        :param last_name: Last name to use. Optional.
        :param callback: Callback to call when adding, will contain success status and the current contact list.
        """
        pass

    @abstractmethod
    def del_contact(self, peer: Peer, callback: callable=None):
        """
        Delete peer from contact list
        :param peer: Peer to delete
        :param callback: Callback to call when deleting, will contain success status and the current contact list.
        """
        pass

    @abstractmethod
    def message_search(self, text: str, callback: callable, peer: Peer=None,
                       min_date: datetime=None, max_date: datetime=None,
                       max_id: int=None, offset: int=0, limit: int=255):
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
        pass

    @abstractmethod
    def set_profile_photo(self, file_path: str, callback: callable=None):
        """
        Sets the profile photo for the bot.
        :param file_path: Path to image file
        :param callback: Callback to call with the status
        """
        pass

    @abstractmethod
    def create_secret_chat(self, user: User, callback: callable):
        """
        Create a secret chat with the user.
        :param user: User to start secret chat with.
        :param callback: Will return the chat and meta information.
        """
        pass

    @abstractmethod
    def create_group_chat(self, user_list: list, name: str, callback: callable=None):
        """
        Create a new group with the specified list of users, must be at least 2 users.
        :param user_list: List of Peers.
        :param name: Name of group.
        :param callback:
        """
        pass

    @abstractmethod
    def status_online(self):
        """
        Sets bot's status to online.
        """
        pass

    @abstractmethod
    def status_offline(self):
        """
        Sets bot's status to offline.
        """
        pass


def get_mimetype(file_path):
    return mimetypes.guess_type(file_path, strict=False)[0] or 'application/octet-stream'

class TWXBotApi(TWX):
    def __init__(self, token):
        super().__init__()
        
        self._bot_user = botapi.User(None, None, None, None)

        self.request_args = dict(
            token=token,
            request_method=botapi.RequestMethod.POST
        )

    @property
    def bot_id(self):
        return self._bot_user.id

    def update_bot_info(self):
        self._bot_user = botapi.get_me(request_args=self.request_args)

    def send_message(self, peer: Peer, text: str, reply: int=None, link_preview: bool=None,
                     callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send message to peer.
        :param peer: Peer to send message to.
        :param text: Text to send.
        :param reply: Message object or message_id to reply to.
        :param link_preview: Whether or not to show the link preview for this message
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        botapi.send_message(chat_id=peer.id, text=text, disable_web_page_preview=not link_preview,
                            reply_to_message_id=reply, callback=callback, reply_markup=reply_markup,
                            request_args=self.request_args)

    def forward_message(self, peer: Peer, message: Message, callback: callable=None):
        """
        Use this method to forward messages of any kind.

        :param peer: Peer to send forwarded message too.
        :param message: Message to be forwarded.
        :param callback: Callback to call when call is complete.

        :returns: On success, the sent Message is returned.
        """
        botapi.forward_message(peer.id, message.sender.id, message.id, request_args=self.request_args)

    def send_photo(self, peer: Peer, photo: str, caption: str=None, reply: int=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send photo to peer.
        :param peer: Peer to send message to.
        :param photo: File path to photo to send.
        :param caption: Caption for photo
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        photo = botapi.InputFile('photo', botapi.InputFileInfo(photo, open(photo, 'rb'), get_mimetype(photo)))

        botapi.send_photo(chat_id=peer.id, photo=photo, caption=caption, reply_to_message_id=reply, callback=callback,
                          reply_markup=reply_markup, request_args=self.request_args)

    def send_audio(self, peer: Peer, audio: str, reply: int=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send audio clip to peer.
        :param peer: Peer to send message to.
        :param audio: File path to audio to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        audio = botapi.InputFile('audio', botapi.InputFileInfo(audio, open(audio, 'rb'), get_mimetype(audio)))

        botapi.send_audio(chat_id=peer.id, audio=audio, reply_to_message_id=reply, callback=callback,
                          reply_markup=reply_markup, request_args=self.request_args)

    def send_document(self, peer: Peer, document: str, reply: int=None, callback: callable=None,
                      reply_markup: botapi.ReplyMarkup=None):
        """
        Send document to peer.
        :param peer: Peer to send message to.
        :param document: File path to document to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        document = botapi.InputFile('document', botapi.InputFileInfo(document, open(document, 'rb'),
                                                                     get_mimetype(document)))

        botapi.send_document(chat_id=peer.id, document=document, reply_to_message_id=reply, callback=callback,
                             reply_markup=reply_markup, request_args=self.request_args)

    def send_sticker(self, peer: Peer, sticker: str, reply: int=None, callback: callable=None,
                     reply_markup: botapi.ReplyMarkup=None):
        """
        Send sticker to peer.
        :param peer: Peer to send message to.
        :param sticker: File path to sticker to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        sticker = botapi.InputFile('sticker', botapi.InputFileInfo(sticker, open(sticker, 'rb'),
                                                                   get_mimetype(sticker)))

        botapi.send_sticker(chat_id=peer.id, sticker=sticker, reply_to_message_id=reply, callback=callback,
                            reply_markup=reply_markup, request_args=self.request_args)
        
    def send_video(self, peer: Peer, video: str, reply: int=None,
                   callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send video to peer.
        :param peer: Peer to send message to.
        :param video: File path to video to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        video = botapi.InputFile('video', botapi.InputFileInfo(video, open(video, 'rb'),
                                                               get_mimetype(video)))

        botapi.send_video(chat_id=peer.id, video=video, reply_to_message_id=reply, callback=callback,
                          reply_markup=reply_markup, request_args=self.request_args)

    def send_location(self, peer: Peer, latitude: float, longitude: float, reply: int=None,
                      callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send location to peer.
        :param peer: Peer to send message to.
        :param latitude: Latitude of the location.
        :param longitude: Longitude of the location.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        if isinstance(reply, Message):
            reply = reply.id

        botapi.send_location(chat_id=peer.id, latitude=latitude, longitude=longitude,
                             reply_to_message_id=reply, callback=callback, reply_markup=reply_markup,
                             request_args=self.request_args)

    def send_chat_action(self, peer: Peer, action: botapi.ChatAction, callback: callable=None):
        """
        Send status to peer.
        :param peer: Peer to send status to.
        :param action: Type of action to send to peer.
        :param callback: Callback to call when call is complete.

        """
        botapi.send_chat_action(chat_id=peer.id, action=action, callback=callback, request_args=self.request_args)

    def get_user_profile_photos(self, peer: Peer, callback: callable, offset: int=None, limit: int=None):
        """
        :param peer:
        :param callback: Callback with the requested photos
        :param offset: Sequential number of the first photo to be returned. By default, all photos are returned
        :param limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
        """
        botapi.get_user_profile_photos(chat_id=peer.id, callback=callback, offset=offset, limit=limit,
                                       request_args=self.request_args)

    # region Unsupported in botapi
    def get_contact_list(self, callback=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def add_contact(self, phone, first_name, last_name=None, callback=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def del_contact(self, peer, callback=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def message_search(self, text, callback, peer=None, min_date=None, max_date=None, max_id=None, offset=0, limit=255):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def set_profile_photo(self, file_path: str, callback: callable=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def create_secret_chat(self, user, callback=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def create_group_chat(self, user_list, name, callback=None):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def status_online(self):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()

    def status_offline(self):
        """
        Unsupported in the Bot API
        """
        raise TWXUnsupportedMethod()
    # endregion


class PeerType(str, Enum):
    GROUP = 'group'
    USER = 'user'
    SECRET_CHAT = 'secret_chat'

class Peer:
    def __init__(self, twx: TWX, peer_id: int, peer_type: PeerType):
        """
        :param twx: twx.TWX instance associated with this peer.
        :param peer_type: Peer type as a class
        :return: New generic peer
        """
        self.twx = twx
        self._id = peer_id
        self._type = peer_type
        self.name = None

    def send_message(self, text: str, reply: int=None, link_preview: bool=None,
                     callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send message to this peer.
        :param text: Text to send.
        :param reply: Message object or message_id to reply to.
        :param link_preview: Whether or not to show the link preview for this message
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        self.twx.send_message(self, text=text, reply=reply, link_preview=link_preview, callback=callback,
                              reply_markup=reply_markup)

    def message_search(self, text: str, callback: callable, min_date: datetime=None, max_date: datetime=None,
                       max_id: int=None, offset: int=0, limit: int=255):
        self.twx.message_search(text, callback, self, min_date=min_date, max_date=max_date,
                                max_id=max_id, offset=offset, limit=limit)

    def get_history(self, callback, offset=0, limit=255):
        raise NotImplemented()

    def send_typing(self):
        self.twx.send_chat_action(self, botapi.ChatAction.TEXT)

    def send_typing_abort(self):
        pass

    def forward_message(self, message: Message=None, callback: callable=None):
        """
        Forward message to this peer.
        :param message: Message to forward to peer.
        :param callback: Callback to call when call is complete.
        :return:
        """
        self.twx.forward_message(self, message, callback=callback)

    def send_photo(self, photo: str, caption: str=None, reply: Message=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send photo to this peer.
        :param photo: File path to photo to send.
        :param caption: Caption for photo
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """
        self.twx.send_photo(peer=self, photo=photo, caption=caption, reply=reply, reply_markup=reply_markup,
                            callback=callback)

    def send_audio(self, audio: str, reply: Message=None, callback: callable=None,
                   reply_markup: botapi.ReplyMarkup=None):
        """
        Send audio clip to this peer.
        :param audio: File path to audio to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """

        self.twx.send_audio(peer=self, audio=audio, reply_to_message_id=reply, callback=callback,
                            reply_markup=reply_markup)

    def send_document(self, document: str, reply: Message=None, callback: callable=None,
                      reply_markup: botapi.ReplyMarkup=None):
        """
        Send document to this peer.
        :param document: File path to document to send.
        :param reply: Message object or message_id to reply to.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """

        self.twx.send_document(peer=self, document=document, reply_to_message_id=reply, callback=callback,
                               reply_markup=reply_markup)

    def send_sticker(self, sticker: str, reply: Message=None, callback: callable=None,
                     reply_markup: botapi.ReplyMarkup=None):
        """
        Send sticker to this peer.
        :param sticker: File path to sticker to send.
        :param reply: Message object.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """

        self.twx.send_sticker(peer=self, sticker=sticker, reply_to_message_id=reply, callback=callback,
                              reply_markup=reply_markup)

    def send_video(self, video: str, reply: Message=None,
                   callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send video to this peer.
        :param video: File path to video to send.
        :param reply: Message object.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """

        self.twx.send_video(peer=self, video=video, reply_to_message_id=reply, callback=callback,
                            reply_markup=reply_markup)

    def send_location(self, latitude: float, longitude: float, reply: Message=None,
                      callback: callable=None, reply_markup: botapi.ReplyMarkup=None):
        """
        Send location to this peer.
        :param latitude: Latitude of the location.
        :param longitude: Longitude of the location.
        :param reply: Message object.
        :param callback: Callback to call when call is complete.

        :type reply: int or Message
        """

        self.twx.send_location(peer=self, latitude=latitude, longitude=longitude,
                               reply_to_message_id=reply, callback=callback, reply_markup=reply_markup)

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type


class Group(Peer):
    def __init__(self, twx: TWX, peer_id: int):
        super().__init__(twx, peer_id, PeerType.GROUP)
        self.user_list = []

    def rename_chat(self, name):
        raise NotImplementedError()

    def add_user(self, user, callback=None):
        raise NotImplementedError()

    def remove_user(self, user, callback=None):
        raise NotImplementedError()


class User(Peer):
    def __init__(self, twx: TWX, peer_id: int):
        super().__init__(twx, peer_id, PeerType.USER)
        self.user_status = {'online': None, 'when': None}
        self.phone = None
        self.first_name = None
        self.last_name = None

class SecretChat(Peer):
    def __init__(self, twx: TWX, peer_id: int):
        super().__init__(twx, peer_id, PeerType.SECRET_CHAT)
        self.user_id = None

class Message:
    def __init__(self):
        self.id = None
        self.flags = None
        self.mention = None
        self.out = None
        self.unread = None
        self.service = None
        self.sender = None
        self.receiver = None
        self.text = None
        self.media = {}
        self.date = None
        self.fwd_src = None
        self.fwd_date = None
        self.reply = None
        self.action = None

    def load_photo(self, callback):
        raise NotImplementedError()

    def load_video(self, callback):
        raise NotImplementedError()

    def load_video_thumb(self, callback):
        raise NotImplementedError()

    def load_audio(self, callback):
        raise NotImplementedError()

    def load_document(self, callback):
        raise NotImplementedError()

    def load_document_thumb(self, callback):
        raise NotImplementedError()

    def delete_msg(self):
        raise NotImplementedError()

class TWXUnsupportedMethod(Exception):
    pass

class TWXException(Exception):
    pass
