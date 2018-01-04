# Create Database Schema
Use MySQL as example.
```
# xxx.sql (exported by MySQL Workbench 6.3)
$ sudo apt intall mysql-server
$ mysql -u root -p
mysql> source xxx.sql;
```

# Generate API using Bee
## Install bee
```
go get github.com/beego/bee
```

## Generate API Code from MySQL Tables
```
$ mkdir ~/go/src/xxx-api
$ cd ~/go/src/xxx-api
$ bee generate appcode -driver=mysql -conn="root:mypass@tcp(127.0.0.1:3306)/<my db name>" -level=3
```

