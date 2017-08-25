# Development Environment
## VirtualEnv
### Install
https://virtualenv.pypa.io/en/stable/installation/
```
[sudo] pip install virtualenv
```
## Tox
### Install
```
$ sudo pip install tox
$ sudo pip install tox -U
$ tox --version
2.7.0 imported from /usr/local/lib/python2.7/dist-packages/tox/__init__.pyc
$ which tox
/usr/local/bin/tox
```

## flake8 - lint
### Install
http://flake8.pycqa.org/en/latest/
```
$ sudo python -m pip install flake8
$ sudo pip install flake8
$ flake8 --version
3.4.1 (mccabe: 0.6.1, pycodestyle: 2.3.1, pyflakes: 1.5.0) CPython 2.7.12 on Linux
$ flake8  # checks all the files recursively inside this directory
```
### flake8 with tox
```
```
### Ignore Errors
https://pypi.python.org/pypi/flake8
* per line
   * xxxx xxxx xxx # noqa: E234
* per file
   * ```# flake8: noqa```
