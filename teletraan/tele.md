## builds
* use artifact_url to point to the debian package, so that we don't need to store extra build files.
* change downloader to download the debian package, and then create a Teletraan file. 
  * download, create file structure. create the install scripts as well.
  * can also do pre-checks here :-)
* package info
  * scm as package name
  * scm_commit as package version 

## Downloader
* Add case for: extension == 'deb' 
  * logging can be sent to server by run_cmd (which reads the logging records)
* executor.py:run_cmd
  * what if return code is not 0, will it throw exception?
  * deploy_report - what's the status_code? how does that pop to server, and what will server act on that?
  * try it with tests/unit/deploy/utils/test_exec.py
  
 

