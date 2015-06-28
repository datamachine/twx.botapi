:mod:`twx.botapi` --- Unofficial Telegram Bot API Client
========================================================

.. automodule:: twx.botapi

.. py:currentmodule:: twx.botapi


Quick Jump
----------

Telegram Bot API Types
^^^^^^^^^^^^^^^^^^^^^^

* :class:`User`
* :class:`GroupChat`
* :class:`Message`
* :class:`PhotoSize`
* :class:`Audio`
* :class:`Document`
* :class:`Sticker`
* :class:`Video`
* :class:`Contact`
* :class:`Location`
* :class:`Update`
* :class:`InputFile`
* :class:`UserProfilePhotos`
* :class:`ReplyKeyboardMarkup`
* :class:`ReplyKeyboardHide`
* :class:`ForceReply`

Telegram Bot API Methods
^^^^^^^^^^^^^^^^^^^^^^^^

* :func:`get_me`
* :func:`send_message`
* :func:`forward_message`
* :func:`send_photo`
* :func:`send_audio`
* :func:`send_document`
* :func:`send_sticker`
* :func:`send_video`
* :func:`send_location`
* :func:`send_chat_action`
* :func:`getUser_profile_photos`
* :func:`get_updates`
* :func:`set_webhook`


Telegram Bot API Types
----------------------

.. autoclass:: User
.. autoclass:: GroupChat
.. autoclass:: Message
.. autoclass:: PhotoSize
.. autoclass:: Audio
.. autoclass:: Document
.. autoclass:: Sticker
.. autoclass:: Video
.. autoclass:: Contact
.. autoclass:: Location
.. autoclass:: Update
.. autoclass:: InputFile
.. autoclass:: UserProfilePhotos
.. autoclass:: ReplyKeyboardMarkup
.. autoclass:: ReplyKeyboardHide
.. autoclass:: ForceReply

Additional Types
----------------

.. autoclass:: Error

Telegram Bot API Methods
------------------------

.. autofunction:: get_me(*, request_args=None, **kwargs)
.. autofunction:: send_message(chat_id: int, text: str, disable_web_page_preview: bool=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, *, request_args=None, **kwargs)
.. autofunction:: forward_message(chat_id, from_chat_id, message_id, *, request_args=None, **kwargs)
.. autofunction:: send_photo(chat_id: int,  photo: InputFile, caption: str=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_audio(chat_id: int, audio: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_document(chat_id: int, document: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_sticker(chat_id: int, sticker: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_video(chat_id: int, video: InputFile, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_location(chat_id: int, latitude: float, longitude: float, reply_to_message_id: int=None, reply_markup: ReplyKeyboardMarkup=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: send_chat_action(chat_id: int, action: ChatAction, *, request_args=None, **kwargs) -> TelegramBotRPCRequest
.. autofunction:: get_user_profile_photos(user_id: int, offset: int=None, limit: int=None, *, request_args: dict=None, **kwargs)
.. autofunction:: get_updates(offset: int=None, limit: int=None, timeout: int=None, *, request_args, **kwargs)
.. autofunction:: set_webhook(url: str=None, *, request_args=None, **kwargs) -> TelegramBotRPCRequest