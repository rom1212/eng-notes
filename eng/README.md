# Development
## Tricky Bugs
* Enum change
  * whenever add or remove an enum (e.g. status), make sure to check all the use cases of existing enum values. 
  * Example: InActive and Active, and we want to add InUse. One usage case is to get all the Active entities, and it uses
    "status==Active". This doesn't work with InUse, and we need to change it to "status!=InActive".
* Relative directory
  * Don't depend on current working directory since this is not threadsafe.
  * Make use of absolute path as possible, since the current working directory could change in the code (e.g. os.chdir, not by calling system("cd xxx")). 
  * Example: if we set glog by flag.Set("log_dir", "./logs"), the logs file could change to "/tmp" if the current working directory is changed to some other directory where the code doesn't have permission to write logs. Actually writing to "/tmp/" is easier to find out. But writing to other places is more difficult to debug (when we need to use lsof to find out)
* Deadlock
  * In golang, don't use channel together with mutex, because they can cause deadlock
* Update(): update is complicated.
  * update cases
    * nothing changes
    * Inplace update
    * Addition update
    * removal update
  * Examples:
    * terraform resource: Update()

## Code Review
* [code review](./code-review.md)

## Project Setup Automation
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
$ pmd -d /usr/src -R java-basic -f textcolor
$ pmd -d . -R java-basic -f textcolor -version 1.8 -language java
```
* https://pmd.github.io/pmd-6.2.0/pmd_userdocs_getting_started.html
* Using short name for ruleset, where short names are defined here for some examples
  * https://github.com/pmd/pmd/blob/master/pmd-core/src/main/java/net/sourceforge/pmd/cli/PMDCommandLineInterface.java
## Spotbugs/Findbugs
* docs
  * https://github.com/spotbugs/spotbugs
  * http://spotbugs.readthedocs.io/en/latest/running.html#quick-start
  * http://spotbugs.readthedocs.io/en/latest/installing.html
  * http://findbugs.sourceforge.net/
  * https://github.com/findbugsproject/findbugs
* Install
```
wget http://repo.maven.apache.org/maven2/com/github/spotbugs/spotbugs/3.1.1/spotbugs-3.1.1.tgz
tar -xvf spotbugs-3.1.1.tgz
export SPOTBUGS=~/spotbugs-3.1.1/bin/spotbugs  # can be used by other scripts
alias spotbugs=~/spotbugs-3.1.1/bin/spotbugs   # for local usage
```
* Works for jar or class, e.g.
```
~/spotbugs-3.1.1/bin/spotbugs -maxHeap 500 -effort:min -high -html -output spotbugs_high.html -auxclasspath target/lib/ target/classes/ target/test-classes/

-auxclasspath target/lib/: for it not to complain about missing classes
```

## Others
* findbugs, code style check, errcheck (golang), gometalinter

# Ramp Up
* Dev process
  * build, deploy
* Testing
  * Add more test
  * Make sure that it works
* Small changes - 
  * bug fix
  * small feature

## Start a New Project
* Who I can learn from so that I can
  * start the project faster
  * avoid pitfalls.
  
## Production Service
* Do we have throttling to avoid DDOS?
* Do we have draining to start from scratch, e.g. can we drain the old messages in our queue?
