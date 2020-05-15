# cron job
## crontab command - easy for run as normal user
* crontab -e
  * example: daily at 23:30
    * ```30 23  * * * /home/<user>/bin/cron/test_cron.sh```
    * test_cron.sh: 
      * ```#!/bin/bash```
      * ```/home/<user>/bin/cron/test.sh >> /home/<user>/bin/cron/test_cron.log 2>&1``` 
    * test.sh
      * ```#!/bin/bash```
      * ```echo ======================================```
      * ```echo run date: $(date)```
      * ```USER=$(whoami)```
      * ```day=$(date +"%Y-%m-%d")```
* crontab -l

/var/spool/cron/<user>

## Create cron
* Ubuntu uses anacron
* locations
  * /etc/crontab - global crontab
  * other crontab files can be put here: /etc/cron.d/
  * /etc/cron.daily etc are actually setup by either crontab or /etc/cron.d/
* create-cron.sh (might not work anymore)
```
#!/bin/bash -ex

BIN=`realpath ./bin.sh`
# execute on the 5th minute of every hour
echo "5 * * * * $USER $BIN" | sudo tee /etc/cron.d/mycron.cron
```

## general crontab definition
```
# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed

```
### Every minute
append date to /tmp/cron.log. file /etc/cron.d/test is not executable. It is run as user <user>, not as root.
```
* * * * * <user> echo $(date) >> /tmp/cron.minute.log
```
### Every Hour
Every hour, at the 5th minute of that hour
```
5 * * * * <user> echo $(date) >> /tmp/cron.minute.log
```
  
### Daily
every first minute of the hour 22:
```
0 22 * * *   <user> echo $(date) >> /tmp/cron.daily.log
```

## duplicate running
* https://stackoverflow.com/questions/10552016/how-to-prevent-the-cron-job-execution-if-it-is-already-running
  * flock - can it release the lock if the process dies?
* https://stackoverflow.com/questions/14409651/will-cron-start-a-new-job-if-the-current-job-is-not-complete
