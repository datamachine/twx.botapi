import sys

"""
Extend the twx namespace
"""
if sys.version_info[0] == 3 and sys.version_info[1] >= 2:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
