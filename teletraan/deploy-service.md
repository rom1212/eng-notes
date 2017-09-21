# Dev

## Iteration
* ./build.sh
* ./run.sh
* ./update.sh - build.sh and run.sh

## Need a new deployment for test
* Use "RESTART" to retire old failed deployment. (keep the same build)
  * clean up build directory: rm -rf /tmp/deployd/builds/*
* retire old deployment only when the "state" is SUCCEEDING or RUNNING. No need to retire it if its "state" is FAILING.
```
update deploys set state = 'SUCCEEDED', acc_status = 'ACCEPTED' where env_id = 'f3SvF2OgSgmavFU6b0aQiw' and deploy_id = 'thchAmZLRt2TytOdq31LDQ';
```

## Retire old deployments
```
update deploys set state = 'SUCCEEDED', acc_status = 'ACCEPTED' where env_id = 'f3SvF2OgSgmavFU6b0aQiw' and deploy_id = 'thchAmZLRt2TytOdq31LDQ';
```

## Show Builds and Packages Together
```
select scm_commit_7, builds.build_id, package_name, package_url from builds join packages on builds.build_id = packages.build_id order by builds.publish_date desc;
```

## Reset Dev
* Mysql
  * delete from agents;  // delete existing agents
  * Update as succeed, (or delete from deploys, be careful since other tables might referring to it, e.g. environs)
  ```
  update deploys set state = 'SUCCEEDED', acc_status = 'ACCEPTED' where env_id = '' and deploy_id = '';
  ```
* Agent
  * rm /tmp/deployd/env_status
  * rm /tmp/deployd/logs/* or move log files;

## Quick Experiment 
common/.../common/CommonUtilsTest.java
```java
    @Test
    public void testExperiment() {
        System.out.println("testExperiment");
    }
```

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
## Tables
* MySQL commands: show databases; use deploy; show tables;
* environments
```
select env_id, env_name, stage_name, deploy_id, deploy_type, last_update from environs order by last_update desc;
```
* deploys - one env_id -> many deploy_id
```
select env_id, deploy_id, deploy_type, build_id, state, acc_status from deploys order by start_date desc;
```
Retire a deployment
```
update deploys set state = 'SUCCEEDED', acc_status = 'ACCEPTED' where env_id = '' and deploy_id = '';
```

* agents - one (host_id, env_id) -> many deploy_id
```
select host_id, host_name, env_id, deploy_id, deploy_stage, state, status from agents;
```
* builds - build information (build_name -> env_name)
```
select scm_commit_7, build_id, build_name, artifact_url from builds order by publish_date desc;
```
* packages 
```
select package_name, package_version, package_url, , group_id from packages order by publish_date desc;
```
* map environment to hosts and envs
  * hosts_and_envs
  * groups_and_envs

## Interaction with Deploy Agent
* return results to agent
  * PingResponseBean.java
    * DeployGoalBean.java

## Handlers/Resources

### Envrionment
* com.pinterest.teletraan.resource.Environs: "Successfully created env stage"
* com.pinterest.teletraan.resource.EnvCapacities: "Successfully updated env deploy-sentinel/canary capacity config"

### DeployHandler.java
* internalDeploy() <- deploy() <- resources/EnvDeploys.java. It creates a new deployment for a given environment.
  * create a record in "deploys" table.
    * select env_id, deploy_id, deploy_type, build_id, state, acc_status from deploys order by start_date desc;
  * update deploy_id and deploy_type in "environs" table.
    * select env_id, env_name, stage_name, deploy_id, deploy_type, last_update from environs order by last_update desc;

### PingHandler
* convergeEnvs() ??? 
* LOG.debug("Found the following envs {} associated with host {} and group {}.", envs.keySet(), hostName, groups);

### Restart
```
# deploys table
+------------------------+------------------------+-------------+--------------------------------+-----------+----------------+
| env_id                 | deploy_id              | deploy_type | build_id                       | state     | acc_status     |
+------------------------+------------------------+-------------+--------------------------------+-----------+----------------+
| f3SvF2OgSgmavFU6b0aQiw | thchAmZLRt2TytOdq31LDQ | RESTART     | CXRHe11-TuOgxgSIP5Ydhw_8507456 | RUNNING   | PENDING_DEPLOY |
```

### Builds.java
* resource/Builds.java
* publish builds, etc.

### UserRoles.java
* Use for environment, where resource_id is the environment name.
```
INFO  [2017-09-14 19:07:41,727] com.pinterest.teletraan.resource.UserRoles: Successfully created new user permission for resource deploy-sentinel with com.pinterest.deployservice.bean.UserRolesBean@1211df6a[user_name=user_name1,resource_id=deploy-sentinel,resource_type=ENV,role=OPERATOR]
```
### TokenRoles.java
* Use for environment, where resource_id is the environment name.
```
INFO  [2017-09-14 19:15:49,012] com.pinterest.teletraan.resource.TokenRoles: Successfully created new script permission for resource deploy-sentinel with com.pinterest.deployservice.bean.TokenRolesBean@73155791[script_name=script_name1,resource_id=deploy-sentinel,resource_type=ENV,token=xxxxxxxx,role=OPERATOR,expire_date=1820776548982]
```
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

## State Transition
Restart could be
```
| f3SvF2OgSgmavFU6b0aQiw | 6TIx81N5TvCSB2yNzCgDfw | RESTART     | 3MDgayoxR_aOTqTcycSLlw_6113136 | RUNNING   | PENDING_DEPLOY
```

# Tips
* Adding a fields DeployGoalBean.java
Might have problem of "com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class", e.g.
```
ERROR [2017-09-05 22:45:42,480] com.pinterest.teletraan.exception.GenericExceptionMapper: Server error:
! com.fasterxml.jackson.databind.JsonMappingException: No serializer found for class com.pinterest.deployservice.bean.DeployGoalBean$TargetState and no properties discovered to create BeanSerializer (to avoid exception, disable SerializationFeature.FAIL_ON_EMPTY_BEANS) ) (through reference chain: com.pinterest.deployservice.bean.PingResponseBean["deployGoal"]->com.pinterest.deployservice.bean.DeployGoalBean["targetState"])
```
Solution: add public getters for all the data members.
https://stackoverflow.com/questions/8367312/serializing-with-jackson-json-getting-no-serializer-found
