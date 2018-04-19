Copy specific resources, and make sure it also included in the jar file.
We need this because api_spec.yaml is put in the repo root directory. 
Also need to make sure that the output directory is target/classes. By default it is in target/
              <outputDirectory>${basedir}/target/classes</outputDirectory>
If we put the spec in src/main/resources/, we don't need this because maven by default will copy all files under that directory.
By default, maven uses the following plugins:
* maven-resources-plugin
* maven-jar-plugin
* maven-release-plugin???

Notes:
* If ```<includes>``` is not used, it copies recursively
* ```<directory>``` is relative to current directory (i.e. the directory of pom.xml)
```

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.xx.xx.xxxxxx</groupId>
  <artifactId>xxx-api-spec</artifactId>
  <version>1.0.0</version>
  <packaging>jar</packaging>

  <name>Xxxx API Specification</name>

  <build>
    <plugins>
      <plugin>
        <artifactId>maven-resources-plugin</artifactId>
        <executions>
          <execution>
            <id>copy-resources-id</id>
            <goals>
              <goal>copy-resources</goal>
            </goals>
            <phase>process-resources</phase>
            <configuration>
              <outputDirectory>${basedir}/target/classes</outputDirectory>
              <resources>          
                <resource>
                  <directory>./</directory>
                  <includes>
                        <include>api_spec.yaml</include>
                  </includes>
                </resource>
              </resources>              
            </configuration>            
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
</project>

```
