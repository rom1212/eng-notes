# RPM
## rpm basics
* http://ftp.rpm.org/max-rpm/index.html. ???TTT read this.
* scripts: https://fedoraproject.org/wiki/Packaging:Scriptlets
* source code: https://github.com/rpm-software-management/rpm

## rpm command
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

## rpm package format
* http://rpm5.org/docs/api/pkgformat.html

## rpm install (-ivh) vs upgrade (-Uvh)
* background: "rpm --upgrade" can handle files that are changed locally by someone manually. This is especially true for config files. rpm handles this by using md5 to remember whether some files are changed locally or not. This [link]( https://www.linuxquestions.org/questions/fedora-35/rpm-ivh-vs-rpm-uvh-256231/) explains the main idea:
```
Update (-U) is different install (-i) if the package was previously installed: especially if some of the files have been modified. Update will attempt to preserve your modifications, whereas install will remove all traces of any modifications you might have made.

If the current contents of the file is different from both that what was originally installed and what is in the update package, and the file in the update package is also different from that originally installed, the current contents are saved to a file with .rpmsave extension before replacing it with the file from the update package.

If there was no file in the originally installed package, the current file is renamed with the .rpmorig extension before replacing it with the file from the update package.

If using update, you are responsible for manually processing any .rpmsave or .rpmorig files that are created.

This handling of modifications is in addition to the other difference: update removes the old package (if there was one), but install does not (requiring manual use of uninstall (-e) if you want to get rid of the other versions).
```
* More details on the upgrade process is here: http://ftp.rpm.org/max-rpm/ch-rpm-upgrade.html
  * original file: means the file last time installed
  * current file: means the file at the time of installation, which could be modified by someone manually. So, it could be different from original file.
  * new file: in the new package.
TTT???

## Extract content from rpm file
### rpm2cpio
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
### show scripts
```
rpm -qp --scripts ./packagecloud-test-1.1-1.x86_64.rpm
```
https://blog.packagecloud.io/eng/2015/10/13/inspect-extract-contents-rpm-packages/
  

# Yum
## yum vs rpm command
"The benefit of yum is that it will resolve dependencies for you and also install dependencies along with the concerned application. But you need to define the path of software resources in /etc/yum.repos.d in a .repo file
"
* https://www.lifewire.com/install-rpm-packages-using-yum-2201155
## yum source - python
* https://github.com/rpm-software-management/yum
