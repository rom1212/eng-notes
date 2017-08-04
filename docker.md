# docker without sudo
```
# https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
# sudo groupadd docker
sudo gpasswd -a $USER docker
newgrp docker
```

# docker commands
* docker inspec container_id # show all configurations including environment variables
