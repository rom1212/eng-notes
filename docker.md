# Docker without sudo
```
# https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
# sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```

# Docker commands
* docker inspec container_id # show all configurations including environment variables

# Install
## docker-engine 1.11 from deb files
```
git clone kubeadm-packages/ubuntu-16.04
sudo apt install ./auftxxx ./cgroupxxx ./docker-enginexxx

# To create those packages
git clone kubeadm-flannel-light
sudo ./install.sh
find packages in /var/cache/apt/*
```
