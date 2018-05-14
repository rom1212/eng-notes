# RPM Examples
## Tools
* https://stackoverflow.com/questions/5613954/extract-the-spec-file-from-rpm-package
```
rpmrebuild --package --notest-install -e oracle-instantclient-basic-10.2.0.4-1.x86_64.rpm
rpmrebuild -s hercules.spec hercules
```
## MySQL
* docs
  * https://www.perkin.org.uk/posts/how-to-build-mysql-releases.html
* online specs
  * https://github.com/mysql/mysql-server/blob/8.0/packaging/rpm-oel/mysql.spec.in
  * https://github.com/twitter/mysql/blob/master/packaging/rpm-oel/mysql.spec.in
  * https://www2.atomicorp.com/channels/source/mysql/mysql.spec
* rpmrebuild
  * rpmrebuild -s mysql.spec mysql-community-server-5.7.22-1.el7.x86_64
* rpm --scripts
```
rpm -q --scripts mysql-community-server-5.7.22-1.el7.x86_64
sudo rpm -qp --scripts /var/cache/yum/x86_64/2.0SP2/mysql57-community/packages/mysql-community-server-5.7.22-1.el7.x86_64.rpm
```

