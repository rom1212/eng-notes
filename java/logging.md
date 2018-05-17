# Java Logging
## format
```java
import org.slf4j.LoggerFactory;
class MyClass {
  private static final Logger LOG = LoggerFactory.getLogger(MyClass.class);
  LOG.info("this is a String: {}, this is a list: {}", aString, aList);
}
```
## slf4j + logback
```
# eclipse oxygen 3
$ ./eclipse 
org.eclipse.m2e.logback.configuration: The org.eclipse.m2e.logback.configuration bundle was activated before the state location was initialized.  Will retry after the state location is initialized.
org.eclipse.m2e.logback.configuration: Logback config file: /home/xxx/eclipse-workspace/.metadata/.plugins/org.eclipse.m2e.logback.configuration/logback.1.8.3.20180227-2137.xml
SLF4J: Class path contains multiple SLF4J bindings.
SLF4J: Found binding in [bundleresource://496.fwk1458748394:1/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: Found binding in [bundleresource://496.fwk1458748394:2/org/slf4j/impl/StaticLoggerBinder.class]
SLF4J: See http://www.slf4j.org/codes.html#multiple_bindings for an explanation.
SLF4J: Actual binding is of type [ch.qos.logback.classic.util.ContextSelectorStaticBinder]
org.eclipse.m2e.logback.configuration: Initializing logback
```

## log4j config - old
* log4j.properties
* for test, src/test/resources/log4j.properties
