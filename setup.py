from distutils.core import setup

from subprocess import Popen, PIPE

version = None
with Popen(['git', 'rev-parse', '--short', 'HEAD'], stdout=PIPE) as f:
    version = '1.0.{}'.format(f.stdout.read().decode().strip())

if version is None:
  raise Exception('Unable to determine version information')

setup(
    name = 'twx',
    packages = ['twx'], # this must be the same as the name above
    version = version,
    description = 'Unofficial Telegram Bot API Client',
    author = 'Vince Castellano, Phillip Lopo',
    author_email = 'surye80@gmail.com, philliplopo@gmail.com',
    url = 'https://github.com/datamachine/twx', # use the URL to the github repo
    download_url = 'https://github.com/datamachine/twx/archive/master.tar.gz', # I'll explain this in a second
    keywords = ['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc'], # arbitrary keywords
    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3.4',
  ]
)
