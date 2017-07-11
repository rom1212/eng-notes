# mesos-guide

## Setup
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv E56151BF
DISTRO=$(lsb_release -is | tr '[:upper:]' '[:lower:]')
CODENAME=$(lsb_release -cs)
```

## Add the repository
```
echo "deb http://repos.mesosphere.com/${DISTRO} ${CODENAME} main" | \
sudo tee /etc/apt/sources.list.d/mesosphere.list
sudo apt-get -y update
```

## Install mesos and marathon
```
sudo apt-get -y install mesos marathon
```

## start mesos master
```
sudo /usr/sbin/mesos-master --ip=127.0.0.1 --work_dir=/tmp/
```
After mesos master is up, you can go to the web UI: http://localhost:5050

## start mesos agent
```
sudo /usr/sbin/mesos-agent --master=127.0.0.1:5050 --work_dir=/tmp/
```

## start marathon - marathon needs zookeeper even if we don't specify (it will use a default one)
```
sudo /usr/bin/marathon --master=localhost:5050
```
After marathon is up, you can go to the web UI: http://localhost:8080

## Problem with Zookeeper on Ubuntu 16.04
If you couldn't find the zookeeper process, e.g. ps aux | grep zookeeper doesn't show the zookeeper process. Try this:
```
sudo su
apt-get remove openjdk-9-jre-headless
echo server.1=$(hostname):2888:3888 >> /etc/zookeeper/conf/zoo.cfg
```
