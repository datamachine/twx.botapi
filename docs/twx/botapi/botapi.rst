:mod:`twx.botapi` --- Unofficial Telegram Bot API Client
========================================================

.. automodule:: twx.botapi

.. py:currentmodule:: twx.botapi

Telegram Bot API Types
----------------------

User
^^^^

.. autoclass:: User

GroupChat
^^^^^^^^^

.. autoclass:: GroupChat

Message
^^^^^^^

.. autoclass:: Message

PhotoSize
^^^^^^^^^

.. autoclass:: PhotoSize

Audio
^^^^^

.. autoclass:: Audio

Document
^^^^^^^^

.. autoclass:: Document

Sticker
^^^^^^^

.. autoclass:: Sticker

Video
^^^^^

.. autoclass:: Video

Contact
^^^^^^^

.. autoclass:: Contact

Location
^^^^^^^^

.. autoclass:: Location

Update
^^^^^^

.. autoclass:: Update

InputFile
^^^^^^^^^

.. autoclass:: InputFile

UserProfilePhotos
^^^^^^^^^^^^^^^^^

.. autoclass:: UserProfilePhotos

ReplyKeyboardMarkup
^^^^^^^^^^^^^^^^^^^

.. autoclass:: ReplyKeyboardMarkup

ReplyKeyboardHide
^^^^^^^^^^^^^^^^^

.. autoclass:: ReplyKeyboardHide

ForceReply
^^^^^^^^^^

.. autoclass:: ForceReply


Additional Types
----------------

Error
^^^^^

.. autoclass:: Error

Telegram Bot API Methods
------------------------

get_me
^^^^^^

.. autofunction:: get_me(*, request_args=None, **kwargs)

send_message
^^^^^^^^^^^^

.. autofunction:: send_message(chat_id: int, text: str, disable_web_page_preview: bool=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, *, request_args=None, **kwargs)

forward_message
^^^^^^^^^^^^^^^

.. autofunction:: forward_message(chat_id, from_chat_id, message_id, *, request_args=None, **kwargs)

send_photo
^^^^^^^^^^

.. autofunction:: send_photo(chat_id: int,  photo: InputFile, caption: str=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_audio
^^^^^^^^^^

.. autofunction:: send_audio(chat_id: int, audio: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_document
^^^^^^^^^^^^^

.. autofunction:: send_document(chat_id: int, document: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_sticker
^^^^^^^^^^^^

.. autofunction:: send_sticker(chat_id: int, sticker: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_video
^^^^^^^^^^

.. autofunction:: send_video(chat_id: int, video: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_location
^^^^^^^^^^^^^

.. autofunction:: send_location(chat_id: int, latitude: float, longitude: float, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

send_chat_action
^^^^^^^^^^^^^^^^

.. autofunction:: send_chat_action(chat_id: int, action: ChatAction, *, request_args=None, **kwargs) -> TelegramBotRPCRequest

get_user_profile_photos
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_user_profile_photos(user_id: int, offset: int=None, limit: int=None, *, request_args: dict=None, **kwargs)

get_updates
^^^^^^^^^^^

.. autofunction:: get_updates(offset: int=None, limit: int=None, timeout: int=None, *, request_args, **kwargs)

set_webhook
^^^^^^^^^^^

.. autofunction:: set_webhook(url: str=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
