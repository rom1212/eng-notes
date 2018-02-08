# anacron
## /etc/cron.d/test
### Every minute
append date to /tmp/cron.log. file /etc/cron.d/test is not executable. It is run as user <user>, not as root.
```
* * * * * <user> echo $(date) >> /tmp/cron.minute.log
```
### Daily
every first minute of the hour 22:
```
0 22 * * *   <user> echo $(date) >> /tmp/cron.daily.log
```

## crontab command
/var/spool/cron/<user>
