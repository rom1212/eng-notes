# Commands
## Add new line
Add new line before each " File" (windows)
```
:%s/ File/\rFile/gc
```

## Replace \n as a new line
Useful to convert string output of a multi-line string 
```
:%s/\\n/\r/gc 

e.g.

```

## Format python list
Replace , with new line
```
:%s/, /, \r /gc

e.g.
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily', 'iscsi_target_ip=xxx.xx.xx.xx', 'iscsi_target_port=3260', 'iscsi_initiator=caring-eagle', 'ip=::::caring-eagle:BOOTIF']
```
