:mod:`twx.botapi` --- Unofficial Telegram Bot API Client
========================================================

.. automodule:: twx.botapi

.. py:currentmodule:: twx.botapi


Primary Bot Class
-----------------
.. autoclass:: TelegramBot

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

VideoNote
^^^^^

.. autoclass:: VideoNote

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

InputMedia
^^^^^^^^^^^^^

.. autoclass:: InputMedia

InputMediaPhoto
^^^^^^^^^^^^^

.. autoclass:: InputMediaPhoto

InputMediaVideo
^^^^^^^^^^^^^

.. autoclass:: InputMediaVideo

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

Game
^^^^

.. autoclass:: Game

GameHighScore
^^^^

.. autoclass:: GameHighScore

Animation
^^^^^^^^^

.. autoclass:: Animation

WebhookInfo
^^^^^^^^^^^

.. autoclass:: WebhookInfo

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

export_chat_invite_link
^^^^^^^^^^^

.. autofunction:: export_chat_invite_link

set_chat_photo
^^^^^^^^^^^

.. autofunction:: set_chat_photo

delete_chat_photo
^^^^^^^^^^^

.. autofunction:: delete_chat_photo

set_chat_title
^^^^^^^^^^^

.. autofunction:: set_chat_title

set_chat_description
^^^^^^^^^^^

.. autofunction:: set_chat_description

pin_chat_message
^^^^^^^^^^^

.. autofunction:: pin_chat_message

unpin_chat_message
^^^^^^^^^^^

.. autofunction:: unpin_chat_message

get_me
^^^^^^^^^^^

.. autofunction:: get_me

send_message
^^^^^^^^^^^

.. autofunction:: send_message

forward_message
^^^^^^^^^^^

.. autofunction:: forward_message

send_photo
^^^^^^^^^^^

.. autofunction:: send_photo

send_audio
^^^^^^^^^^^

.. autofunction:: send_audio

send_document
^^^^^^^^^^^

.. autofunction:: send_document

send_sticker
^^^^^^^^^^^

.. autofunction:: send_sticker

send_video
^^^^^^^^^^^

.. autofunction:: send_video

send_video_note
^^^^^^^^^^^

.. autofunction:: send_video_note

send_voice
^^^^^^^^^^^

.. autofunction:: send_voice

send_media_group
^^^^^^^^^^^

.. autofunction:: send_media_group

send_location
^^^^^^^^^^^

.. autofunction:: send_location

edit_message_live_location
^^^^^^^^^^^

.. autofunction:: edit_message_live_location

stop_message_live_location
^^^^^^^^^^^

.. autofunction:: stop_message_live_location

send_venue
^^^^^^^^^^^

.. autofunction:: send_venue

send_contact
^^^^^^^^^^^

.. autofunction:: send_contact

send_chat_action
^^^^^^^^^^^

.. autofunction:: send_chat_action

kick_chat_member
^^^^^^^^^^^

.. autofunction:: kick_chat_member

restrict_chat_member
^^^^^^^^^^^

.. autofunction:: restrict_chat_member

promote_chat_member
^^^^^^^^^^^

.. autofunction:: promote_chat_member

unban_chat_member
^^^^^^^^^^^

.. autofunction:: unban_chat_member

get_chat
^^^^^^^^^^^

.. autofunction:: get_chat

leave_chat
^^^^^^^^^^^

.. autofunction:: leave_chat

get_chat_administrators
^^^^^^^^^^^

.. autofunction:: get_chat_administrators

get_chat_member
^^^^^^^^^^^

.. autofunction:: get_chat_member

get_chat_members_count
^^^^^^^^^^^

.. autofunction:: get_chat_members_count

set_chat_sticker_set
^^^^^^^^^^^

.. autofunction:: set_chat_sticker_set

delete_chat_sticker_set
^^^^^^^^^^^

.. autofunction:: delete_chat_sticker_set

answer_callback_query
^^^^^^^^^^^

.. autofunction:: answer_callback_query

delete_message
^^^^^^^^^^^

.. autofunction:: delete_message

edit_message_text
^^^^^^^^^^^

.. autofunction:: edit_message_text

edit_message_caption
^^^^^^^^^^^

.. autofunction:: edit_message_caption

edit_message_reply_markup
^^^^^^^^^^^

.. autofunction:: edit_message_reply_markup

answer_inline_query
^^^^^^^^^^^

.. autofunction:: answer_inline_query

get_user_profile_photos
^^^^^^^^^^^

.. autofunction:: get_user_profile_photos

get_file
^^^^^^^^^^^

.. autofunction:: get_file

send_game
^^^^^^^^^^^

.. autofunction:: send_game

set_game_score
^^^^^^^^^^^

.. autofunction:: set_game_score

get_game_high_scores
^^^^^^^^^^^

.. autofunction:: get_game_high_scores

get_updates
^^^^^^^^^^^

.. autofunction:: get_updates

set_webhook
^^^^^^^^^^^

.. autofunction:: set_webhook

get_webhook_info
^^^^^^^^^^^

.. autofunction:: get_webhook_info

download_file
^^^^^^^^^^^

.. autofunction:: download_file

