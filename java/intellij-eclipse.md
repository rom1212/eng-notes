# Also
* General instructions: https://github.com/rom1212/eng-notes/blob/master/intellij-eclipse.md

# IntelliJ for Java
* build jar
  * https://stackoverflow.com/questions/1082580/how-to-build-jars-from-intellij-properly

```
File -> Project Structure -> Project Settings -> Artifacts -> Click green plus sign -> Jar -> From modules with dependencies...
This configure how to generate the jar file, e.g. jar file name, directory, manifest file, Main class (this makes the run easy, e.g. just java -jar <jar file>). Default output directory is .\out\artifacts\<project name>_jar\<project name>.jar

Build | Build Artifact

Find the jar file in .\out\artifacts\<project name>_jar\<project name>.jar

Run the jar file by: java -jar path/to/<project name>.jar
```

# Eclipse for Java
* Classpath similar to ```-cp path:path```
  * Find the java file with main() -> Right Click -> Debug As - > Debug Configurations -> Java Application (double click to create)
  * Classpath tab: Advanced -> Add Variable String

