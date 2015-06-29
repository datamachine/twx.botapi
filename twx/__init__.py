import sys

"""
Only import twx modules on supported pytohn versions. Type hinting breaks testing 2.7 against twx.botapi
"""
if sys.version_info[0] == 3 and sys.version_info[1] >=4:
	from . twx import *