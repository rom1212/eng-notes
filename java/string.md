# Java String
## Format
```java
// https://stackoverflow.com/questions/6431933/how-to-format-strings-in-java

import java.text.MessageFormat;
MessageFormat.format("String is \"{1}\", number is {0}.", 42, "foobar");

// This is similar to 
import org.slf4j.LoggerFactory;
class MyClass {
  private static final Logger LOG = LoggerFactory.getLogger(MyClass.class);
  LOG.info("this is a String: {}, this is a list: {}", aString, aList);
}
```
