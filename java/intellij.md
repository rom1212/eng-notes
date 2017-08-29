# IntelliJ
* build jar
  * https://stackoverflow.com/questions/1082580/how-to-build-jars-from-intellij-properly
  ```
File -> Project Structure -> Project Settings -> Artifacts -> Click green plus sign -> Jar -> From modules with dependencies...
This configure how to generate the jar file, e.g. jar file name, directory, manifest file, Main class (this makes the run easy, e.g. just java -jar <jar file>). Default output directory is .\out\artifacts\<project name>_jar\<project name>.jar

Build | Build Artifact

Find the jar file in .\out\artifacts\<project name>_jar\<project name>.jar

```
