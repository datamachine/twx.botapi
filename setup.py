from setuptools import setup
import sys

__version__ = '1.0.2'

github_tag = __version__
if 'dev' in __version__:
    github_tag = 'master'

download_url = 'https://github.com/datamachine/twx.botapi/archive/{}.zip'
download_url = download_url.format(github_tag)

print(download_url)

requirements = ['requests']

if sys.version_info < (3, 4, 0):
    requirements.append('enum34')

print(requirements)

setup(name='twx.botapi',
      packages=['twx', 'twx.botapi'],
      version=__version__,
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
          'Programming Language :: Python :: 3.5',
          'Topic :: Communications :: Chat',
          'Topic :: Communications :: File Sharing',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ])
