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
_InputFile = namedtuple('InputFile', [])

_Error = namedtuple('Error', ['error_code', 'description'])

class User(_UserBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return User(
            id=_dict.get('id'), 
            first_name=_dict.get('first_name'),
            last_name=_dict.get('last_name'),
            username=_dict.get('username')
            )

class GroupChat(_GroupChatBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return GroupChat(
            id=_dict.get('id'), 
            title=_dict.get('title')
            )

class Message(_MessageBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None
        return Message(
            message_id=_dict.get('message_id'), 
            sender=User.from_dict(_dict.get('from')),
            date=_dict.get('date'),
            chat=_dict.get('chat'), # TODO: May be User or GroupChat
            forward_from=User.from_dict(_dict.get('forward_from')),
            forward_date=_dict.get('forward_date'),
            reply_to_message=Message.from_dict(_dict.get('reply_to_message')),
            text=_dict.get('text'),
            audio=Audio.from_dict(_dict.get('audio')),
            document=Document.from_dict(_dict.get('document')),
            photo=_dict.get('photo'), # TODO: Array of PhotoSize
            sticker=Sticker.from_dict(_dict.get('sticker')),
            video=Video.from_dict(_dict.get('video')),
            contact=Contact.from_dict(_dict.get('contact')),
            location=Location.from_dict(_dict.get('location')),
            new_chat_participant=User.from_dict(_dict.get('new_chat_participant')),
            left_chat_participant=User.from_dict(_dict.get('left_chat_participant')),
            new_chat_title=_dict.get('new_chat_title'),
            new_chat_photo=_dict.get('new_chat_photo'),
            delete_chat_photo=_dict.get('delete_chat_photo'),
            group_chat_created=_dict.get('group_chat_created')
            )

class PhotoSize(_PhotoSizeBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return PhotoSize(
            file_id=_dict.get('file_id'), 
            width=_dict.get('width'), 
            height=_dict.get('height'), 
            file_size=_dict.get('file_size')
            )

class Audio(_AudioBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Audio(
            file_id=_dict.get('file_id'), 
            duration=_dict.get('duration'), 
            mime_type=_dict.get('mime_type'), 
            file_size=_dict.get('file_size')
            )

class Document(_DocumentBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Document(
            file_id=_dict.get('file_id'), 
            thumb=PhotoSize.from_dict(_dict.get('thumb')), 
            file_name=_dict.get('file_name'), 
            mime_type=_dict.get('mime_type'), 
            file_size=_dict.get('file_size') 
            )

class Sticker(_StickerBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Sticker(
            file_id=_dict.get('file_id'), 
            width=_dict.get('width'), 
            height=_dict.get('height'), 
            thumb=PhotoSize.from_dict(_dict.get('thumb')), 
            file_size=_dict.get('file_size')
            )

class Video(_VideoBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Video(
            file_id=_dict.get('file_id'), 
            width=_dict.get('width'), 
            height=_dict.get('height'), 
            duration=_dict.get('duration'), 
            thumb=PhotoSize.from_dict(_dict.get('thumb')), 
            mime_type=_dict.get('mime_type'), 
            file_size=_dict.get('file_size'), 
            caption=_dict.get('caption')
            )

class Contact(_ContactBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Contact(
            phone_number=_dict.get('phone_number'), 
            first_name=_dict.get('first_name'), 
            last_name=_dict.get('last_name'), 
            user_id=_dict.get('user_id')
            )

class Location(_LocationBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return Location(
            longitude=_dict.get('longitude'), 
            latitude=_dict.get('latitude')
            )

class UserProfilePhotos(_UserProfilePhotosBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        if _dict is None:
            return None

        return UserProfilePhotos(
            total_count=_dict.get('total_count'), 
            photos=_dict.get('photos') #TODO: Array of Array of PhotoSize
            )

class ReplyMarkup:
    __slots__ = ()

class ReplyKeyboardMarkup(_ReplyKeyboardMarkupBase, ReplyMarkup):
    __slots__ = ()

class ReplyKeyboardHide(_ReplyKeyboardHideBase, ReplyMarkup):
    __slots__ = ()

class ForceReply(_ForceReplyBase, ReplyMarkup):
    __slots__ = ()

class InputFile(_InputFile):
    __slots__ = ()

class Error(_Error):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        return Error(error_code=_dict.get('error_code'), description=_dict.get('description'))

class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'

class TelegramBotRPCRequest(metaclass=ABCMeta):
    api_url_base = 'https://api.telegram.org/bot'

    def __init__(self, api_method, token, *, params=None, callback=None, on_error=None, files=None, request_method=RequestMethod.GET):
        self.api_method = api_method
        self.token = token
        self.params = params
        self.callback = callback
        self.on_error = on_error
        self.files = files
        self.request_method = RequestMethod(request_method)

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

    @abstractmethod
    def _call_result(self, api_response):
        raise NotImplemented

    def _async_call(self):
        self.error = None
        self.response = None

        s = Session()
        request = self._get_request()
        resp = s.send(request)
        api_response = resp.json()

        if api_response.get('ok') == True:
            self.result = self._call_result(api_response)

            if self.callback is not None:
                self.callback(self.result)
        else:
            self.error = Error.from_dict(api_response)
            if self.on_error:
                self.on_error(self.error)

        return None

    def run(self):
        self._async_call()
        return self

    def cleanup_params(self, **kwargs):
        return {name:val for name, val in kwargs.items() if val is not None}

class getMeRequest(TelegramBotRPCRequest):
    def __init__(self, token:str, *, callback=None, on_error=None, request_method: RequestMethod=None):
        super().__init__('getMe', token, callback=callback, on_error=on_error, request_method=request_method)

    def _call_result(self, api_response):
        return User.from_dict(api_response['result'])

class sendMessageRequest(TelegramBotRPCRequest):
    def __init__(self, token:str, chat_id:int, text:str, 
                 disable_web_page_preview: bool=None, 
                 reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, 
                 *, callback=None, on_error=None, request_method=None):

        params = self.cleanup_params(chat_id=chat_id, text=text, 
                                     disable_web_page_preview=disable_web_page_preview, 
                                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

        super().__init__('sendMessage', token, params=params, callback=callback, on_error=on_error, request_method=request_method)

    def _call_result(self, api_response):
        result = api_response['result']
        return Message.from_dict(result)


class sendPhotoRequest(TelegramBotRPCRequest):
    def __init__(self, token, chat_id, caption, reply_to_message_id, reply_markup, photo_id=None, photo=None,
                 *, callback=None, on_error=None, request_method=None):

        files = None

        if photo_id:
            photo = photo_id
        else:
            files = {'photo': (photo, open(photo, 'rb'), 'image/jpeg')}

        params = self.cleanup_params(token=token, chat_id=chat_id, photo=photo, caption=caption,
                                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

        super().__init__('sendPhoto', token, params=params, callback=callback, on_error=on_error,
                         files=files, request_method=request_method)

    def _call_result(self, api_response):
        print(api_response)
        result = api_response['result']
        return Message.from_dict(result)

class TelegramBotRPC:
    @staticmethod
    def get_me(token, *, callback=None, on_error=None, request_method: RequestMethod=RequestMethod.GET):
        return getMeRequest(token, callback=callback, on_error=on_error, request_method=request_method).run()

    @staticmethod
    def send_message(token, chat_id: int, text: str, disable_web_page_preview: bool=None, 
                     reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, 
                     *, callback=None, on_error=None, request_method: RequestMethod=RequestMethod.GET):

        return sendMessageRequest(token, chat_id, text, disable_web_page_preview, reply_to_message_id, reply_markup,
                                  callback=callback, on_error=on_error, request_method=request_method).run()

    @staticmethod
    def send_photo(token, chat_id: int,  caption: str=None, reply_to_message_id: int=None, 
                   reply_markup: ReplyMarkup=None, photo: str=None, photo_id: str=None,
                   *, callback=None, on_error=None, request_method: RequestMethod=RequestMethod.POST):

        if bool(photo) == bool(photo_id):
            raise TypeError("sendPhotoRequest() requires either photo or photo_id kwarg must be set.")

        return sendPhotoRequest(token, chat_id, caption, reply_to_message_id, reply_markup, photo=photo, photo_id=photo_id,
                                callback=callback, on_error=on_error, request_method=request_method).run()



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

    TelegramBotRPC.get_me(test_token, callback=print_result)
    TelegramBotRPC.send_message(test_token, test_chat_id, 'testing', callback=print_result)
    TelegramBotRPC.send_photo(test_token, test_chat_id,
                              photo='test.jpg',
                              callback=print_result)
    TelegramBotRPC.send_photo(test_token, test_chat_id,
                              photo_id='AgADAwADqacxGwpPWQaFLwABSzSkg2Bq-usqAASiGyniRUnk5BdEAAIC',
                              callback=print_result, on_error=print_error)
