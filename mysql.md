# mysql client
```
# simple command, default is localhost:3306
mysql -u root -p

# command with more options
mysql -u root -p --host localhost --port 3306
```

# Notes
```
=== uninstall on ubuntu 16.04 ===
apt-get remove mysql-*
apt-get purge mysql-*  # this one probably remove the following files already
294  rm -rf  /var/lib/mysql
296  rm -rf /etc/mysql/
306  rm -rf /var/lib/mysql-files/
307  rm -rf /var/lib/mysql-keyring/
rm -rf /var/log/mysql

=== install on ubuntu 16.04 ===
apt-get install  mysql-server-5.7 # set root password, and also mysqld is already running.
mysql_secure_installation # make it more secure by removing test accout and user 

enable remote acces: 
comment out this in file: /etc/mysql/mysql.conf.d/mysqld.cnf
# bind-address          = 127.0.0.1

root@dev-12:/home/switch# netstat -tap | grep mysql
tcp       0      0 localhost:mysql              *:*                  LISTEN      42752/mysqld

systemctl restart mysql

# this mean it is listening to remote access, [localhost]:mysql means local only
root@dev-12:/home/switch# netstat -tap | grep mysql
tcp6       0      0 [::]:mysql              [::]:*                  LISTEN      42752/mysqld

=== manage mysql with systemd ===
https://dev.mysql.com/doc/refman/5.7/en/using-systemd.html

=== add user ===
mysql -u root -p 
add users:
	mysql> create user 'dev'@'%' identified by 'test';
	mysql> grant all privileges on *.* to 'dev'@'%';
	mysql> create user 'ro'@'%' identified by 'pass';
	mysql> grant select on *.* to 'ro'@'%';
	mysql> flush privileges;

verify from another host to make sure that users can access database remotely
mysql -h <xxx.xx.48.2> -u root -p


=== mysql client ===
mysql -u root -p 
# change dynamic system variables
https://dev.mysql.com/doc/refman/5.7/en/using-system-variables.html
mysql> set global net_read_timeout = 600; # might need to exit and enter again to see changed.
mysql> show variables like 'net_read_timeout';
mysql> show databases;
mysql> use xxup;
mysql> show tables;
mysql> select count(*) from t0526a;

innodb_buffer_pool_size and other variables

=== mysqladmin ===
mysqladmin -u root -p<pass> status proc(esslist)
mysqladmin -u root -p status # prompt for password.

http://www.thegeekstuff.com/2009/01/15-practical-usages-of-mysqladmin-command-for-administering-mysql-server/
https://dev.mysql.com/doc/refman/5.7/en/mysqladmin.html

# dev-12 installed on 2017-05-27T04:13:37.505833Z 


 ====
mysqldiskusage --server dev:test@localhost --all -vv

mysql-connector-python .deb package
https://dev.mysql.com/downloads/connector/python/

mysql-utilities: https://downloads.mysql.com/archives/utilities/


"mysql lost connection during query":
* big data problem, change 'net_read_timeout'

```
