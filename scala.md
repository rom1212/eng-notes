# sbt
## Gettting started guide
http://www.scala-sbt.org/0.13/docs/Getting-Started.html

## Install sbt on Ubuntu/Debian
http://www.scala-sbt.org/0.13/docs/Installing-sbt-on-Linux.html
```
echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a /etc/apt/sources.list.d/sbt.list
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2EE0EA64E40A89B84B2DF73499E82A75642AC823
sudo apt-get update
sudo apt-get install sbt

[info] Set current project to root (in build file:/)
[info] This is sbt 0.13.15
[info] The current project is {file:/}root 0.1-SNAPSHOT
[info] The current project is built against Scala 2.10.6
[info] Available Plugins: sbt.plugins.IvyPlugin, sbt.plugins.JvmPlugin, sbt.plugins.CorePlugin, sbt.plugins.JUnitXmlReportPlugin, sbt.plugins.Giter8TemplatePlugin
[info] sbt, sbt plugins, and build definitions are using Scala 2.10.6
# date: 2017-07-11
```
