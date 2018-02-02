# rpm command
* list all installed rpm packages
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
* install a package
  * https://access.redhat.com/solutions/1189
* uninstall a package
```
rpm -e hellocurl-1.0-1.el7.centos.noarch
```
* conflicts: --force, --replacefiles
  * https://stackoverflow.com/questions/17582768/rpm-ignore-conflicts
  * --replacefiles solve this problem: "file /usr/bin/foo from install of foo-1.0-1 conflicts with file from package bar-2.0.20"

# Upgrade
* http://ftp.rpm.org/max-rpm/ch-rpm-upgrade.html
TTT???

# Extract content from rpm file
## rpm2cpio
* http://ftp.rpm.org/max-rpm/s1-rpm-miscellania-rpm2cpio.html, e.g.
```
 rpm2cpio ./packagecloud-test-1.1-1.x86_64.rpm | cpio -idmv
```
