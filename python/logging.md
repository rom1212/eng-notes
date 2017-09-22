# basicConfig
## set format
```
logging.basicConfig(filename=filename, level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s:%(lineno)d %(levelname)-8s %(message)s')
```
## debug process and thread
```
format='[process: %(process)d %(processName)s %(thread)d %(threadName)s]'
```

# multiple processes logging:
* TimedRotatingFileHandler:
  * multiple processes do NOT work correctly with it. Log will be lost during log rotation: http://thinlight.org/2011/08/10/python-logging-from-multiple-processes/
* gunicorn:
  * https://github.com/benoitc/gunicorn/issues/1272, How do gunicorn workers log correctly?
  * what if the log is rotated?
* multiple handlers writing to the same log file:
  * handlers open a file with O_APPEND, which is atomic: http://stackoverflow.com/questions/1154446/is-file-append-atomic-in-unix
* solution is to use WachedFileHandler
  * WachedFileHandler also makes it easier to do log rotation, because it doesn't need to use USR1 signal to know that the log is rotated.

# exc_info:
* "the values returned are (type, value, traceback)"
* example:
```
try:
                raise Exception('ming exception')
            except:
                print 'sys.exc_info()[0]:', sys.exc_info()[0]
                print 'sys.exc_info()[1]:', sys.exc_info()[1]
                print 'sys.exc_info()[2]:', sys.exc_info()[2]
output:
sys.exc_info()[0]: <type 'exceptions.Exception'>
sys.exc_info()[1]: ming exception
sys.exc_info()[2]: <traceback object at 0x7f285deecea8>
```
# refs
https://hynek.me/articles/taking-some-pain-out-of-python-logging/ ???TTT
