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
export SPOTBUGS=~/findbugs-3.0.1/bin/findbugs  # can be used by other scripts
alias spotbugs=~/findbugs-3.0.1/bin/findbugs   # for local usage
```
* Works for jar or class, e.g.
```
~/spotbugs-3.1.1/bin/spotbugs -maxHeap 500 -effort:min -high -html -output spotbugs_high.html -auxclasspath target/lib/ target/classes/ target/test-classes/

-auxclasspath target/lib/: for it not to complain about missing classes
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
