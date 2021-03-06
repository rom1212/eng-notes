# JDBC
* javax.sql
  * https://docstore.mik.ua/orelly/java-ent/jenut/ch27_01.htm
  * The javax.sql package contains the JDBC 2.0 Standard Extension API
  
# MyBatis
* Introduction and Gettting Started
  * http://www.mybatis.org/mybatis-3/index.html
* Generator
  * http://www.mybatis.org/generator/running/runningFromCmdLine.html
  * Generated - mapper classes, mapper xml files, e.g. (we can also manually create them)
    * BookMapper.java
    ```java
    int updateByPrimaryKeySelective(BookBean record);
    ```
    * BookMapper.xml
    ```xml
    <update id="updateByPrimaryKeySelective" parameterType="com.xxx.xxx.db.model.BookBean">
    update book
    <set>
      <if test="name != null">
        name = #{name,jdbcType=CHAR},
      </if>
      <if test="description != null">
        description = #{description,jdbcType=VARCHAR},
      </if>
      <if test="owner != null">
        owner = #{owner,jdbcType=VARCHAR},
      </if>
      <if test="statusEnum != null">
        status_enum = #{statusEnum,jdbcType=VARCHAR},
      </if>
      <if test="createTime != null">
        create_time = #{createTime,jdbcType=TIMESTAMP},
      </if>
      <if test="updateTime != null">
        update_time = #{updateTime,jdbcType=TIMESTAMP},
      </if>
    </set>
    where id = #{id,jdbcType=BIGINT}
    </update>    
    ```
* Problems
  * it might fail silently if the mapper class and the mapper xml doesn't match. e.g
    * The generated model file has a "status" field, but the mapper xml file doesn't have it when doing insert. In the end, the insert operation will succeed without writing "status" field.
    * This might be feature that can be used to add "status" first in the code, and then later change the schema. 
    * However, it would be better that mybatis can at least log an warning there so that we can spot this potential issue.
  
# Common Issues
## date
* https://stackoverflow.com/questions/2305973/java-util-date-vs-java-sql-date

# MySQL Test
## mysql-connector-mxj
* Newest version is 5.0.12 and is discontinued, with two jar files.
  * mysql-connector-mxj-5.0.12.jar
  * mysql-connector-mxj-db-files-5.0.12.jar
    * created: 5-5-9/Linux-x86_64/
    * inflated: 5-5-9/Linux-x86_64/mysql
    * inflated: 5-5-9/Linux-x86_64/version.txt
    * inflated: 5-5-9/Linux-x86_64/mysqld
* debug
  ```
  cd <path to mysqld>/data
  ../bin/mysql -u tester -p --port <the port number, e.g. 3305> --socket=./mysql.sock
  ```
* common issues
  * might not be able to stop it somehow, e.g. if the folder is deleted. We need to stop the process first, and then remove the folder, e.g.
```
if lsof -i tcp:3303; then
    lsof -i tcp:3303 | awk 'NR!=1 {print $2}' | xargs kill
fi

if lsof -i tcp:3305; then
    lsof -i tcp:3305 | awk 'NR!=1 {print $2}' | xargs kill
fi

rm -rf /tmp/xxx/xx/  # the directory for embedded mysql working directory
```
