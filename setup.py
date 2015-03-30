from setuptools import setup, find_packages

setup(
  name = 'recast-helloworld-demo',
  version = '0.0.1',
  description = 'recast-helloworld-demo',
  url = '',
  author = 'Lukas Heinrich',
  author_email = 'lukas.heinrich@cern.ch',
  packages = find_packages(),
  include_package_data = True,
  install_requires = [
    'Flask',
    'celery',
    'requests',
    'recast-api',
    'yoda',
    'socket.io-python-emitter',
    'redis'
  ],
  dependency_links = [       'https://github.com/ziyasal/socket.io-python-emitter/tarball/master#egg=socket.io-python-emitter-0.1.3',
'https://github.com/recast-hep/recast-api/tarball/master#egg=recast-api-0.0.1'
  ]
)
