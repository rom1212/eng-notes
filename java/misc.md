# Misc
## classes
* https://docs.oracle.com/javase/8/docs/api/index.html?java/nio/charset/StandardCharsets.html
* Random
  * nextFloat: [0.0, 1)
    * This range is perfect for failure rate. 0.0. means no failure, and 1.0 mean all failure.
    ```java
      Random rand = new Random();
      if (rand.nextFloat() < failureRate) {
         // fail
      } else {
         // succeed
      }
    ```
