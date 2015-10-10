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

Voice
^^^^^

.. autoclass:: Voice

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

Request Objects
---------------

.. autoclass:: RequestMethod

.. autoclass:: TelegramBotRPCRequest

Telegram Bot API Methods
------------------------

get_me
^^^^^^

.. autofunction:: get_me(*, request_args=None, **kwargs)

send_message
^^^^^^^^^^^^

.. autofunction:: send_message(chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup, *, request_args=None, **kwargs)

forward_message
^^^^^^^^^^^^^^^

.. autofunction:: forward_message(chat_id, from_chat_id, message_id, *, request_args=None, **kwargs)

send_photo
^^^^^^^^^^

.. autofunction:: send_photo(chat_id, photo, caption=None, reply_to_message_id=None, reply_markup, *, request_args=None, **kwargs)

send_audio
^^^^^^^^^^

.. autofunction:: send_audio(chat_id, audio, duration=None, performer=None, title=None, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_document
^^^^^^^^^^^^^

.. autofunction:: send_document(chat_id, document, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_sticker
^^^^^^^^^^^^

.. autofunction:: send_sticker(chat_id, sticker, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_video
^^^^^^^^^^

.. autofunction:: send_video(chat_id, video, duration=None, caption=None, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_voice
^^^^^^^^^^

.. autofunction:: send_voice(chat_id, voice, duration=None, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_location
^^^^^^^^^^^^^

.. autofunction:: send_location(chat_id, latitude, longitude, reply_to_message_id=None, reply_markup=None, *, request_args=None, **kwargs)

send_chat_action
^^^^^^^^^^^^^^^^

.. autofunction:: send_chat_action(chat_id, action, *, request_args=None, **kwargs)

get_user_profile_photos
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_user_profile_photos(user_id, offset=None, limit=None, *, request_args=None, **kwargs)

get_updates
^^^^^^^^^^^

.. autofunction:: get_updates(offset=None, limit=None, timeout=None, *, request_args, **kwargs)

set_webhook
^^^^^^^^^^^

.. autofunction:: set_webhook(url=None, *, request_args=None, **kwargs)
