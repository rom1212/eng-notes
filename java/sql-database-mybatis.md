# JDBC
* javax.sql
  * https://docstore.mik.ua/orelly/java-ent/jenut/ch27_01.htm
  * The javax.sql package contains the JDBC 2.0 Standard Extension API
  
# MyBatis
* Introduction and Gettting Started
  * http://www.mybatis.org/mybatis-3/index.html
* Generator
  * http://www.mybatis.org/generator/running/runningFromCmdLine.html
* Problems
  * it might fail silently if the mapper class and the mapper xml doesn't match. e.g
    * The generated model file has a "status" field, but the mapper xml file doesn't have it when doing insert. In the end, the insert operation will succeed without writing "status" field.
    * This might be feature that can be used to add "status" first in the code, and then later change the schema. 
    * However, it would be better that mybatis can at least log an warning there so that we can spot this potential issue.
  
# Common Issues
## date
* https://stackoverflow.com/questions/2305973/java-util-date-vs-java-sql-date
