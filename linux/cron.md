# anacron
## /etc/cron.d/test
Every minute append date to /tmp/cron.log. file /etc/cron.d/test is not executable.
```
* * * * * <user> echo $(date) >> /tmp/cron.log
```
