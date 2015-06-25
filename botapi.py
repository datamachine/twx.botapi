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
_VideoBase = namedtuple('Video', ['file_id', 'width', 'height', 'duration', 'thumb', 'mime_type', 'file_size', 'caption'])
_ContactBase = namedtuple('Contact', ['phone_number', 'first_name', 'last_name', 'user_id'])
_LocationBase = namedtuple('Location', ['longitude', 'latitude'])
_UserProfilePhotosBase = namedtuple('UserProfilePhotos', ['total_count', 'photos'])
_ReplyKeyboardMarkupBase = namedtuple('ReplyKeyboardMarkup', ['keyboard', 'resize_keyboard', 'one_time_keyboard', 'selective'])
_ReplyKeyboardHideBase = namedtuple('ReplyKeyboardHide', ['hide_keyboard', 'selective'])
_ForceReplyBase = namedtuple('ForceReply', ['force_reply', 'selective'])
_InputFile = namedtuple('InputFile', [])

class User(_UserBase):
    __slots__ = ()

    @staticmethod
    def from_dict(_dict):
        return User(
            id=_dict.get('id'), 
            first_name=_dict.get('first_name'),
            last_name=_dict.get('last_name'),
            username=_dict.get('username')
            )

class GroupChat(_GroupChatBase):
    __slots__ = ()

class Message(_MessageBase):
    __slots__ = ()

class PhotoSize(_PhotoSizeBase):
    __slots__ = ()

class Audio(_AudioBase):
    __slots__ = ()

class Document(_DocumentBase):
    __slots__ = ()

class Sticker(_StickerBase):
    __slots__ = ()

class Video(_VideoBase):
    __slots__ = ()

class Contact(_ContactBase):
    __slots__ = ()

class Location(_LocationBase):
    __slots__ = ()

class UserProfilePhotos(_UserProfilePhotosBase):
    __slots__ = ()

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

class RequestMethod(str, Enum):
    GET = 'GET'
    POST = 'POST'

class TelegramBotRPCRequest(metaclass=ABCMeta):
    api_url_base = 'https://api.telegram.org/bot'

    def __init__(self, api_method, token, params, callback, files=None, request_method=RequestMethod.GET):
        self.api_method = api_method
        self.token = token
        self.callback = callback
        self.params = params
        self.files = files
        self.request_method = request_method
        self.result = None

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

    def _async_call(self, callback):
        s = Session()
        request = self._get_request()
        print(request.body)
        resp = s.send(request)
        api_response = resp.json()
        print(api_response)
        self.result = self._call_result(api_response)
        if callback is not None:
            callback(self.result)
        return None

    def run(self):
        self._async_call(self.callback)
        return self

    def cleanup_params(self, **kwargs):
        return {name:val for name, val in kwargs.items() if val is not None}

class getMeRequest(TelegramBotRPCRequest):
    def __init__(self, token, callback=None, request_method=None):
        super().__init__('getMe', token=token, params=None, callback=callback, request_method=request_method)

    def _call_result(self, api_response):
        return User.from_dict(api_response['result'])

class sendMessageRequest(TelegramBotRPCRequest):
    def __init__(self, token, chat_id, text, disable_web_page_preview, 
                 reply_to_message_id, reply_markup, 
                 callback=None, request_method=None):

        params = self.cleanup_params(chat_id=chat_id, text=text, 
                                     disable_web_page_preview=disable_web_page_preview, 
                                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

        print('sendMessageRequest', params)

        super().__init__('sendMessage', token=token, params=params, callback=callback, request_method=request_method)

    def _call_result(self, api_response):
        result = api_response['result']
        return Message(
                message_id=result.get('message_id'),
                sender=result.get('from'),
                date=result.get('date'),
                chat=result.get('chat'),
                forward_from=result.get('forward_from'),
                forward_date=result.get('forward_date'),
                reply_to_message=result.get('reply_to_message'),
                text=result.get('text'),
                audio=result.get('audio'),
                document=result.get('document'),
                photo=result.get('photo'),
                sticker=result.get('sticker'),
                video=result.get('video'),
                contact=result.get('contact'),
                location=result.get('location'),
                new_chat_participant=result.get('new_chat_participant'),
                left_chat_participant=result.get('left_chat_participant'),
                new_chat_title=result.get('new_chat_title'),
                new_chat_photo=result.get('new_chat_photo'),
                delete_chat_photo=result.get('delete_chat_photo'),
                group_chat_created=result.get('group_chat_created')
        )


class sendPhotoRequest(TelegramBotRPCRequest):
    def __init__(self, token, chat_id, photo, caption, reply_to_message_id, reply_markup,
                 callback=None, request_method=None):

        params = self.cleanup_params(token=token, chat_id=chat_id, photo=photo, caption=caption,
                                     reply_to_message_id=reply_to_message_id, reply_markup=reply_markup)

        try:
            params['photo'] = int(photo)
        except ValueError:
            # we don't have a photo_id, send new file
            files = {'photo': (photo, open(photo, 'rb'), 'image/jpeg')}

        print('sendPhotoRequest', params)

        super().__init__('sendPhoto', token=token, params=params, callback=callback, files=files, request_method=request_method)

    def _call_result(self, api_response):
        result = api_response['result']
        return Message(
                message_id=result.get('message_id'),
                sender=result.get('from'),
                date=result.get('date'),
                chat=result.get('chat'),
                forward_from=result.get('forward_from'),
                forward_date=result.get('forward_date'),
                reply_to_message=result.get('reply_to_message'),
                text=result.get('text'),
                audio=result.get('audio'),
                document=result.get('document'),
                photo=result.get('photo'),
                sticker=result.get('sticker'),
                video=result.get('video'),
                contact=result.get('contact'),
                location=result.get('location'),
                new_chat_participant=result.get('new_chat_participant'),
                left_chat_participant=result.get('left_chat_participant'),
                new_chat_title=result.get('new_chat_title'),
                new_chat_photo=result.get('new_chat_photo'),
                delete_chat_photo=result.get('delete_chat_photo'),
                group_chat_created=result.get('group_chat_created')
            )

class TelegramBotRPC:
    @staticmethod
    def get_me(token, callback=None, request_method :RequestMethod=RequestMethod.GET):
        return getMeRequest(token, callback, request_method).run()

    @staticmethod
    def send_message(token, chat_id :int, text :str, disable_web_page_preview :bool=None, 
                     reply_to_message_id :int=None, reply_markup :ReplyMarkup=None, 
                     callback=None, request_method :RequestMethod=RequestMethod.GET):

        return sendMessageRequest(token, chat_id, text, disable_web_page_preview, reply_to_message_id, reply_markup,
                                  callback, request_method).run()

    @staticmethod
    def send_photo(token, chat_id :int, photo :str, caption :str=None, reply_to_message_id :int=None,
                   reply_markup :ReplyMarkup=None, callback=None, request_method :RequestMethod=RequestMethod.POST):

        return sendPhotoRequest(token, chat_id, photo, caption, reply_to_message_id, reply_markup,
                                  callback, request_method).run()



def print_result(result):
    print(result)

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read("test.conf")
    token = config['Test']['token']
    test_chat_id = config['Test']['chat_id']

    TelegramBotRPC.get_me(token, callback=print_result)
    TelegramBotRPC.send_message(token, test_chat_id, 'testing', callback=print_result)
    TelegramBotRPC.send_photo(token, test_chat_id, 'test.jpg', callback=print_result)
