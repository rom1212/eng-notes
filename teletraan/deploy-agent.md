# env_status
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
