# Teletraan
https://github.com/pinterest/teletraan

## Quick Start
https://github.com/pinterest/teletraan/wiki/Quickstart-guide
* Manual Option
  * wget is faster
  * Capacity Config - use "test-host-1" as the hostname because this is the content in /teletraan-demo/deploy-sentinel/host_info
  * Might need to run "deploy-agent" twice to make the deployment start to deploy

## Setup on Host
https://github.com/pinterest/teletraan/wiki/Setup-Teletraan-directly-on-host
* Run Teletraan Server
  * It's easier to debug if we run it in foreground mode: ./teletraanservice/bin/run.sh run
* Run Deploy Dashboard
```
  cd ~/teletraan/deploy-board
  ~/teletraan/deploy-board$ virtualenv venv
  ~/teletraan/deploy-board$ source venv/bin/activate
  (venv) xx@xx:~/teletraan/deploy-board$ pip install -r requirements.txt
  (venv) xx@xx:~/teletraan/deploy-board$ ./run.sh start
```
