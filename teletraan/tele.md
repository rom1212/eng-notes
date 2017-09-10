## builds
* use artifact_url to point to the debian package, so that we don't need to store extra build files.
* change downloader to download the debian package, and then create a Teletraan file. 
  * download, create file structure. create the install scripts as well.
  * can also do pre-checks here :-)
* package info
  * scm as package name
  * scm_commit as package version 
