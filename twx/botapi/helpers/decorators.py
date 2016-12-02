from enum import Enum
from functools import wraps

class Permissions(Enum):
    ADMIN = 1
    EVERYONE = 2

class Scopes(Enum):
    GROUP = 1
    PRIVATE = 2
    CHANNEL = 3

class Command:
    _registry = dict()

    def __init__(self, aliases, permission, scope):
        self.aliases = aliases
        self.permission = permission
        self.scope = scope

    def __call__(self, _command):
        @wraps(_command)
        def wrapper(*args, **kwds):
            return _command(*args, **kwds)
        return wrapper

