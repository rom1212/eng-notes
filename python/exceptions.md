# Catch Exceptions
* Catch all Exceptions
  * Use: "except Exception" instead of BaseException because it also contains GeneratorExit, SystemExit and KeyboardInterrupt. Otherwise, it is hard to exit, for example, exit() or Ctrl+C cannot exit from the code.
  * GeneratorExit is used for the clean-up work for generator, because it could be cases that the denerator is not done yet, and also need to do cleanups. https://stackoverflow.com/questions/30862196/generatorexit-in-python-generator

# Log Exceptions
* http://stackoverflow.com/questions/5191830/best-way-to-log-a-python-exception
* logger.exception(), e.g.
```
        try:
            self.serve_build()
        except Exception:
            log.exception("Deploy Agent got exceptions: {}".format(traceback.format_exc()))
```

# How to get exception message
## docs
* https://stackoverflow.com/questions/4308182/getting-the-exception-value-in-python
* https://stackoverflow.com/questions/33239308/how-to-get-exception-message-in-python-properly

## Examples
* maas uses str() implicitly by using "%s" % (e), e.g. https://github.com/maas/maas/blob/master/src/maasserver/dhcp.py#L670
```
    except Exception as exc:
        ipv6_exc = exc
        ipv6_status = SERVICE_STATUS.DEAD
        log.err(
            "Error configuring DHCPv6 on rack controller '%s': %s" % (
                rack_controller.system_id, exc))
```
It doesn't explicitly use str(e). However, string formatting with %s implicitly called str(), while %r implicitly called repr() and .format() implicitly calls ```__format__```. See:
* https://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
* https://www.python.org/dev/peps/pep-3101/
  * For all built-in types, an empty format specification will produce the equivalent of str(value).
* https://pyformat.info/
