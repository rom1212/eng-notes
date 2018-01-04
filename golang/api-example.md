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

## Add main.go and MySQL support
Bee v1.9.1 only generate routers/, controllers/ and models/. We need to write main.go ourselves. Here is an example:
```
// main.go
package main

import (
        _ "cmdb-api/routers"

        "github.com/astaxie/beego"
        "github.com/astaxie/beego/orm"
        _ "github.com/go-sql-driver/mysql"
        "time"
)

func init() {
        orm.RegisterDriver("mysql", orm.DRMySQL)
        // set default database
        orm.RegisterDataBase("default", "mysql", "root:mypass@/mydbname?charset=utf8", 30)
        // Set to UTC time
        orm.DefaultTimeLoc = time.UTC
}

func main() {
        if beego.BConfig.RunMode == "dev" {
                beego.BConfig.WebConfig.DirectoryIndex = true
                beego.BConfig.WebConfig.StaticDir["/swagger"] = "swagger"
        }
        beego.Run()
}
```
Now, ```bee run``` can start the app, and we can access the API through localhost:8080/v1/<table name/resource name>

## Generate Swagger Spec and UI
```
$ bee run -downdoc=true -gendoc=true

# Then the swagger UI is accessible at: http://localhost:8080/swagger/
```
