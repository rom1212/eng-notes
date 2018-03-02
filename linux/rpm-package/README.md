# rpm basics
* http://ftp.rpm.org/max-rpm/index.html. ???TTT read this.
* scripts: https://fedoraproject.org/wiki/Packaging:Scriptlets

# rpm command
* docs
  * https://www.tecmint.com/20-practical-examples-of-rpm-commands-in-linux/
  * https://wiki.centos.org/TipsAndTricks/YumAndRPM
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
  * rpm -ivh foo.rpm
* uninstall a package
```
rpm -e hellocurl-1.0-1.el7.centos.noarch
```
* conflicts: --force, --replacefiles
  * https://stackoverflow.com/questions/17582768/rpm-ignore-conflicts
  * --replacefiles solve this problem: "file /usr/bin/foo from install of foo-1.0-1 conflicts with file from package bar-2.0.20"
* dry run:
  * rpm --test
  * check whether it is installed???TTT : ```rpm -q <package name>```, this can also check previous versions

# rpm package format
* http://rpm5.org/docs/api/pkgformat.html

# yum command
"The benefit of yum is that it will resolve dependencies for you and also install dependencies along with the concerned application. But you need to define the path of software resources in /etc/yum.repos.d in a .repo file
"
* https://www.lifewire.com/install-rpm-packages-using-yum-2201155

# Upgrade
* http://ftp.rpm.org/max-rpm/ch-rpm-upgrade.html
TTT???

# Extract content from rpm file
## rpm2cpio
* http://ftp.rpm.org/max-rpm/s1-rpm-miscellania-rpm2cpio.html, e.g.
```
 rpm2cpio ./packagecloud-test-1.1-1.x86_64.rpm | cpio -idmv
```
rpmdev-extract (https://github.com/RsrchBoy/rpmdevtools/blob/master/rpmdev-extract) also use this method.
* source code
  * rpm2cpio
    * https://github.com/rpm-software-management/rpm/blob/master/rpm2cpio.c
    * https://github.com/rom1212/rpm/blob/master/rpm2cpio.c
  * cpio
    * https://ftp.gnu.org/gnu/cpio/
    * https://github.com/Distrotech/cpio
    * https://github.com/rom1212/cpio
## show scripts
```
rpm -qp --scripts ./packagecloud-test-1.1-1.x86_64.rpm
```
https://blog.packagecloud.io/eng/2015/10/13/inspect-extract-contents-rpm-packages/
  
