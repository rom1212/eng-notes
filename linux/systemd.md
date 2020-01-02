# Config
* /etc/systemd/system/
  * mariadb.service
* /usr/lib/systemd/system/
  * mariadb.service to 

# Restart Service on Failure
* https://jonarcher.info/2015/08/ensure-systemd-services-restart-on-failure/
* https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units
* https://www.digitalocean.com/community/tutorials/how-to-configure-a-linux-service-to-start-automatically-after-a-crash-or-reboot-part-1-practical-examples



```
copy /usr/lib/systemd/system/mariadb.service to /etc/systemd/system/mariadb.service
[service] section
Restart=always
RestartSec=3
```

# Manually Stop a Service
```
$ sudo systemctl stop mariadb.service
```
