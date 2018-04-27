# Java Logging
## format
```java
import org.slf4j.LoggerFactory;
class MyClass {
  private static final Logger LOG = LoggerFactory.getLogger(MyClass.class);
  LOG.info("this is a String: {}, this is a list: {}", aString, aList);
}
```

## config
* log4j.properties
* for test, src/test/resources/log4j.properties
