# Teletraan
https://github.com/pinterest/teletraan

## Quick Start
https://github.com/pinterest/teletraan/wiki/Quickstart-guide
* Manual Option
  * wget is faster
  * Capacity Config
    * just fill the host class. No need for the host name.
    * Or use "test-host-1" as the hostname because this is the content in /teletraan-demo/deploy-sentinel/host_info
  * Might need to run "deploy-agent" twice to make the deployment start to deploy
  * Only one virtualenv is created in ~/teletraan-demo/venv
    * start venv
      * cd ~/teletraan-demo
      * source venv/bin/activate or . venv/bin/activate
    * can be used for publishing build or deploy-agent.

### Directory Structure
* logs - /tmp/deployd/logs/
  * deploy-agent.log  deploy-sentinel.log
* binary
  * downloaded to: /tmp/deployd/builds/
    * deploy-sentinel-jXRgaOLYTh-YOSxzODjSAg_3551948.tar.gz
    * jXRgaOLYTh-YOSxzODjSAg_3551948
    * jXRgaOLYTh-YOSxzODjSAg_3551948.extracted
  * symlink: /tmp/deploy-sentinel -> /tmp/deployd/builds/jXRgaOLYTh-YOSxzODjSAg_3551948

### Deploy Steps/Stages
* Steps
  * PRE_DOWNLOAD, DOWNLOADING, POST_DOWNLOAD, STAGING, PRE_RESTART, RESTARTING, POST_RESTART, SERVING_BUILD
* special steps - see agent.py:process_deploy()
  * DOWNLOADING: use deploy-downloader: deploy-agent/deployd/download/downloader.py
  * STAGING: deploy-stager: deploy-agent/deployed/staging/stager.py
* ls /tmp/deploy-sentinel/teletraan/
    * POST_DOWNLOAD  POST_RESTART  PRE_DOWNLOAD  PRE_RESTART  RESTARTING  test.conf  test.conf.tmpl

### Kill Previous Build/Version
* teletraan/PRE_DOWNLOAD
```
#!/bin/bash

set +e

echo Running PRE_DOWNLOAD script.
# Remove old tmp files
rm -r /tmp/deploy-sentinel

# Delete running processes on port 8000
PORT_NUMBER=8000
lsof -i tcp:${PORT_NUMBER} | awk 'NR!=1 {print $2}' | xargs kill
```


## Setup on Host
https://github.com/pinterest/teletraan/wiki/Setup-Teletraan-directly-on-host
* sudo vim /etc/sudoers
* Run Teletraan Server
  * sudo apt-get install  mysql-server-5.7, mysql -u root, source xxx/deploy-service/common/src/main/resources/sql/deploy.sql
  * sudo apt install maven, and javac
  * ./build.sh
  * ./run.sh (or update.sh)
  * Add mysql password in file: ~/teletraan/deploy-service/teletraanservice/bin/server.yaml
  * It's easier to debug if we run it in foreground mode: 
  ```./teletraanservice/bin/run.sh run```
* Run Deploy Dashboard
```
  cd ~/teletraan/deploy-board
  ~/teletraan/deploy-board$ virtualenv venv
  ~/teletraan/deploy-board$ source venv/bin/activate
  (venv) xx@xx:~/teletraan/deploy-board$ pip install -r requirements.txt
  (venv) xx@xx:~/teletraan/deploy-board$ ./run.sh start
```
http://127.0.0.1:8888/

## Deploy Agent (deploy-agent)

### Data
* DeployGoal
```
        self.deployId = None  # is this used for detect changes???
        self.envId = None
        self.envName = None
        self.stageName = None
        self.deployStage = None
        self.build = None
        self.deployAlias = None
        self.config = None
        self.scriptVariables = None
        self.firstDeploy = None
        self.isDocker = None
```
* DeployStatus
```
    report = None
    build_info = None
    runtime_config = None
    first_deploy = None
    op_code = OpCode.NOOP
    script_variables = None
    is_docker = None

        self.report.envId = deploy_goal.envId
        self.report.deployId = deploy_goal.deployId
        self.report.deployStage = deploy_goal.deployStage
        self.report.deployAlias = deploy_goal.deployAlias
        self.report.envName = deploy_goal.envName
        self.report.status = AgentStatus.UNKNOWN
        self.report.stageName = deploy_goal.stageName
        
        self.first_deploy = deploy_goal.firstDeploy
        self.is_docker = deploy_goal.isDocker
        self.build_info = BuildInfo(deploy_goal.build.***)
        self.script_variables = deploy_goal.scriptVariables
        self.runtime_config = dict(deploy_goal.config)
        
        self.op_code = response.opCode or self.op_code = OperationCode._VALUES_TO_NAMES[json_value.get('op_code', OpCode.NOOP)]
```
* PingResponse
```diff
+ There is only one deployGoal in the response, but there could be more than one reports in the request. 
- This is because it doesn't want to have multiple deployments at the same time.
```

```
        self.opCode = OpCode.NOOP or self.opCode = jsonValue.get('opCode')
        self.deployGoal = None or self.deployGoal = DeployGoal(jsonValue=jsonValue.get('deployGoal'))
```
* PingReport
```
        self.deployId = None
        self.envId = None
        self.envName = None
        self.stageName = None
        self.deployStage = None
        self.status = None  # AgentStatus, better be deploymentStatus??? or this is just for agent???
        self.errorCode = 0
        self.errorMessage = None
        self.failCount = 0
        self.extraInfo = None
        self.deployAlias = None
```
* PingRequest
```
        self.hostId = hostId
        self.hostName = hostName
        self.hostIp = hostIp
        self.groups = groups
        self.reports = reports  # a list of PingReport, difference - ping_report["agentStatus"] = report.status
```
* DeployReport
  * This is confusing for some reasons
    * There is already PingReport.
    * There is DeployStatus.
  
### deployd/agent.py
* self._client.send_reports(self._envs)
  * how to determine whether it is just to send report, or it also need to get a new deployment id???

### deployd/client/client.py 
* send_reports() - used for two purposes
  * report the status of the deployment
  * check whether there is any goal changes from the server.
  
## Deploy Service (deploy-service)
### deployservice/handler/PingHandler.java
* ping()
  * GoalAnalyst
  * pick the first one from List<GoalAnalyst.InstallCandidate> installCandidates, which is sorted mostly according priority, and also consider AgentState.STOP, installCandidate.needWait.
* canDeploy ???
  * Check if we can start deploy on host for certain env. We should not allow more than parallelThreshold hosts in install in the same time
