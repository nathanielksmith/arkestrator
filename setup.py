from distutils.core import setup

setup(name="mdc3",
    version="0.0.1",
    description="An Internet Message Board",
    author="Rev. Johnny Healey",
    author_email="rev.null@gmail.com",
    packages=[
        'mdc3',
        'mdc3.board',
        'mdc3.gallery',
        'mdc3.invites',
        'mdc3.profiles',
        'mdc3.shenanigans',
        'mdc3.tags',
        'mdc3.themes'
    ],
    package_data={
        'mdc3':['media/*/*','templates/*'],
        'mdc3.board':['templates/*']
    },
    install_requires=[
      'Django == 1.4.10',
      'South == 0.7.3',
      'python-memcached == 1.48',
      'ply == 3.4',
      'pytz',
      #'git+git://github.com/adreyer/BBKing.git#egg=bbking',
      'django-haystack == 1.2.7',
      'simplejson == 2.3.0',
      'pysolr == 2.1.0-beta',
      'multiprocessing == 2.6.2.1',
      'BeautifulSoup == 3.2.0',
      'unittest2 == 0.5.1',
      'mock == 0.7.2',
      'django-oembed == 0.1.3',
      'django-debug-toolbar == 0.11.0',
      ],
    )
