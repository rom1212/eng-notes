# basic
## Map
Iterate over map
```java
for (Map.Entry<String, Object> entry : map.entrySet()) {
    String key = entry.getKey();
    Object value = entry.getValue();
    // ...
}
```

## String
* String.format("%s_%d", "abcd", index)
  * format is a static function. So, DONOT use "%s_%d".format("abcd", index), 
