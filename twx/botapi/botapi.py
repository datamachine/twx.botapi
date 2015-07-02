# -*- coding: utf-8 -*-
"""Unofficial Telegram Bot API

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

from requests import Request, Session
from collections import namedtuple
from abc import ABCMeta, abstractmethod
from threading import Thread
from enum import Enum

import json

"""
Telegram Bot API Types as defined at https://core.telegram.org/bots/api#available-types
"""
_UserBase = namedtuple('User', ['id', 'first_name', 'last_name', 'username'])


class User(_UserBase):

    """This object represents a Telegram user or bot.

    Attributes:
        id (int): Unique identifier for this user or bot
        first_name (str): User‘s or bot’s first name
        last_name (Optional[str]): User‘s or bot’s last name
        username (Optional[str]): User‘s or bot’s username

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return User(
            id=result.get('id'),
            first_name=result.get('first_name'),
            last_name=result.get('last_name'),
            username=result.get('username')
            )


_GroupChatBase = namedtuple('GroupChat', ['id', 'title'])


class GroupChat(_GroupChatBase):

    """This object represents a group chat.

    Attributes:
        id    (int): Unique identifier for this group chat
        title (str): Group name

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return GroupChat(
            id=result.get('id'),
            title=result.get('title')
            )


_MessageBase = namedtuple('Message', [
    'message_id', 'sender', 'date', 'chat', 'forward_from', 'forward_date',
    'reply_to_message', 'text', 'audio', 'document', 'photo', 'sticker',
    'video', 'contact', 'location', 'new_chat_participant',
    'left_chat_participant', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
    'group_chat_created'])


class Message(_MessageBase):

    """This object represents a message.

    Attributes:
        message_id            (int)                 :Unique message identifier
        from                  (User)                :Sender
        date                  (int)                 :Date the message was sent in Unix time
        chat                  (User or GroupChat)   :Conversation the message belongs to — user in case of a private
                                                     message, GroupChat in case of a group
        forward_from          (User)                :*Optional.* For forwarded messages, sender of the original message
        forward_date          (int)                 :*Optional.* For forwarded messages, date the original message was
                                                                 sent in Unix time
        reply_to_message      (Message)             :*Optional.* For replies, the original message. Note that the
                                                                 Message object in this field will not contain further
                                                                 reply_to_message fields even if it itself is a reply.
        text                  (str)                 :*Optional.* For text messages, the actual UTF-8 text of the message
        audio                 (Audio)               :*Optional.* Message is an audio file, information about the file
        document              (Document)            :*Optional.* Message is a general file, information about the file
        photo                 (Sequence[PhotoSize]) :*Optional.* Message is a photo, available sizes of the photo
        sticker               (Sticker)             :*Optional.* Message is a sticker, information about the sticker
        video                 (Video)               :*Optional.* Message is a video, information about the video
        contact               (Contact)             :*Optional.* Message is a shared contact, information about
                                                                 the contact
        location              (Location)            :*Optional.* Message is a shared location, information about the
                                                                 location
        new_chat_participant  (User)                :*Optional.* A new member was added to the group, information about
                                                                 them (this member may be bot itself)
        left_chat_participant (User)                :*Optional.* A member was removed from the group, information about
                                                                 them (this member may be bot itself)
        new_chat_title        (str)                 :*Optional.* A group title was changed to this value
        new_chat_photo        (Sequence[PhotoSize]) :*Optional.* A group photo was change to this value
        delete_chat_photo     (``True``)            :*Optional.* Informs that the group photo was deleted
        group_chat_created    (``True``)            :*Optional.* Informs that the group has been created
    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        # Determine whether chat is GroupChat or User type
        chat = result.get('chat')
        if 'id' in chat and 'title' in chat:
            chat = GroupChat.from_result(chat)
        else:
            chat = User.from_result(chat)

        # photo is a list of PhotoSize
        photo = result.get('photo')
        if photo is not None:
            photo = [PhotoSize.from_result(photo_size) for photo_size in photo]

        return Message(
            message_id=result.get('message_id'),
            sender=User.from_result(result.get('from')),
            date=result.get('date'),
            chat=chat,
            forward_from=User.from_result(result.get('forward_from')),
            forward_date=result.get('forward_date'),
            reply_to_message=Message.from_result(result.get('reply_to_message')),
            text=result.get('text'),
            audio=Audio.from_result(result.get('audio')),
            document=Document.from_result(result.get('document')),
            photo=photo,
            sticker=Sticker.from_result(result.get('sticker')),
            video=Video.from_result(result.get('video')),
            contact=Contact.from_result(result.get('contact')),
            location=Location.from_result(result.get('location')),
            new_chat_participant=User.from_result(result.get('new_chat_participant')),
            left_chat_participant=User.from_result(result.get('left_chat_participant')),
            new_chat_title=result.get('new_chat_title'),
            new_chat_photo=result.get('new_chat_photo'),
            delete_chat_photo=result.get('delete_chat_photo'),
            group_chat_created=result.get('group_chat_created')
            )


_PhotoSizeBase = namedtuple('PhotoSize', ['file_id', 'width', 'height', 'file_size'])


class PhotoSize(_PhotoSizeBase):

    """This object represents one size of a photo or a file / sticker thumbnail.

    Attributes:
        file_id    (str)  :Unique identifier for this file
        width      (int)  :Photo width
        height     (int)  :Photo height
        file_size  (int)  :*Optional.* File size
    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return PhotoSize(
            file_id=result.get('file_id'),
            width=result.get('width'),
            height=result.get('height'),
            file_size=result.get('file_size')
            )


_AudioBase = namedtuple('Audio', ['file_id', 'duration', 'mime_type', 'file_size'])


class Audio(_AudioBase):

    """This object represents an audio file (voice note).

    Attributes:
        file_id    (str)  :Unique identifier for this file
        duration   (int)  :Duration of the audio in seconds as defined by sender
        mime_type  (str)  :*Optional.* MIME type of the file as defined by sender
        file_size  (int)  :*Optional.* File size

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Audio(
            file_id=result.get('file_id'),
            duration=result.get('duration'),
            mime_type=result.get('mime_type'),
            file_size=result.get('file_size')
            )


_DocumentBase = namedtuple('Document', ['file_id', 'thumb', 'file_name', 'mime_type', 'file_size'])


class Document(_DocumentBase):

    """This object represents a general file (as opposed to photos and audio files).

    Attributes:
        file_id    (str)        :Unique file identifier
        thumb      (PhotoSize)  :Document thumbnail as defined by sender
        file_name  (str)        :*Optional.* Original filename as defined by sender
        mime_type  (str)        :*Optional.* MIME type of the file as defined by sender
        file_size  (int)        :*Optional.* File size

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Document(
            file_id=result.get('file_id'),
            thumb=PhotoSize.from_result(result.get('thumb')),
            file_name=result.get('file_name'),
            mime_type=result.get('mime_type'),
            file_size=result.get('file_size')
            )


_StickerBase = namedtuple('Sticker', ['file_id', 'width', 'height', 'thumb', 'file_size'])


class Sticker(_StickerBase):

    """This object represents a sticker.

    Attributes:
        file_id    (str)        :Unique identifier for this file
        width      (int)        :Sticker width
        height     (int)        :Sticker height
        thumb      (PhotoSize)  :Sticker thumbnail in .webp or .jpg format
        file_size  (int)        :*Optional.* File size

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Sticker(
            file_id=result.get('file_id'),
            width=result.get('width'),
            height=result.get('height'),
            thumb=PhotoSize.from_result(result.get('thumb')),
            file_size=result.get('file_size')
            )


_VideoBase = namedtuple('Video', [
    'file_id', 'width', 'height', 'duration', 'thumb', 'mime_type', 'file_size', 'caption'])


class Video(_VideoBase):

    """This object represents a video file.

    Attributes:
        file_id     (str)       :Unique identifier for this file
        width       (int)       :Video width as defined by sender
        height      (int)       :Video height as defined by sender
        duration    (int)       :Duration of the video in seconds as defined by sender
        thumb       (PhotoSize) :Video thumbnail
        mime_type   (str)       :*Optional.* Mime type of a file as defined by sender
        file_size   (int)       :*Optional.* File size
        caption     (str)       :*Optional.* Text description of the video (usually empty)

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Video(
            file_id=result.get('file_id'),
            width=result.get('width'),
            height=result.get('height'),
            duration=result.get('duration'),
            thumb=PhotoSize.from_result(result.get('thumb')),
            mime_type=result.get('mime_type'),
            file_size=result.get('file_size'),
            caption=result.get('caption')
            )


_ContactBase = namedtuple('Contact', ['phone_number', 'first_name', 'last_name', 'user_id'])


class Contact(_ContactBase):

    """This object represents a phone contact.

    Attributes:
        phone_number    (str)  :Contact's phone number
        first_name      (str)  :Contact's first name
        last_name       (str)  :*Optional.* Contact's last name
        user_id         (str)  :*Optional.* Contact's user identifier in Telegram

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Contact(
            phone_number=result.get('phone_number'),
            first_name=result.get('first_name'),
            last_name=result.get('last_name'),
            user_id=result.get('user_id')
            )


_LocationBase = namedtuple('Location', ['longitude', 'latitude'])


class Location(_LocationBase):

    """This object represents a point on the map.

    Attributes:
        longitude   (float)   :Longitude as defined by sender
        latitude    (float)   :Latitude as defined by sender

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Location(
            longitude=result.get('longitude'),
            latitude=result.get('latitude')
            )


_UpdateBase = namedtuple('Update', ['update_id', 'message'])


class Update(_UpdateBase):

    """This object represents an incoming update.

    Attributes:
        update_id   (int)     :The update‘s unique identifier. Update identifiers start from a certain
                               positive number and increase sequentially. This ID becomes especially handy
                               if you’re using Webhooks, since it allows you to ignore repeated updates or to
                               restore the correct update sequence, should they get out of order.
        message     (Message) :*Optional.* New incoming message of any kind — text, photo, sticker, etc.

    """
    __slots__ = ()

    @staticmethod
    def from_dict(message_update):
        if message_update is None:
            return None

        return Update(message_update.get('update_id'), Message.from_result(message_update.get('message')))

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return [Update.from_dict(message_update) for message_update in result]


_InputFileInfoBase = namedtuple('InputFileInfo', ['file_name', 'fp', 'mime_type'])


class InputFileInfo(_InputFileInfoBase):
    __slots__ = ()


_InputFileBase = namedtuple('InputFile', ['form', 'file_info'])


class InputFile(_InputFileBase):

    """This object represents the contents of a file to be uploaded. Must be posted using multipart/form-data
        in the usual way that files are uploaded via the browser.

        Attributes:
            form        (str)           :the form used to submit (e.g. 'photo')
            file_info   (InputFileInfo) :The file metadata required

        :Example:

            ::

                fp = open('foo.png', 'rb')
                file_info = InputFileInfo('foo.png', fp, 'image/png')

                InputFile('photo', file_info)

                bot.send_photo(chat_id=12345678, photo=InputFile)

            .. note::

                While creating the FileInput currently requires a reasonable amount
                of preparation just to send a file. This class will be extended
                in the future to make the process easier.

    """
    __slots__ = ()


_UserProfilePhotosBase = namedtuple('UserProfilePhotos', ['total_count', 'photos'])


class UserProfilePhotos(_UserProfilePhotosBase):

    """This object represent a user's profile pictures.

    Attributes:
        total_count (int): Total number of profile pictures the target user has
        photos      (list of list of PhotoSize): Requested profile pictures (in up to 4 sizes each)

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        photos = []
        for photo_list in result.get('photos'):
            photos.append([PhotoSize.from_result(photo) for photo in photo_list])

        return UserProfilePhotos(
            total_count=result.get('total_count'),
            photos=photos
            )


class ReplyMarkup:
    __metaclass__ = ABCMeta
    __slots__ = ()

    @abstractmethod
    def serialize(self):
        raise NotImplementedError("")


_ReplyKeyboardMarkupBase = namedtuple('ReplyKeyboardMarkup', [
    'keyboard', 'resize_keyboard', 'one_time_keyboard', 'selective'])


class ReplyKeyboardMarkup(_ReplyKeyboardMarkupBase, ReplyMarkup):

    """This object represents a custom keyboard with reply options (see Introduction to bots for details and examples).

    Attributes:
        keyboard            (list of list of str)   :Array of button rows, each represented by an Array of Strings
        resize_keyboard     (bool)  :*Optional.* Requests clients to resize the keyboard vertically for optimal
                                        fit (e.g., make the keyboard smaller if there are just two rows of buttons).
                                        Defaults to false, in which case the custom keyboard is always of the
                                        same height as the app's standard keyboard.
        one_time_keyboard   (bool)  :*Optional.* Requests clients to hide the keyboard as soon as it's been
                                        used. Defaults to false.
        selective           (bool)  :*Optional.* Use this parameter if you want to show the keyboard to
                                        specific users only. Targets:

                                            1. users that are @mentioned in the text of the Message object;
                                            2. if the bot's message is a reply (has reply_to_message_id), sender
                                               of the original message.

                                        :example: A user requests to change the bot‘s language, bot replies to the
                                            request with a keyboard to select the new language. Other users in the
                                            group don’t see the keyboard.

    :Example:

        ::

                keyboard = [
                ['7', '8', '9'],
                ['4', '5', '6'],
                ['1', '2', '3'],
                     ['0']
                ]

                reply_markup = ReplyKeyboardMarkup.create(keyboard)
                bot.send_message(12345678, 'testing reply_markup', reply_markup=reply_markup)

    """
    __slots__ = ()

    @staticmethod
    def create(keyboard, resize_keyboard=None, one_time_keyboard=None, selective=None):
        return ReplyKeyboardMarkup(keyboard, resize_keyboard, one_time_keyboard, selective)

    def serialize(self):
        reply_markup = dict(keyboard=self.keyboard)

        if self.resize_keyboard is not None:
            reply_markup['resize_keyboard'] = bool(self.resize_keyboard)

        if self.one_time_keyboard is not None:
            reply_markup['one_time_keyboard'] = bool(self.one_time_keyboard)

        if self.selective is not None:
            reply_markup['selective'] = bool(self.selective)

        return json.dumps(reply_markup)


_ReplyKeyboardHideBase = namedtuple('ReplyKeyboardHide', ['hide_keyboard', 'selective'])


class ReplyKeyboardHide(_ReplyKeyboardHideBase, ReplyMarkup):

    """Upon receiving a message with this object, Telegram clients will hide the current custom keyboard and
        display the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard
        is sent by a bot. An exception is made for one-time keyboards that are hidden immediately after the
        user presses a button (see :class:`ReplyKeyboardMarkup`).

    Attributes:
        hide_keyboard   (``True``)  :Requests clients to hide the custom keyboard
        selective       (bool)      :*Optional.* Use this parameter if you want to hide keyboard for specific
                                    users only. Targets:

                                        1. users that are @mentioned in the text of the Message object;
                                        2. if the bot's message is a reply (has reply_to_message_id), sender
                                           of the original message.

                                    :example: A user votes in a poll, bot returns confirmation message in reply
                                        to the vote and hides keyboard for that user, while still showing the
                                        keyboard with poll options to users who haven't voted yet.

    """
    __slots__ = ()

    @staticmethod
    def create(selective=None):
        return ReplyKeyboardHide(True, selective)

    def serialize(self):
        reply_markup = dict(
            hide_keyboard=True
            )

        if self.selective is not None:
            reply_markup['selective'] = bool(self.selective)

        return json.dumps(reply_markup)


_ForceReplyBase = namedtuple('ForceReply', ['force_reply', 'selective'])


class ForceReply(_ForceReplyBase, ReplyMarkup):

    """Upon receiving a message with this object, Telegram clients will display a reply interface to the user
        (act as if the user has selected the bot‘s message and tapped ’Reply'). This can be extremely useful
        if you want to create user-friendly step-by-step interfaces without having to sacrifice privacy mode.

    Attributes:
        force_reply (``True``)  :Shows reply interface to the user, as if they manually selected the bot‘s
                                    message and tapped ’Reply'
        selective   (bool)      :Optional. Use this parameter if you want to force reply from specific users
                                    only. Targets: 1) users that are @mentioned in the text of the Message
                                    object; 2) if the bot's message is a reply (has reply_to_message_id),
                                    sender of the original message.

    :Example: A poll bot for groups runs in privacy mode (only receives commands, replies to its messages and
        mentions). There could be two ways to create a new poll:

            * Explain the user how to send a command with parameters (e.g. /newpoll question answer1 answer2).
              May be appealing for hardcore users but lacks modern day polish.
            * Guide the user through a step-by-step process. ‘Please send me your question’, ‘Cool, now let’s
              add the first answer option‘, ’Great. Keep adding answer options, then send /done when you‘re ready’.

    The last option is definitely more attractive. And if you use ForceReply in your bot‘s questions, it will
    receive the user’s answers even if it only receives replies, commands and mentions — without any extra
    work for the user.

    """
    __slots__ = ()

    @staticmethod
    def create(selective=None):
        return ForceReply(True, selective)

    def serialize(self):
        reply_markup = dict(force_reply=True)
        if self.selective is not None:
            reply_markup['selective'] = bool(self.selective)

        return json.dumps(reply_markup)


"""
Types added for utility purposes
"""


_ErrorBase = namedtuple('Error', ['error_code', 'description'])


class Error(_ErrorBase):

    """The error code and message returned when a request was successfuly but the method call was invalid

    Attributes:
        error_code  (int)   :An Integer ‘error_code’ field is also returned, but its
                            contents are subject to change in the future.
        description (str)   :The description of the error as reported by Telegram

    """
    __slots__ = ()

    @staticmethod
    def from_result(result):
        return Error(error_code=result.get('error_code'), description=result.get('description'))

"""
RPC Objects
"""


class RequestMethod(str, Enum):

    """Used to specify the HTTP request method.

    Attributes:
        GET : 'GET'
        POST: 'POST'

    :example:

    ::

        bot.get_me(request_method=RequestMethod.GET)

    """
    GET = 'GET'
    POST = 'POST'


class TelegramBotRPCRequest:

    """Class that handles creating the actual RPC request, and sending callbacks based on response

    :param api_method: The API method to call. See https://core.telegram.org/bots/api#available-methods
    :param token: The API token generated following the instructions at https://core.telegram.org/bots#botfather
    :param params: A dictionary mapping the api method parameters to their arguments
    :param on_result: a callback function that gets called before when te request finishes. The return value
                      of this function gets passed to on_success. Useful if you wish to override the generated
                      result type
    :param on_success: a callback function that gets called when the api call was successful, gets passed
                       the return value from on_result
    :param on_error: called when an error occurs
    :param files: a list of :class:`InputFile`s to be sent to the server`
    :param request_method: ``RequestMethod.POST`` or ``RequestMethod.GET``

    :type api_method: str
    :type token: str
    :type params: dict
    :type on_result: callable
    :type on_success: callable
    :type on_error: callable
    :type files: `list` of :class:`InputFile`
    :type request_method: RequestMethod

    .. note::

        Typically you do not have to interact with this class directly. However, you may override any of these
        arguments by specifiying it in the the `\*\*kwargs` of any api method.
    """

    api_url_base = 'https://api.telegram.org/bot'

    def __init__(self, api_method, token, params=None, on_result=None, on_success=None, callback=None,
                 on_error=None, files=None, request_method=RequestMethod.POST):
        reply_markup = params.get('reply_markup') if params else None
        if reply_markup is not None:
            params['reply_markup'] = reply_markup.serialize()

        if callback is not None:
            print('WARNING: callback is deprecated in favor of on_success')
            if on_success:
                print('WARNING: callback parameter will be ignored, on_success will be used instead')
            else:
                on_success = callback

        self.api_method = api_method
        self.token = token
        self.params = params
        self.on_result = on_result
        self.on_success = on_success
        self.on_error = on_error
        self.files = files
        self.request_method = RequestMethod(request_method)

        self.result = None
        self.error = None

        self.thread = Thread(target=self._async_call)

    def _get_url(self):
        return '{base_url}{token}/{method}'.format(base_url=TelegramBotRPCRequest.api_url_base,
                                                   token=self.token,
                                                   method=self.api_method)

    def _get_request(self):
        data, files = None, None
        if self.params is not None:
            data = self.params
        if self.files is not None:
            files = self.files

        return Request(self.request_method, self._get_url(), data=data, files=files).prepare()

    def _async_call(self):
        self.error = None
        self.response = None

        s = Session()
        request = self._get_request()
        resp = s.send(request)

        try:
            api_response = resp.json()
        except ValueError:
            api_response = {'ok': False, 'description': 'Invalid Value in JSON response'}

        if api_response.get('ok'):
            result = api_response['result']
            if self.on_result is None:
                self.result = result
            else:
                self.result = self.on_result(result)

            if self.on_success is not None:
                self.on_success(self.result)
        else:
            self.error = Error.from_result(api_response)
            if self.on_error:
                self.on_error(self.error)

        return None

    def run(self):
        self.thread.start()

        return self

    def join(self, timeout=None):
        self.thread.join(timeout)
        return self

    def wait(self):
        """
        Wait for the request to finish and return the result or error when finished

        :returns: result or error
        :type: result tyoe or Error
        """
        self.thread.join()
        if self.error is not None:
            return self.error
        return self.result


def _clean_params(**params):
    return {name: val for name, val in params.items() if val is not None}


"""
Telegram Bot API Methods as defined at https://core.telegram.org/bots/api#available-methods
"""


def get_me(**kwargs):
    """
    A simple method for testing your bot's auth token. Requires no parameters.
    Returns basic information about the bot in form of a User object.

    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :returns: Returns basic information about the bot in form of a User object.
    :rtype: User
    """
    return TelegramBotRPCRequest('getMe', on_result=User.from_result, **kwargs)


def send_message(chat_id, text,
                 disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None,
                 **kwargs):
    """
    Use this method to send text messages.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param text: Text of the message to be sent
    :param disable_web_page_preview: Disables link previews for links in this message
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a
                         custom reply keyboard, instructions to hide keyboard or to
                         force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type text: str
    :type disable_web_page_preview: bool
    :type reply_to_message_id: int
    :type reply_markup: :class:`ReplyKeyboardMarkup` or :class:`ReplyKeyboardHide` or :class:`ForceReply`

    :returns: On success, the sent Message is returned.
    :rtype: Message

    """
    # required args
    params = dict(chat_id=chat_id, text=text)

    # optional args
    params.update(_clean_params(
        disable_web_page_preview=disable_web_page_preview,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendMessage', params=params, on_result=Message.from_result, **kwargs)


def forward_message(chat_id, from_chat_id, message_id,
                    **kwargs):
    """
    Use this method to forward messages of any kind.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param from_chat_id: Unique identifier for the chat where the original message was sent — User or
                         GroupChat id
    :param message_id: Unique message identifier
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type from_chat_id: int
    :type message_id: int

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """

    # required args
    params = dict(
        chat_id=chat_id,
        from_chat_id=from_chat_id,
        message_id=message_id
    )

    return TelegramBotRPCRequest('forwardMessage', params=params, on_result=Message.from_result, **kwargs)


def send_photo(chat_id,  photo,
               caption=None, reply_to_message_id=None, reply_markup=None,
               **kwargs):
    """
    Use this method to send photos.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param photo: Photo to send. You can either pass a file_id as String to resend a
                  photo that is already on the Telegram servers, or upload a new photo
                  using multipart/form-data.
    :param caption: Photo caption (may also be used when resending photos by file_id).
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a
                         custom reply keyboard, instructions to hide keyboard or to
                         force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type photo: InputFile or str
    :type caption: str
    :type reply_to_message_id: int
    :type reply_markup: :class:`ReplyKeyboardMarkup` or :class:`ReplyKeyboardHide` or :class:`ForceReply`

    :returns: On success, the sent Message is returned.
    :rtype: TelegramBotRPCRequest
    """

    files = None
    if isinstance(photo, InputFile):
        files = [photo]
        photo = None
    elif not isinstance(photo, str):
        raise Exception('photo must be instance of InputFile or str')

    # required args
    params = dict(
        chat_id=chat_id,
        photo=photo
    )

    # optional args
    params.update(
        _clean_params(
            caption=caption,
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendPhoto', params=params, files=files, on_result=Message.from_result, **kwargs)


def send_audio(chat_id, audio,
               reply_to_message_id=None, reply_markup=None,
               **kwargs):
    """
    Use this method to send audio files, if you want Telegram clients to display the file as a playable voice
    message. For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent
    as Document).

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param audio: Audio file to send. You can either pass a file_id as String to resend an audio that is already on
                  the Telegram servers, or upload a new audio file using multipart/form-data.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard,
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type audio: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: TelegramBotRPCRequest
    """
    files = None
    if isinstance(audio, InputFile):
        files = [audio]
        audio = None
    elif not isinstance(audio, str):
        raise Exception('audio must be instance of InputFile or str')

    # required args
    params = dict(
        chat_id=chat_id,
        audio=audio
    )

    # optional args
    params.update(
        _clean_params(
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendAudio', params=params, files=files, on_result=Message.from_result, **kwargs)


def send_document(chat_id, document,
                  reply_to_message_id=None, reply_markup=None,
                  **kwargs):
    """
    Use this method to send general files.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param document: File to send. You can either pass a file_id as String to resend a file that is already on
                     the Telegram servers, or upload a new file using multipart/form-data.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard,
                         instructions to hide keyboard or to force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type document: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: TelegramBotRPCRequest
    """
    files = None
    if isinstance(document, InputFile):
        files = [document]
        document = None
    elif not isinstance(document, str):
        raise Exception('document must be instance of InputFile or str')

    # required args
    params = dict(
        chat_id=chat_id,
        document=document
    )

    # optional args
    params.update(
        _clean_params(
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendDocument', params=params, files=files, on_result=Message.from_result, **kwargs)


def send_sticker(chat_id, sticker,
                 reply_to_message_id=None, reply_markup=None,
                 **kwargs):
    """
    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param sticker: Sticker to send. You can either pass a file_id as String to resend a sticker
                    that is already on the Telegram servers, or upload a new sticker using multipart/form-data.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard,
                         instructions to hide keyboard or to force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type sticker: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: TelegramBotRPCRequest
    """
    files = None
    if isinstance(sticker, InputFile):
        files = [sticker]
        sticker = None
    elif not isinstance(sticker, str):
        raise Exception('sticker must be instance of InputFile or str')

    # required args
    params = dict(
        chat_id=chat_id,
        sticker=sticker
    )

    # optional args
    params.update(
        _clean_params(
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendSticker', params=params, files=files, on_result=Message.from_result, **kwargs)


def send_video(chat_id, video,
               reply_to_message_id=None, reply_markup=None,
               **kwargs):
    """
    Use this method to send video files, Telegram clients support mp4 videos (other formats may be sent as Document).

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param video: Video to send. You can either pass a file_id as String to resend a
                  video that is already on the Telegram servers, or upload a new video
                  using multipart/form-data.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a
                         custom reply keyboard, instructions to hide keyboard or to
                         force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type video: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype:  TelegramBotRPCRequest
    """
    files = None
    if isinstance(video, InputFile):
        files = [video]
        video = None
    elif not isinstance(video, str):
        raise Exception('video must be instance of InputFile or str')

    # required args
    params = dict(
        chat_id=chat_id,
        video=video
    )

    # optional args
    params.update(
        _clean_params(
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendVideo', params=params, files=files, on_result=Message.from_result, **kwargs)


def send_location(chat_id, latitude, longitude,
                  reply_to_message_id=None, reply_markup=None,
                  **kwargs):
    """
    Use this method to send point on the map.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param latitude: Latitude of location.
    :param longitude: Longitude of location.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a
                         custom reply keyboard, instructions to hide keyboard or to
                         force a reply from the user.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type latitude: float
    :type longitude: float
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype:  TelegramBotRPCRequest
    """

    # required args
    params = dict(
        chat_id=chat_id,
        latitude=latitude,
        longitude=longitude
    )

    # optional args
    params.update(
        _clean_params(
            reply_to_message_id=reply_to_message_id,
            reply_markup=reply_markup
        )
    )

    return TelegramBotRPCRequest('sendLocation', params=params, on_result=Message.from_result, **kwargs)


class ChatAction(str, Enum):
    TEXT = 'typing'
    PHOTO = 'upload_photo'
    RECORD_VIDEO = 'record_video'
    VIDEO = 'upload_video'
    RECORD_AUDIO = 'record_audio'
    AUDIO = 'upload_audio'
    DOCUMENT = 'upload_document'
    LOCATION = 'find_location'


def send_chat_action(chat_id, action,
                     **kwargs):
    """
    Use this method when you need to tell the user that something is happening on the bot's side. The status is set
     for 5 seconds or less (when a message arrives from your bot, Telegram clients clear its typing status).

    Example: The ImageBot needs some time to process a request and upload the image. Instead of sending a text message
    along the lines of “Retrieving image, please wait…”, the bot may use sendChatAction with action = upload_photo.
    The user will see a “sending photo” status for the bot.

    We only recommend using this method when a response from the bot will take a noticeable amount of time to arrive.

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param action: Type of action to broadcast.  Choose one, depending on what the user is about to receive:
                   typing for text messages, upload_photo for photos, record_video or upload_video for videos,
                   record_audio or upload_audio for audio files, upload_document for general files,
                   find_location for location data.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type chat_id: int
    :type action: ChatAction

    :returns: Returns True on success.
    :rtype:  bool
    """
    # required args
    params = dict(
        chat_id=chat_id,
        action=action
    )

    return TelegramBotRPCRequest('sendChatAction', params=params, on_result=lambda result: result, **kwargs)


def get_user_profile_photos(user_id,
                            offset=None, limit=None,
                            **kwargs):
    """
    Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

    :param user_id: Unique identifier of the target user
    :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
    :param limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type user_id: int
    :type offset: int
    :type limit: int

    :returns: Returns a UserProfilePhotos object.
    :rtype: TelegramBotRPCRequest
    """
    # required args
    params = dict(user_id=user_id)

    # optional args
    params.update(
        _clean_params(
            offset=offset,
            limit=limit
        )
    )

    return TelegramBotRPCRequest('getUserProfilePhotos', params=params,
                                 on_result=UserProfilePhotos.from_result, **kwargs)


def get_updates(offset=None, limit=None, timeout=None,
                **kwargs):
    """
    Use this method to receive incoming updates using long polling.

    .. note::

        1. This method will not work if an outgoing webhook is set up.
        2. In order to avoid getting duplicate updates, recalculate offset after each server response.

    :param offset: Identifier of the first update to be returned. Must be
                   greater by one than the highest among the identifiers of
                   previously received updates. By default, updates starting
                   with the earliest unconfirmed update are returned. An update
                   is considered confirmed as soon as getUpdates is called with
                   an offset higher than its update_id.
    :param limit: Limits the number of updates to be retrieved. Values between
                  1—100 are accepted. Defaults to 100
    :param timeout: Timeout in seconds for long polling. Defaults to 0, i.e.
                    usual short polling
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type offset: int
    :type limit: int
    :type timeout: int

    :returns: An Array of Update objects is returned.
    :rtype: TelegramBotRPCRequest
    """
    # optional parameters
    params = _clean_params(
            offset=offset,
            limit=limit,
            timeout=timeout
        )

    return TelegramBotRPCRequest('getUpdates', params=params, on_result=Update.from_result, **kwargs)


def set_webhook(url=None, **kwargs):
    """
    Use this method to specify a url and receive incoming updates via an outgoing webhook.
    Whenever there is an update for the bot, we will send an HTTPS POST request to the specified url, containing a
    JSON-serialized Update. In case of an unsuccessful request, we will give up after a reasonable amount of attempts.

    Please note that you will not be able to receive updates using getUpdates for as long as an outgoing
    webhook is set up.

    :param url: HTTPS url to send updates to. Use an empty string to remove webhook integration
    :param \*\*kwargs: Args that get passed down to :class:`TelegramBotRPCRequest`

    :type url: str

    :returns: Returns True on success.
    :rtype:  TelegramBotRPCRequest
    """
    # optional args
    params = _clean_params(url=url)

    return TelegramBotRPCRequest('setWebhook', params=params, on_result=lambda result: result, **kwargs)


class TelegramBot:

    """A `TelegramBot` object represents a specific regisitered bot user as identified by its token. The bot
    object also helps try to maintain state and simplify interaction for library users.

    Attributes:
        token (str) :The api token generated by BotFather
        request_method (`RequestMethod` or `str`) :*Optional.* The http method to use
                                                    (e.g. 'POST' or RequestMethod.POST')

    .. note::

        Unlike the unbound API methods, when the bot executes an API call, ``run()`` is immediately called
        on the request object.

    """

    def __init__(self, token, request_method=RequestMethod.POST):
        self._bot_user = None

        self.request_args = dict(
            token=token,
            request_method=request_method
        )

    def __str__(self):
        return self.token

    def _merge_overrides(self, **kwargs):
        ra = self.request_args.copy()
        ra.update(kwargs)
        return ra

    def get_me(self, *args, **kwargs):
        """See :func:`get_me`"""
        return get_me(*args, **self._merge_overrides(**kwargs)).run()

    def send_message(self, *args, **kwargs):
        """See :func:`send_message`"""
        return send_message(*args, **self._merge_overrides(**kwargs)).run()

    def forward_message(self, *args, **kwargs):
        """See :func:`forward_message`"""
        return forward_message(*args, **self._merge_overrides(**kwargs)).run()

    def send_photo(self, *args, **kwargs):
        """See :func:`send_photo`"""
        return send_photo(*args, **self._merge_overrides(**kwargs)).run()

    def send_audio(self, *args, **kwargs):
        """See :func:`send_audio`"""
        return send_audio(*args, **self._merge_overrides(**kwargs)).run()

    def send_document(self, *args, **kwargs):
        """See :func:`send_document`"""
        return send_document(*args, **self._merge_overrides(**kwargs)).run()

    def send_sticker(self, *args, **kwargs):
        """See :func:`send_sticker`"""
        return send_sticker(*args, **self._merge_overrides(**kwargs)).run()

    def send_video(self, *args, **kwargs):
        """See :func:`send_video`"""
        return send_video(*args, **self._merge_overrides(**kwargs)).run()

    def send_location(self, *args, **kwargs):
        """See :func:`send_location`"""
        return send_location(*args, **self._merge_overrides(**kwargs)).run()

    def send_chat_action(self, *args, **kwargs):
        """See :func:`send_chat_action`"""
        return send_chat_action(*args, **self._merge_overrides(**kwargs)).run()

    def get_user_profile_photos(self, *args, **kwargs):
        """See :func:`get_user_profile_photos`"""
        return get_user_profile_photos(*args, **self._merge_overrides(**kwargs)).run()

    def get_updates(self, *args, **kwargs):
        """See :func:`get_updates`"""
        return get_updates(*args, **self._merge_overrides(**kwargs)).run()

    def set_webhook(self, *args, **kwargs):
        """See :func:`set_webhook`"""
        return set_webhook(*args, **self._merge_overrides(**kwargs)).run()

    def _update_bot_info(self, response):
        self._bot_user = response

    def update_bot_info(self):
        return self.get_me(callback=self._update_bot_info)

    @property
    def token(self):
        return self.request_args['token']

    @token.setter
    def token(self, val):
        self.request_args['token'] = val

    @property
    def request_method(self):
        return self.request_args['request_method']

    @request_method.setter
    def request_method(self, val):
        self.request_args['request_method'] = val

    @property
    def id(self):
        if self._bot_user is not None:
            return self._bot_user.id

    @property
    def first_name(self):
        if self._bot_user is not None:
            return self._bot_user.first_name

    @property
    def last_name(self):
        if self._bot_user is not None:
            return self._bot_user.last_name

    @property
    def username(self):
        if self._bot_user is not None:
            return self._bot_user.username
