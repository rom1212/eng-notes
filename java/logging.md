# Java Logging
```java
import org.slf4j.LoggerFactory;
class MyClass {
  private static final Logger LOG = LoggerFactory.getLogger(MyClass.class);
  LOG.info("this is a String: {}, this is a list: {}", aString, aList);
}
```
