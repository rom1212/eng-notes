# dev
## First time
* ???
## Code Update/Change
* ./update.sh

# code
## env_status
* deployd/common/config.py: get_env_status_fn()
* deployd/agent.py: DeployAgent:_STATUS_FILE
* /tmp/deployd/env_status, example:
```
{
  "deploy-sentinel": {
    "build_info": {
      "build_branch": "master",
      "build_commit": "36772621683057978559095604549951",
      "build_id": "Yx2UMKCxRP2Kyy5-S0ZsWg_3677262",
      "build_name": "deploy-sentinel",
      "build_repo": "local",
      "build_url": "file:///tmp/quickstart-build.tar.gz"
    },
    "first_deploy": true,
    "op_code": "DEPLOY",
    "report": {
      "deployAlias": null,
      "deployId": "xiZZFdpiQXiuF_ZO2DLDZg",
      "deployStage": "SERVING_BUILD",      # this is the deploy steps (PRE_DOWNLOAD, POST_DOWNLOAD etc.)
      "envId": "vJauQoSlSDSjtJHr1WeFhQ",
      "envName": "deploy-sentinel",
      "errorCode": 0,
      "errorMessage": null,
      "extraInfo": null,
      "failCount": 0,
      "stageName": "canary",  # this is the environment stage, alpha, beta, gamma etc.
      "status": "SUCCEEDED"
    }
  }
}

```

## deploy-stager
Arguments
* -v, --build-id, args.build: build version ID
* -t, --target, args.target: target directory name
* -e, --env-name, args.env_name: environment name currently in deploy.
```
deploy-stager -v QZoW3W7JQ3SClrzSnnQvBQ_2296782 -t /tmp/deploy-sentinel -e deploy-sentinel
```

agent.py: get_staging_script(), "deploy-stager"

## deployd/common/config.py
* get_target(): 
  * default: /tmp/os.environ['ENV_NAME']
  * self._configs.get('target')
* get_script_directory(): 
  * script_dir=self.get_target()/teletraan/
  * or script_dir/os.environ['ENV_NAME']
  
## env_status.py
* dump_envs()
  * agent._update_ping_reports()
    * agent.update_deploy_status()
      * PingServer.__call__
      * serve_build(): after the deployment (process_deploy())
    * serve_build(): fail to update internal goal
