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

=====
Usage
=====

::
    
    from twx.botapi import TelegramBot
    
    bot = TelegramBot('<API TOKEN>')
    
    request = bot.get_me()
    result = request.wait()
    print(result)
    
    result = bot.send_message(int('userid'), 'test message body').wait()
    print(result)

    updates = bot.get_updates().wait()
    for update in updates:
        print("update_id: {}".format(update.update_id))
