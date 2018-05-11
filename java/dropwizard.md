# Docs
## Example
https://github.com/rom1212/taskboard-dropwizard

## Quick Start
* Create a new dropwizard project
  * mvn "archetype:generate" "-DinteractiveMode=false" "-DarchetypeGroupId=io.dropwizard.archetypes" "-DarchetypeArtifactId=java-simple" "-DarchetypeVersion=1.3.0" "-DgroupId=myservice.xxx.com" "-DartifactId=myservice" "-Dpackage=com.xxx.myservice" "-Dname=MyService" "-Dversion=0.1-SNAPSHOT" "-Dshaded=true" "-Ddescription='My Service'"
* found this here: dropwizard-archetypes/src/main/resources/dropwizard-create, by cloning and grep. github search doesn't work that well.
```bash
# http://www.dropwizard.io/1.3.0/docs/getting-started.html
# batch mode - the same as above, but displayed as one line
mvn "archetype:generate" "-DinteractiveMode=false" "-DarchetypeGroupId=io.dropwizard.archetypes" "-DarchetypeArtifactId=java-simple" "-DarchetypeVersion=1.3.0" "-DgroupId=myservice.xxx.com" "-DartifactId=myservice" "-Dpackage=com.xxx.myservice" "-Dname=MyService" "-Dversion=0.1-SNAPSHOT" "-Dshaded=true" "-Ddescription='My Service'"

# interactive mode
mvn archetype:generate -DarchetypeGroupId=io.dropwizard.archetypes -DarchetypeArtifactId=java-simple -DarchetypeVersion=1.3.0
```

## Main Docs
* http://www.dropwizard.io
* https://github.com/dropwizard/dropwizard
* http://www.dropwizard.io/1.3.0/docs/getting-started.html
* config reference: http://www.dropwizard.io/1.3.0/docs/manual/configuration.html#request-log

## Misc Docs
* Configuration:
  * https://github.com/dropwizard/dropwizard/blob/master/dropwizard-core/src/main/java/io/dropwizard/Configuration.java
  * comments says that it is using yaml. But the code is using  @JsonProperty("server"). So, I think it is using json. And also, the ConfigurationTest.java is using jackson ObjectMapper.
* Managed:
  * Create a service with start() and stop(): http://www.dropwizard.io/0.9.1/dropwizard-lifecycle/apidocs/io/dropwizard/lifecycle/Managed.html
* Jersey:
  * https://en.wikipedia.org/wiki/Project_Jersey
  * https://jersey.java.net/


# Service
## API
* Start up log
```
INFO  [2017-12-30 03:31:24,719] io.dropwizard.jersey.DropwizardResourceConfig: The following paths were found for the configured resources:

    GET     /v1/builds (com.xxx.xxx.xxx.resource.Builds)
    ...
```
This is especially useful to find out where the code is.

## Config ports
server.yaml
```
logging:
  level: INFO
  loggers:
    taskboard.io: DEBUG
  appenders:
    - type: file
      currentLogFilename: /tmp/taskboard/service.log
      timeZone: UTC
      threshold: ALL
      archive: true
      archivedLogFilenamePattern: /tmp/taskboard/service.log.%d.gz
      archivedFileCount: 10
      # customized logging format with file line number
      # logFormat: "%date %level [%thread] %logger{10} [%file:%line] %msg%n"
      # includeCallerData: true        

server:
  applicationConnectors:
    - type: http
      port: 8080
  adminConnectors:
    - type: http
      port: 8081

  requestLog:
    appenders:
      - type: file
        currentLogFilename: /tmp/taskboard/access.log
        threshold: ALL
        timeZone: UTC
        archive: true
        archivedLogFilenamePattern: /tmp/taskboard/access.log.%d.gz
        archivedFileCount: 10
```
For customized logging, see:
* https://stackoverflow.com/questions/27522905/dropwizard-log-format-method-and-line-is-not-working

## Generate Swagger
```java
public class TaskBoardService extends Application<TaskBoardConfiguration> {
    @Override
    public void run(final TaskBoardConfiguration configuration,
                    final Environment environment) {

        environment.jersey().register(new ApiListingResource());
        environment.jersey().register(new SwaggerSerializers());
        BeanConfig config = new BeanConfig();
        config.setTitle("Task Board Service API Docs");
        config.setVersion("0.1.0");
        // make sure this is correct, e.g. resource vs resources.
        config.setResourcePackage("io.taskboard.service.resources");
        config.setScan(true);
    }
}
```
