from distutils.core import setup

from subprocess import Popen, PIPE

short_rev = None
long_rev = None

with Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=PIPE) as f:
    short_rev = f.stdout.read().decode().strip()

with Popen(['git', 'rev-parse', 'HEAD'], stdout=PIPE) as f:
    long_rev = f.stdout.read().decode().strip()

if short_rev is None:
  raise Exception('Unable to determine short revision')

if long_rev is None:
  raise Exception('Unable to determine long revision')

version = '0.9.{short_rev}'.format(short_rev=short_rev)
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
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3.4',
  ]
)
