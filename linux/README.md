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
sudo useradd -m xxx
sudo passwd xxx
# add user xx to "sudo" group, so that it can execute any command. 
# /etc/sudoers is pre-configured to grant permissions to all members of this group (i.e. "sudo" group)
# https://askubuntu.com/questions/7477/how-can-i-add-a-new-user-as-sudoer-using-the-command-line
# ??? take effect next loging ???
sudo adduser xx sudo  
```

## Change Hostname
```
sudo hostname <new name> # take effect immediately
vi /etc/hostname
vi /etc/hosts # for future, and also sudo xxx will have warning about not recognizing the hostname.
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

# Ubuntu

## gdebi - install packages with dependencies
https://askubuntu.com/questions/784656/could-not-find-package-gdebi
```
sudo apt-get install gdebi-core
```
