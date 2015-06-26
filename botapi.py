from requests import Request, Session
from collections import namedtuple
from enum import Enum
from functools import partial
from abc import ABCMeta
from threading import Thread

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

        print(result)

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

    def __init__(self, api_method: str, *, token, params: dict=None, on_result=None, callback=None, on_error=None, files=None, request_method=RequestMethod.POST):
        """
        :param api_method: The API method to call. See https://core.telegram.org/bots/api#available-methods
        :param token: The API token generated following the instructions at https://core.telegram.org/bots#botfather
        :param params: The api method parameters.

        :type api_method: str
        :type token: str
        :type params: dict
        """

        self.api_method = api_method
        self.token = token
        self.params = params
        self.on_result = on_result
        self.callback = callback
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
        api_response = resp.json()

        if api_response.get('ok'):
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
        self.thread.start()

        return self

    def join(self, timeout=None):
        self.thread.join(timeout)
        return self.result

def _clean_params(**params):
    return {name: val for name, val in params.items() if val is not None}

def _merge_dict(request_args, kwargs):
    result = request_args.copy() if request_args is not None else {}
    if kwargs is not None:
        result.update(kwargs)
    return result

def get_me(*, request_args=None, **kwargs):
    """
    A simple method for testing your bot's auth token. Requires no parameters. 
    Returns basic information about the bot in form of a User object.

    :param request_args: Args passed down to TelegramBotRPCRequest

    :returns: Returns basic information about the bot in form of a User object.
    :rtype: User
    """

    return TelegramBotRPCRequest('getMe', on_result=User.from_result, **(_merge_dict(request_args, kwargs))).run()

def send_message(chat_id: int, text: str, 
                 disable_web_page_preview: bool=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, 
                 *, request_args=None, **kwargs):
    """
    Use this method to send text messages. 

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param text: Text of the message to be sent
    :param disable_web_page_preview: Disables link previews for links in this message
    :param reply_to_message_id: If the message is a reply, ID of the original message
    :param reply_markup: Additional interface options. A JSON-serialized object for a 
                         custom reply keyboard, instructions to hide keyboard or to 
                         force a reply from the user.
    :param request_args: Args passed down to TelegramBotRPCRequest

    :type chat_id: int
    :type text: str
    :type disable_web_page_preview: bool
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """    
    params = _clean_params(
        chat_id=chat_id, 
        text=text, 
        disable_web_page_preview=disable_web_page_preview,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
        )

    return TelegramBotRPCRequest('sendMessage', params=params, on_result=Message.from_result,
                                 **(_merge_dict(request_args, kwargs))).run()

def forward_message(chat_id, from_chat_id, message_id,
                    *, request_args=None, **kwargs):
    """
    Use this method to forward messages of any kind. 

    :param chat_id: Unique identifier for the message recipient — User or GroupChat id
    :param from_chat_id: Unique identifier for the chat where the original message was sent — User or GroupChat id
    :param message_id: Unique message identifier
    :param request_args: Args passed down to TelegramBotRPCRequest

    :type chat_id: int
    :type from_chat_id: int
    :type message_id: int

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """

    params = dict(
        chat_id=chat_id, 
        from_chat_id=from_chat_id, 
        message_id=message_id
        )

    request_args = _merge_dict(request_args, kwargs)

    return TelegramBotRPCRequest('forwardMessage', params=params, on_result=Message.from_result, **request_args).run()

def send_photo(chat_id: int,  photo: InputFile, 
               caption: str=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None,
               *, request_args=None, **kwargs):
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
    :param request_args: Args passed down to TelegramBotRPCRequest

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

    params = _clean_params(
        chat_id=chat_id,
        photo=photo,
        caption=caption,
        reply_to_message_id=reply_to_message_id,
        reply_markup=reply_markup
        )

    return TelegramBotRPCRequest('sendPhoto', params=params, files=files, on_result=Message.from_result,
                                 **(_merge_dict(request_args, kwargs))).run()

def send_audio(chat_id: int, audio: InputFile, reply_to_message_id: int=None,
               reply_markup: ReplyKeyboardMarkup=None,
               *, request_args=None, **kwargs):
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
    :param request_args: Args passed down to TelegramBotRPCRequest

    :type chat_id: int
    :type audio: InputFile or str
    :type reply_to_message_id: int
    :type reply_markup: ReplyKeyboardMarkup or ReplyKeyboardHide or ForceReply

    :returns: On success, the sent Message is returned.
    :rtype: Message
    """
    #TODO: implement
    raise NotImplemented

def send_document(chat_id, document, reply_to_message_id=None, reply_markup=None,
                  *, request_args=None, **kwargs):
    """
    :param chat_id: 
    :param document: 
    :param reply_to_message_id: 
    :param reply_markup: 
    :param request_args: Args passed down to TelegramBotRPCRequest

    :type chat_id: 
    :type document: 
    :type reply_to_message_id: 
    :type reply_markup: 

    :returns:
    :rtype:
    """
    # TODO: Implement
    raise NotImplemented

def send_sticker(chat_id, sticker, reply_to_message_id, reply_markup=None,
                 *, request_args=None, **kwargs):
    """
    :param token: 
    :param chat_id: 
    :param sticker: 
    :param reply_to_message_id: 
    :param reply_markup: 
    :param request_args: Args passed down to TelegramBotRPCRequest

    :type token: 
    :type chat_id: 
    :type sticker: 
    :type reply_to_message_id: 
    :type reply_markup: 

    :returns:
    :rtype:
    """
    #TODO: implement
    raise NotImplemented

def send_video(request_args, **kwargs):
    """
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest
    """
    #TODO: implement
    raise NotImplemented

def send_location(request_args, **kwargs):
    """
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest
    """
    #TODO: implement
    raise NotImplemented

def send_chat_action(request_args, **kwargs):
    """
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest
    """
    #TODO: implement
    raise NotImplemented

def _process_get_user_profile_photos_result(result):
    if result is None:
        return None

    photo_lists = []
    for photo_list in result.get('photos'):
        photo_lists.append([PhotoSize.from_result(photo) for photo in photo_list])

    return photo_lists


def get_user_profile_photos(user_id: int, offset: int=None, limit: int=None, *, request_args: dict=None, **kwargs):
    """
    Use this method to get a list of profile pictures for a user. Returns a UserProfilePhotos object.

    :param user_id: Unique identifier of the target user
    :param offset: Sequential number of the first photo to be returned. By default, all photos are returned.
    :param limit: Limits the number of photos to be retrieved. Values between 1—100 are accepted. Defaults to 100.
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest

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

    # merge bot args with user overrides
    request_args = _merge_dict(request_args, kwargs)

    return TelegramBotRPCRequest('getUserProfilePhotos', params=params, on_result=_process_get_user_profile_photos_result, **request_args).run()

def get_updates(request_args, **kwargs):
    """
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest
    """
    #TODO: implement
    raise NotImplemented

def set_webhook(request_args, **kwargs):
    """
    :param request_args, **kwargs: Args passed down to the TelegramBotRPCRequest
    """
    #TODO: implement
    raise NotImplemented


class TelegramBot:

    def __init__(self, token, request_method: RequestMethod=RequestMethod.POST):
        self._bot_user = User(None, None, None, None)

        self.request_args = dict(
            token=token,
            request_method=request_method
        )

        self.get_me = partial(get_me, request_args=self.request_args)
        self.send_message = partial(send_message, request_args=self.request_args)
        self.forward_message = partial(forward_message, request_args=self.request_args)
        self.send_photo = partial(send_photo, request_args=self.request_args)
        self.send_audio = partial(send_audio, request_args=self.request_args)
        self.send_document = partial(send_document, request_args=self.request_args)
        self.send_sticker = partial(send_sticker, request_args=self.request_args)
        self.send_video = partial(send_video, request_args=self.request_args)
        self.send_location = partial(send_location, request_args=self.request_args)
        self.send_chat_action = partial(send_chat_action, request_args=self.request_args)
        self.get_user_profile_photos = partial(get_user_profile_photos, request_args=self.request_args)
        self.get_updates = partial(get_updates, request_args=self.request_args)
        self.set_webhook = partial(set_webhook, request_args=self.request_args)
        self.update_bot_info = partial(get_me, request_args=self.request_args, callback=self._update_bot_info)

    def __str__(self):
        return self.token

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
    def request_method(self, val: RequestMethod):
        self.request_args['request_method'] = val

    @property
    def username(self):
        return self._bot_user.username    

    def _update_bot_info(self, bot_user):
        self._bot_user = bot_user

def print_result(result):
    #print(result)
    pass

def print_error(result):
    print(result)

if __name__ == '__main__':
    import configparser
    config = configparser.ConfigParser()
    config.read("test.conf")
    test_token = config['Test']['token']
    test_chat_id = config['Test']['chat_id']

    photo = InputFile('photo', InputFileInfo('test.jpg', open('test.jpg', 'rb'), 'image/jpeg'))

    bot = TelegramBot(test_token)
    bot.get_me(callback=print_result)
    bot.update_bot_info()
    
    # 97704886

    #msg = bot.send_message(test_chat_id, 'testing1', callback=print_result).join()

    #result = bot.forward_message(97704886, 96846582, msg.message_id).join()

    result = bot.get_user_profile_photos(97704886, on_error=print_error, request_method=RequestMethod.GET).join()

    print(result)

    #bot.forward_message(test_chat_id, 'testing1', callback=print_result)

    #send_message(test_chat_id, 'testing', token=test_token, callback=print_result)
    #bot.send_photo(test_chat_id, photo, callback=print_result)

    #TelegramBotRPC.send_photo(test_token, test_chat_id, 'AgADAwADqacxGwpPWQaFLwABSzSkg2Bq-usqAASiGyniRUnk5BdEAAIC',
    #                         callback=print_result, on_error=print_error)
