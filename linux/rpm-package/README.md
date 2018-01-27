# rpm command
## list all installed rpm packages
```
rpm -qa
```
* query information of an installed package
```
rpm -qi mysql57-community-release-el7-11.noarch
```
* query information for a RPM package file
```
rpm -qip  mysql57-community-release-el7-11.noarch.rpm
```

## Upgrade
* http://ftp.rpm.org/max-rpm/ch-rpm-upgrade.html
TTT???

# Extract content from rpm file
## rpm2cpio
* http://ftp.rpm.org/max-rpm/s1-rpm-miscellania-rpm2cpio.html, e.g.
```
 rpm2cpio ./packagecloud-test-1.1-1.x86_64.rpm | cpio -idmv
```
