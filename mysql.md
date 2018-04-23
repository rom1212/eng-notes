# Install
## Install on CentOS
* https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-centos-7
* Get password from log: ```sudo grep 'temporary password' /var/log/mysqld.log```
* To turn off password validation: ```mysql> uninstall plugin validate_password;```
## Install mysql-workbench
```bash
# ubuntu 16.04
sudo apt install mysql-workbench
```

# CLI Tools
## mysql client
```bash
# simple command, default is localhost:3306
mysql -u root -p

# command with more options
mysql -u root -p --host localhost --port 3306

# command with password, database and query
MYSQL_PWD=${PWD} mysql --user="root" --connect-expired-password --database='cible' --execute="SELECT DISTINCT User FROM mysql.user;"

mysql --user="root" --password=i2test --connect-expired-password --database='cible' --execute="SELECT DISTINCT User FROM mysql.user;"
```

## Add User
```
create user 'dev'@'%' identified by 'test';
grant all privileges on *.* to 'dev'@'%' WITH GRANT OPTION;
flush privileges;
```

## Backup
https://www.liquidweb.com/kb/how-to-back-up-mysql-databases-from-the-command-line/
* mysqldump

# Schema
## Drop User
```
DROP USER IF EXISTS test
```

## Show table schema
```
show create table <table name, e.g. agents>;
```
## Update primary key
https://stackoverflow.com/questions/2341576/updating-mysql-primary-key
```
alter table xx drop primary key, add primary key(k1, k2, k3);
e.g.
alter table agents drop primary key, add primary key(host_id, env_id, deploy_id);
```
## Add column
```
ALTER TABLE table_name ADD COLUMN column_name column_type;
e.g.
ALTER TABLE deploys ADD COLUMN error_message   VARCHAR(2048);
```

## Add Unique Constraint
* CONSTRAINT and UNIQUE INDEX are the same, because
  * "A UNIQUE index creates a constraint such that all values in the index must be distinct"
  * https://dba.stackexchange.com/questions/63211/what-is-the-difference-between-uniqe-index-unique-unique-key-unique-constraint-k/63280
  ```
  unique index query_md5_index (query_md5)
  unique query_md5_index (query_md5)
  constraint md5_constraint unique (query_md5)
  unique key query_md5_key (query_md5)
  ```
* INDEX and KEY are the same
  * https://dev.mysql.com/doc/refman/8.0/en/create-table.html
  * https://www.quora.com/What-is-the-difference-between-using-KEY-and-INDEX-in-MySQL


# HA 
## docs
* https://dev.mysql.com/doc/refman/5.7/en/mysql-innodb-cluster-introduction.html
* https://dev.mysql.com/doc/refman/5.7/en/group-replication.html
* http://mysqlhighavailability.com/category/replication/group-replication/
* https://dev.mysql.com/doc/relnotes/mysql/5.7/en/news-5-7-17.html
* https://dev.mysql.com/doc/refman/5.7/en/group-replication-limitations.html
* https://dev.mysql.com/doc/refman/5.7/en/mysql-innodb-cluster-limitations.html

# Notes
```
=== uninstall on ubuntu 16.04 ===
apt-get remove mysql-*
apt-get purge mysql-*  # this one probably remove the following files already
rm -rf  /var/lib/mysql
rm -rf /etc/mysql/
rm -rf /var/lib/mysql-files/
rm -rf /var/lib/mysql-keyring/
rm -rf /var/log/mysql

=== install on ubuntu 16.04 ===
apt-get install  mysql-server # set root password, and also mysqld is already running. old version can use mysql-server-5.7 
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

# turn off password validation
mysql> uninstall plugin validate_password;

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
