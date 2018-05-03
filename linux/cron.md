# anacron

## Create cron
* locations
  * /etc/crontab - global crontab
  * other crontab files can be put here: /etc/cron.d/
  * /etc/cron.daily etc are actually setup by either crontab or /etc/cron.d/
  

## crontab
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

## crontab command
/var/spool/cron/<user>

