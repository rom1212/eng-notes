# Dev
* ./build.sh
* ./run.sh
* ./update.sh - build.sh and run.sh

# Code

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
    * select env_id, deploy_id, deploy_type, build_id, state, acc_status from deploys order by start_date desc;
  * update deploy_id and deploy_type in "environs" table.
    * select env_id, env_name, stage_name, deploy_id, deploy_type, last_update from environs order by last_update desc;

### PingHandler
* convergeEnvs() ??? 
* LOG.debug("Found the following envs {} associated with host {} and group {}.", envs.keySet(), hostName, groups);
* 

## DAO
* Implemtation
  * common/src/java/com/pinterest/deployservice/db/
* Interface
  * common/src/java/com/pinterest/deployservice/dao/

## AgentBean
* status: how the agent is doing the deployments, e.g. SUCCEEDED, TOO_MANY_RETRY, SCRIPT_FAILED. AgentStatus.java
* state: how agent itself is going, e.g. NORMAL, UNREACHABLE, STOP, see AgentState.java

## GoalAnalyst.java
* case 1.1: handle the last deployment step: SERVING_BUILD
  * This is the most common case for ping, where deployment is done, and it only does the reporting.
* case 1.2: agent normal execution with AgentStatus.SUCCEEDED, i.e. agent successfully executed the deployment step/stage. except the last step, i.e. SERVING_BUILD. 
* case 1.5: could be beginning of a new agent ping???

## SUCCEEDED
There are only two places that set the final state to be SUCCEEDED
* grep FINAL_STATE_TRANSITION_MAP * -r
  * common/src/main/java/com/pinterest/deployservice/handler/DeployHandler.java
    * created a new deployment, and make the old one as succeeded.
  * common/src/main/java/com/pinterest/deployservice/handler/CommonHandler.java
    * transitioner found that the deployId is not the current deployId of the associated environment anymore.
* not find related infor by
  * grep "DeployState.SUCCEEDED" * -r
  * grep "SUCCEEDED" * -r
  
Maybe we should mark it as SUCCEEDED when all active agents are deployed
* need to re-consider when a new agent joins
* the way to count the number of agents for an environment.
* worker/StateTransitioner.java -> handler/CommonHandler.java


# Tips
* Adding a fields DeployGoalBean.java
Might have problem of "com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class", e.g.
```
ERROR [2017-09-05 22:45:42,480] com.pinterest.teletraan.exception.GenericExceptionMapper: Server error:
! com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class com.pinterest.deployservice.bean.DeployGoalBean$TargetState and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) ) (through reference chain: com.pinterest.deployservice.bean.PingResponseBean["deployGoal"]->com.pinterest.deployservice.bean.DeployGoalBean["targetState"])
```
Solution: add public getters for all the data members.
https://stackoverflow.com/questions/8367312/serializing-with-jackson-json-getting-no-serializer-found
