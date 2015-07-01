from setuptools import setup
import sys

import twx.botapi

github_tag = twx.botapi.__version__
if 'dev' in twx.botapi.__version__:
    github_tag = 'master'

download_url = 'https://github.com/datamachine/twx.botapi/archive/{}.tar.gz'
download_url = download_url.format(github_tag)

print(download_url)

requirements = ['requests']

if sys.version_info.major < 3 or sys.version_info.minor < 4:
    requirements.append('enum34')

print(requirements)

setup(name='twx.botapi',
      packages=['twx', 'twx.botapi'],
      version=twx.botapi.__version__,
      description='Unofficial Telegram Bot API Library and Client',
      long_description=open("README.rst").read(),
      author='Vince Castellano, Phillip Lopo',
      author_email='surye80@gmail.com, philliplopo@gmail.com',
      keywords=['datamachine', 'telex', 'telegram', 'bot', 'api', 'rpc', 'twx', 'chat'],
      url='https://github.com/datamachine/twx.botapi',
      download_url=download_url,
      install_requires=requirements,
      platforms=['Linux', 'FreeBSD', 'BSD', 'Unix', 'Mac', 'OS X', 'Windows'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
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
          'Topic :: Communications :: File Sharing',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
