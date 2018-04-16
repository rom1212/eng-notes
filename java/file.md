# Java File
## Absolute Path
```java
File file = new File("./target/test.txt");
String dirPath = file.getAbsoluteFile().getParentFile().getAbsolutePath()
assert dirPath.equals("/home/me/dev/target");
```
