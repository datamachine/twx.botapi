from setuptools import setup
from subprocess import Popen, PIPE
import sys

revision = None

# must match PEP 440
_MAJOR_VERSION         = 1
_MINOR_VERSION         = 0
_MICRO_VERSION         = None
_PRE_RELEASE_TYPE      = 'rc'   # a | b | rc
_PRE_RELEASE_VERSION   = 1
_DEV_RELEASE_VERSION   = None

version = '{}.{}'.format(_MAJOR_VERSION, _MINOR_VERSION)
revision = None

if _MICRO_VERSION is not None:
    version += '.{}'.format(_MICRO_VERSION)

if _PRE_RELEASE_TYPE is not None and _PRE_RELEASE_VERSION is not None:
    version += '{}{}'.format(_PRE_RELEASE_TYPE, _PRE_RELEASE_VERSION)

if _DEV_RELEASE_VERSION is not None:
    version += '.dev{}'.format(_DEV_RELEASE_VERSION)
    revision = 'master'
else:
    revision = version

download_url = 'https://github.com/datamachine/twx.botapi/archive/{}.tar.gz'.format(revision)

print(version)
print(download_url)

requirements = ['requests']

if sys.version_info.major < 3 or sys.version_info.minor < 4:
  requirements.append('enum34')

print(requirements)

setup(
    name = 'twx.botapi',
    packages = ['twx', 'twx.botapi'],
    version = version,
    description = 'Unofficial Telegram Bot API Client',
    long_description = open("README.rst").read(),
    author = 'Vince Castellano, Phillip Lopo',
    author_email = 'surye80@gmail.com, philliplopo@gmail.com',
    keywords = ['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc'],
    url = 'https://github.com/datamachine/twx', 
    download_url = download_url, 
    install_requires=requirements,
    platforms = ['Linux', 'Unix', 'MacOsX', 'Windows'],
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3.0',
      'Programming Language :: Python :: 3.1',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Topic :: Communications :: Chat',
      'Topic :: Communications :: File Sharing'
      ]
)
