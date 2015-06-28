TWX: Unofficial Telegram Bot API Client
##########

:contributions: Please join https://github.com/datamachine/twx
:issues: Please use https://github.com/datamachine/twx/issues
:Python version supported: 3.4

**TWX** is a python interface for the Telegram bot API. It supports
making synchronous and asynchronous calls and converts the response
into a usable native python object.

Support for the MTProto API is in the works, but considered pre-alpha right now.

=======
Install
=======

For stable:

``pip install twx``

For dev:

``pip install -i https://testpypi.python.org/pypi twx``

===========
Quick Start
===========

Setup the bot
-------------

::
    
    from twx.botapi import TelegramBot
    
    bot = TelegramBot('<API TOKEN>')
    bot.update_bot_info().wait()

    print(bot.username)

Send a message
--------------

::
    
    result = bot.send_message(int('userid'), 'test message body').wait()
    print(result)

Get messages sent to the bot
----------------------------

::

    updates = bot.get_updates().wait()
    for update in updates:
        print(update)

Use a custom keyboard

::

    keyboard = [
        ['7', '8', '9'],
        ['4', '5', '6'],
        ['1', '2', '3'],
             ['0']
    ]

    reply_markup = ReplyKeyboardMarkup.create(keyboard)

    bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()

