# Config
/usr/lib/systemd/system/mariadb.service to /etc/systemd/system/mariadb.service

# Restart Service on Failure
https://jonarcher.info/2015/08/ensure-systemd-services-restart-on-failure/


```
copy /usr/lib/systemd/system/mariadb.service to /etc/systemd/system/mariadb.service
[service] section
Restart=always
RestartSec=3
```
