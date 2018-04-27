# mvn commands

## options
* To build the parent alone, I run mvn package -N (where -N is "non-recursive").
* To build a few modules, I run mvn package -pl api,servie (where -pl is "projects").
* To build both: mvn package -pl api,service --also-make

## mvn test
* [single test](http://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html):
  * mvn -Dtest=DBDAOTest#testDeploymentQueries test
    * DBDAOTest is test class name, and testDeploymentQueries is method name
* Integration test is different, because it handles setting up other resources, and clean up, and verification. If our
  code can handle all those things, we can just use "mvn test", e.g. our code can do setting up database using mysql-connector-mxj in setUpTest. 
  * https://stackoverflow.com/questions/1399240/how-do-i-get-my-maven-integration-tests-to-run

# Install on Ubuntu 16.04
## Install from apt package
```
sudo apt install maven

~$ mvn --version
Apache Maven 3.3.9
Maven home: /usr/share/maven
Java version: 1.8.0_131, vendor: Oracle Corporation
Java home: /usr/lib/jvm/java-8-openjdk-amd64/jre
Default locale: en_US, platform encoding: UTF-8
OS name: "linux", version: "4.10.0-33-generic", arch: "amd64", family: "unix

# optional - in case "javac -version" is not installed.
sudo apt install openjdk-8-jdk-headless
```
## download from maven.apache.org
https://maven.apache.org/install.html
* Download binary from here: https://maven.apache.org/download.cgi, e.g. apache-maven-3.5.0-bin.tar.gz
* tar xzvf apache-maven-3.5.0-bin.tar.gz
* set PATH to include the maven bin directory, e.g. ```export PATH=$PATH:~/bin/apache-maven-3.5.0/bin```
* mvn -v
* seems that JAVA_HOME is not needed.

## Proxy
${user.home}/.m2/settings.xml
```
<settings>
  <proxies>
   <proxy>
      <id>example-proxy</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>proxy.example.com</host>
      <port>8080</port>
      <username>proxyuser</username>
      <password>somepassword</password>
      <nonProxyHosts>www.google.com|*.example.com</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

## Mirror
```
<settings>
  <mirrors>
    <mirror>
      <id>UK</id>
      <name>UK Central</name>
      <url>http://uk.maven.org/maven2</url>
      <mirrorOf>central</mirrorOf>
    </mirror>
  </mirrors>
</settings>  
```
