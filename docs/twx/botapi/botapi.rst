:mod:`twx.botapi` --- Unofficial Telegram Bot API Client
========================================================

.. automodule:: twx.botapi

.. py:currentmodule:: twx.botapi

Index
-----

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

Telegram Bot API Methods
------------------------

.. autofunction:: get_me(*, request_args=None, **kwargs)

.. autofunction:: send_message(chat_id: int, text: str, disable_web_page_preview: bool=None, reply_to_message_id: int=None, reply_markup: ReplyMarkup=None, *, request_args=None, **kwargs)