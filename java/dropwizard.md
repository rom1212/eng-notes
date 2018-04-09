# Docs

## Main Docs
* http://www.dropwizard.io
* https://github.com/dropwizard/dropwizard
* http://www.dropwizard.io/1.3.0/docs/getting-started.html

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
    com.xx.xxx: DEBUG
  appenders:
    - type: file
      timeZone: UTC
      threshold: DEBUG
      archive: false
      currentLogFilename: /tmp/xx/service.log

server:
  applicationConnectors:
    - type: http
      port: 8090
  adminConnectors:
    - type: http
      port: 8091
```
