| WARNING: This project is effectively retired, and won't be seeing any dev or support. There may be random commits in the future as we use it for side projects, but it's basically dead. There's plenty of other well maintained and feature rich (or feature lean) python TG libraries so you shouldn't have a problem finding another. Thanks for all the support and use in the past few years! |
| --- |




twx.botapi
==========

**twx.botapi: Unofficial Telegram Bot API Library and Client**

  -|-   
--:|:--
contributions | Please join https://github.com/datamachine/twx.botapi
issues | Please use https://github.com/datamachine/twx.botapi/issues
Python version supported | 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6

**twx.botapi** is a python interface for the Telegram bot API. It supports
making synchronous and asynchronous calls and converts the response into a
usable native python object.

Support for the MTProto API is in the works, but considered pre-alpha right now.

Support
-------

You can join our support chat at: https://telegram.me/twxapi

Install
-------

For stable:

``pip install twx.botapi``

For dev:

``pip install -i https://testpypi.python.org/pypi twx.botapi``

Documentation
-------------

Documentation can be found at http://pythonhosted.org/twx.botapi/

Quick Start
-----------

```python
from twx.botapi import TelegramBot, ReplyKeyboardMarkup

"""
Setup the bot
"""

bot = TelegramBot('<API TOKEN>')
bot.update_bot_info().wait()
print(bot.username)

"""
Send a message to a user
"""
user_id = int(<someuserid>)

result = bot.send_message(user_id, 'test message body').wait()
print(result)

"""
Get updates sent to the bot
"""
updates = bot.get_updates().wait()
for update in updates:
    print(update)

"""
Use a custom keyboard
"""
keyboard = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
            ['0']
]
reply_markup = ReplyKeyboardMarkup.create(keyboard)

bot.send_message(user_id, 'please enter a number', reply_markup=reply_markup).wait()
```
