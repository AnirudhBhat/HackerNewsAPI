try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '2.1.4'

setup(
    name='hacker_news',
    version=version,
    packages=['hn'],
    install_requires=['requests'],
    author='Anirudh Bhat',
    author_email='abhat38@gmail.com',
    url='https://github.com/AnirudhBhat/HackerNewsAPI/',
    license='MIT License',
    description='Python wrapper for Hacker News API.',
    long_description='https://github.com/AnirudhBhat/HackerNewsAPI/',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)