# anacron
## /etc/cron.d/test
### Every minute append date to /tmp/cron.log. file /etc/cron.d/test is not executable.
```
* * * * * <user> echo $(date) >> /tmp/cron.minute.log
```
### Daily
every first minute of the hour 22:
```
0 22 * * *   <user> echo $(date) >> /tmp/cron.daily.log
```
