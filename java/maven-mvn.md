# mvn commands

## mvn test
* [single test](http://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html):
  * mvn -Dtest=DBDAOTest#testDeploymentQueries test
    * DBDAOTest is test class name, and testDeploymentQueries is method name

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

