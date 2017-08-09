# Number of Cores/CPUs/Processors
```
$ lscpu
$ nproc
$ grep processor /proc/cpuinfo
```

# Commands/Tools
## screen
```
$ screen -ls  # list existing screens
$ Ctrl-a d  # detach the screen
$ screen -r <>  # attach to a screen, if there is only one screen, no need to specify the name
```

## Mount Drive from Windows with Readonly Access
```
sudo mkdir /media/xxxx/Acer
sudo mount -t "ntfs" -ro "uhelper=udisks2,nodev,nosuid,uid=1000,gid=1000" "/dev/sda3" "/media/xxxx/Acer"
```

## Add User
```
sudo useradd -m ming
sudo passwd ming
sudo adduser ming sudo
```

## Limit SSH Access
```
# sudo vim /etc/ssh/sshd_config
AllowUsers root xxxx
```

## SSH Keep Alive
https://stackoverflow.com/questions/25084288/keep-ssh-session-alive
```
# .ssh/config, chmod 600 .ssh/config
Host *
ServerAliveInterval 240
```
