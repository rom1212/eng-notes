# Commands
## Add a word and new line in the end
```
%s/\n/something\r/gc
```

## Add new line before a word
Add new line before each " File" (windows)
```
:%s/ File/\rFile/gc
```

## Format yaml string
Replace \n as a new line. Useful to convert string output of a multi-line string, e.g. yaml.
```
:%s/\\n/\r/gc 

e.g.
"#cloud-config\napt:\n  preserve_sources_list: false\n  primary:\n  - arches: [default]\n    uri: http://archive.ubuntu.com/ubuntu\n "
```

## Format python list
Replace , with new line, useful for formatting list output
```
:%s/, /, \r /gc

e.g.
['iscsi_target_name=iqn.2004-05.com.ubuntu:maas:ephemeral-ubuntu-amd64-generic-xenial-daily', 'iscsi_target_ip=xxx.xx.xx.xx', 'iscsi_target_port=3260', 'iscsi_initiator=caring-eagle', 'ip=::::caring-eagle:BOOTIF']
```
