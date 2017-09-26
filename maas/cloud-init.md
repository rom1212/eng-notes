# cloud-init

## docs
http://www.whiteboardcoder.com/2016/04/install-cloud-init-on-ubuntu-and-use.html

## Install
```
$ sudo apt install cloud-init   # ubuntu 16.04
The following NEW packages will be installed:
  cloud-guest-utils cloud-init eatmydata libeatmydata1 python3-configobj python3-json-pointer python3-jsonpatch python3-prettytable
  python3-serial python3-yaml
```

## Package Content
```
apt-get install --reinstall --print-uris -qq cloud-init
wget http://us.archive.ubuntu.com/ubuntu/pool/main/c/cloud-init/cloud-init_0.7.9-233-ge586fe35-0ubuntu1~16.04.1_all.deb
dpkg -x cloud-init_0.7.9-233-ge586fe35-0ubuntu1~16.04.1_all.deb cloud-init/
```


