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
sudo mkdir /media/ming/Acer
sudo mount -t "ntfs" -ro "uhelper=udisks2,nodev,nosuid,uid=1000,gid=1000" "/dev/sda3" "/media/ming/Acer"
```
