# Services

## Two Services
* TeletraanService.java
```
        // Support pings as well
        Pings pings = new Pings(context);
```        
* TeletraanAgentService.java
```
# Just support pings
        Pings pings = new Pings(context);
```

## Handlers
### DeployHandler.java
* internalDeploy() <- deploy() <- resources/EnvDeploys.java. It creates a new deployment for a given environment.
  * create a record in "deploys" table.
    * select env_id, deploy_id, deploy_type, build_id, state from deploys order by start_date desc;
  * update deploy_id and deploy_type in "environs" table.
    * select env_id, env_name, stage_name, deploy_id, deploy_type, last_update from environs order by last_update desc;


# Tips
* Adding a fields DeployGoalBean.java
Might have problem of "com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class", e.g.
```
ERROR [2017-09-05 22:45:42,480] com.pinterest.teletraan.exception.GenericExceptionMapper: Server error:
! com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class com.pinterest.deployservice.bean.DeployGoalBean$TargetState and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) ) (through reference chain: com.pinterest.deployservice.bean.PingResponseBean["deployGoal"]->com.pinterest.deployservice.bean.DeployGoalBean["targetState"])
```
Solution: add public getters for all the data members.
https://stackoverflow.com/questions/8367312/serializing-with-jackson-json-getting-no-serializer-found
