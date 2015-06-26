from distutils.core import setup

from subprocess import Popen, PIPE

revlist_count = None
long_rev = None

VERSION_MAJOR=1
VERSION_MINOR=0
VERSION_BETA=1

with Popen(['git', 'rev-list', 'HEAD', '--count'], stdout=PIPE) as f:
    revlist_count = f.stdout.read().decode().strip()

with Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE) as f:
    long_rev = f.stdout.read().decode().strip()

if revlist_count is None:
  raise Exception('Unable to determine short revision')

if long_rev is None:
  raise Exception('Unable to determine long revision')

import sys

version = '{}.{}'.format(VERSION_MAJOR, VERSION_MINOR)
if VERSION_BETA is not None:
  version = '{}b{}'.format(version, VERSION_BETA)
if 'pypitest' in sys.argv:
  version = '{}.dev{}'.format(version, revlist_count)

download_url = 'https://github.com/datamachine/twx/archive/{long_rev}.tar.gz'.format(long_rev=long_rev)

setup(
    name = 'twx',
    packages = ['twx'],
    version = version,
    description = 'Unofficial Telegram Bot API Client',
    author = 'Vince Castellano, Phillip Lopo',
    author_email = 'surye80@gmail.com, philliplopo@gmail.com',
    url = 'https://github.com/datamachine/twx', 
    download_url = download_url, 
    keywords = ['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc'],
    platforms = ['Linux', 'Unix', 'MacOsX', 'Windows'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 3.4',
  ]
)
