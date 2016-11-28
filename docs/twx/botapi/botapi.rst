:mod:`twx.botapi` --- Unofficial Telegram Bot API Client
========================================================

.. automodule:: twx.botapi

.. py:currentmodule:: twx.botapi

Telegram Bot API Types
----------------------

User
^^^^

.. autoclass:: User

ChatMember
^^^^^^^^^^

.. autoclass:: ChatMember

Chat
^^^^

.. autoclass:: Chat

Message
^^^^^^^

.. autoclass:: Message


MessageEntity
^^^^^^^^^^^^^

.. autoclass:: MessageEntity

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

Venue
^^^^^

.. autoclass:: Venue

Update
^^^^^^

.. autoclass:: Update

InputFile
^^^^^^^^^

.. autoclass:: InputFile

InputFileInfo
^^^^^^^^^^^^^

.. autoclass:: InputFileInfo


UserProfilePhotos
^^^^^^^^^^^^^^^^^

.. autoclass:: UserProfilePhotos


File
^^^^

.. autoclass:: File


ReplyKeyboardMarkup
^^^^^^^^^^^^^^^^^^^

.. autoclass:: ReplyKeyboardMarkup

ReplyKeyboardHide
^^^^^^^^^^^^^^^^^

.. autoclass:: ReplyKeyboardHide

ForceReply
^^^^^^^^^^

.. autoclass:: ForceReply


KeyboardButton
^^^^^^^^^^^^^^

.. autoclass:: KeyboardButton


Inline Types
------------

InlineQuery
^^^^^^^^^^^

.. autoclass:: InlineQuery

ChosenInlineResult
^^^^^^^^^^^^^^^^^^

.. autoclass:: ChosenInlineResult

CallbackQuery
^^^^^^^^^^^^^

.. autoclass:: CallbackQuery

InlineKeyboardMarkup
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineKeyboardMarkup

InlineKeyboardButton
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineKeyboardButton


Inline Query Return Types
-------------------------

InlineQueryResultArticle
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultArticle


InlineQueryResultPhoto
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultPhoto


InlineQueryResultCachedPhoto
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultPhoto


InlineQueryResultGif
^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultGif


InlineQueryResultCachedGif
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedGif


InlineQueryResultMpeg4Gif
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultMpeg4Gif


InlineQueryResultCachedMpeg4Gif
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedMpeg4Gif


InlineQueryResultVideo
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultVideo


InlineQueryResultCachedVideo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedVideo


InlineQueryResultAudio
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultAudio


InlineQueryResultCachedAudio
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedAudio


InlineQueryResultVoice
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultVoice


InlineQueryResultCachedVoice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedVoice


InlineQueryResultDocument
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultDocument


InlineQueryResultCachedDocument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultCachedDocument


InlineQueryResultLocation
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultLocation


InlineQueryResultVenue
^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultVenue


InlineQueryResultContact
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultContact


InlineQueryResultContact
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InlineQueryResultContact


InputTextMessageContent
^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InputTextMessageContent


InputLocationMessageContent
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InputLocationMessageContent


InputVenueMessageContent
^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InputVenueMessageContent


InputContactMessageContent
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: InputContactMessageContent




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

send_venue
^^^^^^^^^^

.. autofunction:: send_venue(chat_id, latitude, longitude, title, address, foursquare_id=None, reply_to_message_id=None, reply_markup=None, disable_notification=False, **kwargs)

send_contact
^^^^^^^^^^^^

.. autofunction:: send_contact(chat_id, phone_number, first_name, last_name=None, reply_to_message_id=None, reply_markup=None, disable_notification=False, **kwargs)

send_chat_action
^^^^^^^^^^^^^^^^

.. autofunction:: send_chat_action(chat_id, action, *, request_args=None, **kwargs)

kick_chat_member
^^^^^^^^^^^^^^^^

.. autofunction:: kick_chat_member(chat_id, user_id, **kwargs)

unban_chat_member
^^^^^^^^^^^^^^^^^

.. autofunction:: unban_chat_member(chat_id, user_id, **kwargs)

get_chat
^^^^^^^^

.. autofunction:: get_chat(chat_id, **kwargs)

leave_chat
^^^^^^^^^^

.. autofunction:: leave_chat(chat_id, **kwargs)

get_chat_administrators
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_chat_administrators(chat_id, **kwargs)


get_chat_member
^^^^^^^^^^^^^^^

.. autofunction:: get_chat_member(chat_id, **kwargs)

get_chat_members_count
^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_chat_members_count(chat_id, **kwargs)

answer_callback_query
^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: answer_callback_query(callback_query_id, text=None, show_alert=None, **kwargs)

edit_message_text
^^^^^^^^^^^^^^^^^

.. autofunction:: edit_message_text(text, chat_id=None, message_id=None, inline_message_id=None, parse_mode=None, disable_web_page_preview=None, reply_markup=None, **kwargs)

edit_message_caption
^^^^^^^^^^^^^^^^^^^^

.. autofunction:: edit_message_caption(caption, chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, **kwargs)

edit_message_reply_markup
^^^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: edit_message_reply_markup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None, **kwargs)

answer_inline_query
^^^^^^^^^^^^^^^^^^^

.. autofunction:: answer_inline_query(inline_query_id, results, cache_time=None, is_personal=None, next_offset=None, switch_pm_text=None, switch_pm_parameter=None, **kwargs)

get_user_profile_photos
^^^^^^^^^^^^^^^^^^^^^^^

.. autofunction:: get_user_profile_photos(user_id, offset=None, limit=None, *, request_args=None, **kwargs)

get_file
^^^^^^^^

.. autofunction:: get_file(file_id, **kwargs)

download_file
^^^^^^^^^^^^^

.. autofunction:: download_file(file_path, out_file, **kwargs)

get_updates
^^^^^^^^^^^

.. autofunction:: get_updates(offset=None, limit=None, timeout=None, *, request_args, **kwargs)

set_webhook
^^^^^^^^^^^

.. autofunction:: set_webhook(url=None, *, request_args=None, **kwargs)
