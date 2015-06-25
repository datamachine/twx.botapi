from requests import Request, Session
from collections import namedtuple
from enum import Enum
from abc import ABCMeta, abstractmethod

_UserBase = namedtuple('User', ['id', 'first_name', 'last_name', 'username'])
_GroupChatBase = namedtuple('GroupChat', ['id', 'title'])
_MessageBase = namedtuple('Message', ['message_id', 'sender', 'date', 
                                      'chat', 'forward_from', 'forward_date', 'reply_to_message', 
                                      'text', 'audio', 'document', 'photo', 'sticker', 'video', 'contact', 'location', 
                                      'new_chat_participant', 'left_chat_participant', 'new_chat_title', 
                                      'new_chat_photo', 'delete_chat_photo', 'group_chat_created'])
_PhotoSizeBase = namedtuple('PhotoSize', ['file_id', 'width', 'height', 'file_size'])
_AudioBase = namedtuple('Audio', ['file_id', 'duration', 'mime_type', 'file_size'])
_DocumentBase = namedtuple('Document', ['file_id', 'thumb', 'file_name', 'mime_type', 'file_size'])
_StickerBase = namedtuple('Sticker', ['file_id', 'width', 'height', 'thumb', 'file_size'])
_VideoBase = namedtuple('Video', ['file_id', 'width', 'height', 'duration', 'thumb', 'mime_type',
                                  'file_size', 'caption'])
_ContactBase = namedtuple('Contact', ['phone_number', 'first_name', 'last_name', 'user_id'])
_LocationBase = namedtuple('Location', ['longitude', 'latitude'])
_UserProfilePhotosBase = namedtuple('UserProfilePhotos', ['total_count', 'photos'])
_ReplyKeyboardMarkupBase = namedtuple('ReplyKeyboardMarkup', ['keyboard', 'resize_keyboard',
                                                              'one_time_keyboard', 'selective'])
_ReplyKeyboardHideBase = namedtuple('ReplyKeyboardHide', ['hide_keyboard', 'selective'])
_ForceReplyBase = namedtuple('ForceReply', ['force_reply', 'selective'])
_InputFileInfoBase = namedtuple('InputFileInfo', ['file_name', 'fp', 'mime_type'])
_InputFileBase = namedtuple('InputFile', ['form', 'file_info' ])

_Error = namedtuple('Error', ['error_code', 'description'])

class User(_UserBase):
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

class GroupChat(_GroupChatBase):
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return GroupChat(
            id=result.get('id'), 
            title=result.get('title')
            )

class Message(_MessageBase):
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None
        return Message(
            message_id=result.get('message_id'), 
            sender=User.from_result(result.get('from')),
            date=result.get('date'),
            chat=result.get('chat'), # TODO: May be User or GroupChat
            forward_from=User.from_result(result.get('forward_from')),
            forward_date=result.get('forward_date'),
            reply_to_message=Message.from_result(result.get('reply_to_message')),
            text=result.get('text'),
            audio=Audio.from_result(result.get('audio')),
            document=Document.from_result(result.get('document')),
            photo=result.get('photo'), # TODO: Array of PhotoSize
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

class PhotoSize(_PhotoSizeBase):
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

class Audio(_AudioBase):
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

class Document(_DocumentBase):
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

class Sticker(_StickerBase):
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

class Video(_VideoBase):
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

class Contact(_ContactBase):
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

class Location(_LocationBase):
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return Location(
            longitude=result.get('longitude'), 
            latitude=result.get('latitude')
            )

class UserProfilePhotos(_UserProfilePhotosBase):
    __slots__ = ()

    @staticmethod
    def from_result(result):
        if result is None:
            return None

        return UserProfilePhotos(
            total_count=result.get('total_count'), 
            photos=result.get('photos') #TODO: Array of Array of PhotoSize
            )

class ReplyMarkup:
    __slots__ = ()

class ReplyKeyboardMarkup(_ReplyKeyboardMarkupBase, ReplyMarkup):
    __slots__ = ()

class ReplyKeyboardHide(_ReplyKeyboardHideBase, ReplyMarkup):
    __slots__ = ()

class ForceReply(_ForceReplyBase, ReplyMarkup):
    __slots__ = ()

class InputFileInfo(_InputFileInfoBase):
    __slots__ = ()

class InputFile(_InputFileBase):
    __slots__ = ()


class Error(_Error):
    __slots__ = ()

    @staticmethod
    def from_result(result):
        return Error(error_code=result.get('error_code'), description=result.get('description'))

class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'

class TelegramBotRPCRequest(metaclass=ABCMeta):
    api_url_base = 'https://api.telegram.org/bot'

    def __init__(self, api_method, token, *, params=None, callback=None, on_result=None, on_error=None, files=None, request_method=RequestMethod.GET):
        self.api_method = api_method
        self.token = token
        self.params = params
        self.callback = callback
        self.on_error = on_error
        self.files = files
        self.request_method = RequestMethod(request_method)
        self.on_result = on_result

        self.result = None
        self.error = None

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
        api_response = resp.json()

        if api_response.get('ok') == True:
            result = api_response['result']
            if self.on_result is None:
                self.result = result
            else:
                self.result = self.on_result(result)

            if self.callback is not None:
                self.callback(self.result)
        else:
            self.error = Error.from_result(api_response)
            if self.on_error:
                self.on_error(self.error)

        return None

    def run(self):
        self._async_call()
        return self

def _cleanup_params(**kwargs):
    return {name:val for name, val in kwargs.items() if val is not None}

def get_me(token, **kwargs):
    """
    A simple method for testing your bot's auth token. Requires no parameters. 
    Returns basic information about the bot in form of a User object.

    :returns: Returns basic information about the bot in form of a User object.
    :rtype: User
    """
    return TelegramBotRPCRequest('getMe', token, on_result=User.from_result, **kwargs).run()

def send_message(token, chat_id: int, text: str, 
                 disable_web_page_preview: bool=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, 
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

    :type chat_id: int
    :type text: str
    :type disable_web_page_preview: bool
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """    
    params = _cleanup_params(
        chat_id=chat_id, 
        text=text, 
        disable_web_page_preview=disable_web_page_preview,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
        )

    return TelegramBotRPCRequest('sendMessage', token, params=params, on_result=Message.from_result, **kwargs).run()

def forward_message(token, chat_id, from_chat_id, message_id, **kwargs):
    """
    Use this method to forward messages of any kind. 

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param from_chat_id: Unique identifier for the chat where the original message was sent — User or GroupChat id
    :param message_id: Unique message identifier


    :type chat_id: int
    :type from_chat_id: int
    :type message_id: int

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """
    #TODO: implement
    return None

def send_photo(token, chat_id: int,  photo: InputFile, 
               caption: str=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None,
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

    :type chat_id: int
    :type photo: InputFile or str
    :type caption: str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """

    files = None
    if isinstance(photo, InputFile):
        files = [photo]
        photo = None
    elif not isinstance(photo, str):
        raise Exception('photo must be instance of InputFile or str')

    params = _cleanup_params(
        chat_id=chat_id,
        photo=photo,
        caption=caption,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
        )

    return TelegramBotRPCRequest('sendPhoto', token, params=params, files=files, on_result=Message.from_result, **kwargs).run()

def send_audio(token, chat_id: int, audio: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, **kwargs):
    """
    Use this method to send audio files, if you want Telegram clients to display the file as a playable voice
    message. For this to work, your audio must be in an .ogg file encoded with OPUS (other formats may be sent 
    as Document). 

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param audio: Audio file to send. You can either pass a file_id as String to resend an audio that is already on
                  the Telegram servers, or upload a new audio file using multipart/form-data.
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a custom reply keyboard, 
                         instructions to hide keyboard or to force a reply from the user.

    :type chat_id: int
    :type audio: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """
    #TODO: implement
    return None

def send_document(token, chat_id, document, reply_to_message_id=None, reply_markup=None, **kwargs):
    """
    :param chat_id: 
    :param document: 
    :param reply_to_message_id: 
    :param reply_markup: 

    :type chat_id: 
    :type document: 
    :type reply_to_message_id: 
    :type reply_markup: 

    :returns:
    :rtype:
    """
    # TODO: Implement
    return None

def send_sticker(token, chat_id, sticker, reply_to_message_id, reply_markup, **kwargs):
    """
    :param token: 
    :param chat_id: 
    :param sticker: 
    :param reply_to_message_id: 
    :param reply_markup: 

    :type token: 
    :type chat_id: 
    :type sticker: 
    :type reply_to_message_id: 
    :type reply_markup: 

    :returns:
    :rtype:
    """
    #TODO: implement
    return None

def print_result(result):
    print(result)

def print_error(result):
    print(result)

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read("test.conf")
    test_token = config['Test']['token']
    test_chat_id = config['Test']['chat_id']

    photo = InputFile('photo', InputFileInfo('test.jpg', open('test.jpg', 'rb'), 'image/jpeg'))

    get_me(test_token, callback=print_result)
    send_message(test_token, test_chat_id, 'testing', callback=print_result)
    send_photo(test_token, test_chat_id, photo, callback=print_result)
    #TelegramBotRPC.send_photo(test_token, test_chat_id, 'AgADAwADqacxGwpPWQaFLwABSzSkg2Bq-usqAASiGyniRUnk5BdEAAIC',
    #                         callback=print_result, on_error=print_error)
