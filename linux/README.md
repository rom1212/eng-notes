
# Commands/Tools
## Long Running Process
```
nohup node server.js &
```

## Screen
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
Ubuntu 16.04
```
sudo useradd -m xxx
sudo passwd xxx
# add user xx to "sudo" group, so that it can execute any command. 
# /etc/sudoers is pre-configured to grant permissions to all members of this group (i.e. "sudo" group)
# https://askubuntu.com/questions/7477/how-can-i-add-a-new-user-as-sudoer-using-the-command-line
# ??? take effect next loging ???
sudo adduser xxx sudo

# Change the default shell, e.g. /bin/bash, check the value by $SHELL
sudo chsh <user name> 
Enter the new value, or press ENTER for the default
        Login Shell []: /bin/bash
        
# sudo vim /etc/sudoers, add the following line at the end of it.
# execute command without password: https://askubuntu.com/questions/147241/execute-sudo-without-password
username ALL=(ALL) NOPASSWD: ALL
```
CentOS: useradd and adduser are the same
```
sudo useradd -m xxx
sudo passwd xxx
usermod -aG wheel username  # no sudo group here
```

## Change Hostname
```
sudo hostname <new name> # take effect immediately
vi /etc/hostname
vi /etc/hosts # for future, and also sudo xxx will have warning about not recognizing the hostname.
127.0.0.1       localhost
127.0.1.1       <host name>

```

## Limit SSH Access
```
# sudo vim /etc/ssh/sshd_config
AllowUsers root xxxx

# sudo systemctl restart ssh
```

## SSH Connection Reset
* When ssh client see this error
```
$ ssh username@xx.xx.xx.xx
ssh_exchange_identification: read: Connection reset by peer
```
* Check server sshd log
Run
```
# on CentOS
systemctl status sshd or vi /var/log/secure

# See this error

refused connect from xx.xx.xx.xx (xx.xx.xx.xx)
```
* vi /etc/hosts.deny, /etc/hosts.allow
```
clean up /etc/hosts.deny
```
* a better way
```
sudo su
systemctl stop denyhosts
sed -i '/192.168/d' /var/lib/denyhosts/* /etc/hosts.deny
systemctl start denyhosts
exit
```

## SSH Keep Alive
https://stackoverflow.com/questions/25084288/keep-ssh-session-alive
```
# .ssh/config, chmod 600 .ssh/config
Host *
ServerAliveInterval 240
```

## Who login/history
```
last [-10]
```

# Ubuntu

## gdebi - install packages with dependencies
https://askubuntu.com/questions/784656/could-not-find-package-gdebi
```
sudo apt-get install gdebi-core
```
