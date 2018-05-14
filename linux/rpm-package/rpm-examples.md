# RPM Spec Examples
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

## Others
* cassandra
  * https://github.com/karlbohlmark/cassandra-rpm/blob/master/apache-cassandra.spec
* dhcp
  * https://git.centos.org/blob/rpms!dhcp.git/3f2076a2a871a7866f908b22e38f2a6da8f0651e/SPECS!dhcp.spec
  * https://src.fedoraproject.org/cgit/rpms/dhcp.git/tree/dhcp.spec?id=4a364d130b918caed6d357fd5a1fcc2c35926851
*  kubelet - simple
  * https://github.com/kubernetes/release/blob/master/rpm/kubelet.spec
* cadvisor - simple
  * https://git.centos.org/blob/rpms!cadvisor.git/058502407d0469fbb112b23226a47f15de8068dc/SPECS!cadvisor.spec
