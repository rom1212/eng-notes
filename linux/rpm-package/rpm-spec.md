# RPM Spec
## Scripts
* Add user on $pre
  * https://linux.die.net/man/8/useradd
  * useradd can create and update an existing user
  * could be security risk if that user already exists and we add it to the e.g. sudo.
* delete user in $preun or $postun
  * might be ok - 
  * security concerns - some else created with the same user id
* create wheel group in /etc/suoders.d/xxx
  * How fast it is to pickup the new update?

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
## Cassandra
* https://www.howtoforge.com/tutorial/how-to-install-apache-cassandra-on-centos-7/
  * http://blog.mclaughlinsoftware.com/2017/07/25/install-cassandra-on-fedora/
```
$ sudo vim /etc/yum.repos.d/cassandra.repo
[cassandra]
name=Apache Cassandra
baseurl=https://www.apache.org/dist/cassandra/redhat/311x/
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://www.apache.org/dist/cassandra/KEYS

$ sudo yum -y install --downloadonly cassandra

$ sudo rpm -qp --scripts /var/cache/yum/x86_64/2.0SP2/cassandra/packages/cassandra-3.11.2-1.noarch.rpm
warning: /var/cache/yum/x86_64/2.0SP2/cassandra/packages/cassandra-3.11.2-1.noarch.rpm: Header V4 RSA/SHA256 Signature, key ID fe4b2bda: NOKEY
preinstall scriptlet (using /bin/sh):
getent group cassandra >/dev/null || groupadd -r cassandra
getent passwd cassandra >/dev/null || \
useradd -d /var/lib/cassandra -g cassandra -M -r cassandra
exit 0
postinstall scriptlet (using /bin/sh):
alternatives --install //etc/cassandra/conf cassandra //etc/cassandra/default.conf/ 0
exit 0
preuninstall scriptlet (using /bin/sh):
# only delete alternative on removal, not upgrade
if [ "$1" = "0" ]; then
    alternatives --remove cassandra //etc/cassandra/default.conf/
fi
exit 0

```

## Others
* cassandra
  * https://github.com/karlbohlmark/cassandra-rpm/blob/master/apache-cassandra.spec
  * https://github.com/apache/cassandra-builds
* dhcp
  * https://git.centos.org/blob/rpms!dhcp.git/3f2076a2a871a7866f908b22e38f2a6da8f0651e/SPECS!dhcp.spec
  * https://src.fedoraproject.org/cgit/rpms/dhcp.git/tree/dhcp.spec?id=4a364d130b918caed6d357fd5a1fcc2c35926851
*  kubelet - simple
  * https://github.com/kubernetes/release/blob/master/rpm/kubelet.spec
* cadvisor - simple
  * https://git.centos.org/blob/rpms!cadvisor.git/058502407d0469fbb112b23226a47f15de8068dc/SPECS!cadvisor.spec

# Improvements
* use global variable
* https://www.endpoint.com/blog/2009/08/20/defining-variables-for-rpmbuild
* ```@ xxx @```???TTT
