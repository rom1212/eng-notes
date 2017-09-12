Java Runtime Errors
* @JsonProperty
  * If two data member are marked with the same @JsonProperty, compiling works, but it is runtime error, e.g. 
  ```java
  @JsonProperty('name')
  private String name;
  
  @JsonProperty('name')
  private String userName;
  ```
