# Project Setup Automation
It is so important to automate all the setups of a project, including install, and build and run.
This is especially important to development because
* we might do that again and again
* we might forget the details, and after some time (e.g. 1 month), we can still easily catch up with the development.

# Code quality control
## PMD
* https://pmd.github.io/, https://pmd.github.io/pmd-6.1.0/
```
$ cd $HOME
$ wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F6.2.0/pmd-bin-6.2.0.zip
$ unzip pmd-bin-6.2.0.zip
$ alias pmd="$HOME/pmd-bin-6.2.0/bin/run.sh pmd"
$ pmd -d /usr/src -R java-basic -f text
```
## Others
* findbugs, code style check, errcheck (golang)

# Ramp Up
* Dev process
  * build, deploy
* Testing
  * Add more test
  * Make sure that it works
* Small changes - 
  * bug fix
  * small feature
