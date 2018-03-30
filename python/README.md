# Development Environment
## install pip
```
#ubuntu 16.04
sudo apt install python-pip
```
## pip with proxy
```
# it can also take environment varibles: http_proxy, https_proxy,
sudo pip --proxy http://xxxx:xxx install xxx
```
## VirtualEnv
* When behind a proxy, virtualenv can use environment variable http_proxy, https_proxy
### Install
https://virtualenv.pypa.io/en/stable/installation/
```
[sudo] pip install virtualenv
```
If you stil have this problem after installation:
```
Traceback (most recent call last):
  File "/usr/bin/virtualenv", line 7, in <module>
    from virtualenv import main
ImportError: No module named virtualen
```
And you also can find virtualenv.py file in /usr/lib/python2.7/site-packages/. Please check whether the permission of virutalenv.py is right, e.g. less /usr/lib/python2.7/site-packages/virtualenv.py. 

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
Good example can be found in flake8 project: https://github.com/PyCQA/flake8/blob/master/tox.ini

Simple Example
```
[tox]
envlist=py27,flake8

[flake8]
exclude=.tox
max-line-length=100

[testenv:py27]
deps=-rrequirements.txt
commands=py.test {posargs}

[testenv:flake8]
deps=
  flake8==3.4.1
commands=flake8
```
[tox] and [flake8] are special sections. 
* [tox] configures tox, where envlist says which type of environments to use. This is useful when we want to run the same tests for all the python versions, where each version is a kind of environment. And we can also configure how to run the each environment by other environment specific sections, and this is used by flake8, which is defined in [testenv:flake8]. This makes the environment for flake8 different from normal tests.
* [flake8] is for configuration of flake8. Only [testenv:py27] and [testenv:flake8]

Other sections are configurations for each specific environment, which that are actually executed. We can list all the environments by 
 ```
 tox --showconfig
 ```

### Ignore Errors
https://pypi.python.org/pypi/flake8
* per line
   * xxxx xxxx xxx # noqa: E234
* per file
   * ```# flake8: noqa```

# Import
## Local file import
* common.py
```python
def get_api_url(relative_path):
```
* list.py
```python
from common import get_api_url
```
