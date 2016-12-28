import twx.botapi
import re
import logging
from enum import Enum

class Scope(Enum):
    Group = 1
    PM = 2

class Permission(Enum):
    User = 1
    Admin = 2


class UpdateLoop:
    """
    Super Simple loop and handler helper. Runs until exit.

    TODO: Implement decorators. Split loop from handler code.
    """

    def __init__(self, bot, handler, prefix="/"):
        self.bot = bot
        self.handler = handler
        self.prefix = prefix
        self.update_offset = 0
        self.logger = logging.getLogger("twx.botapi.UpdateLoop")
        self.command_registry = dict()
        self.reply_registry = dict()

    def register_command(self, name, function, permission=Permission.User, scope=Scope.Group):
        self.command_registry[name.lower()] = {
            'func': function,
            'permission': permission,
            'scope': scope
        }
    def register_reply_watch(self, message_id, function):
        self.reply_registry[message_id] = function

    def run(self):
        while True:
            twx.botapi.get_updates(offset=self.update_offset, timeout=300,
                                   on_success=self.new_updates, **self.bot.request_args).run().wait()

    def new_updates(self, updates):
        for update in updates:
            self.update_offset = update.update_id + 1
            self.process_update(update)

    def process_update(self, update):
        msg = update.message
        if msg.reply_to_message and msg.reply_to_message.message_id in self.reply_registry:
            self.reply_registry[msg.reply_to_message.message_id](msg, None)
            self.reply_registry.pop(msg.reply_to_message.message_id)
        else:
            member = self.bot.get_chat_member(chat_id=msg.chat.id, user_id=msg.sender.id).join().result
            if not msg or not msg.text:
                return  # Ignore any non-text updates

            match = re.match(r"^(?:/|@)(?P<command>[^\s@]+)@?(?P<bot_name>\S+)?\s?(?P<arguments>.*)$", msg.text, re.IGNORECASE)

            if match:
                command = match.group('command').lower()
                if self.command_registry[command]["permission"] == Permission.Admin and member.status not in ["creator", "administrator"]:
                    self.bot.send_message(chat_id=msg.chat.id, text="Sorry, this command is only available to group admins.", reply_to_message_id=msg.message_id)

                else:
                    if match.group('bot_name') and match.group('bot_name').lower() != self.bot.username.lower():
                        self.logger.warning("Command received for another bot: {}".format(msg.text))

                    try:
                        self.command_registry[command]['func'](msg, match.group('arguments'))
                    except KeyError:
                        self.logger.debug("Unregistered command called: " + command)
            else:
                self.logger.warning("Got a message that doesn't match a command.")  # TODO: Support this warning optionally
