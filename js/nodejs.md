# Install npm and node
## Install npm on Ubuntu 16.04
Use PPA
```
curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt-get install nodejs
~# node -v
v6.11.1
~# nodejs -v 
v6.11.1
~# npm -v
5.3.0
~# which node
/usr/bin/node
~# which nodejs
/usr/bin/nodejs
~# ll /usr/bin/node
lrwxrwxrwx 1 root root 22 Jul 18 12:50 /usr/bin/node -> /etc/alternatives/node*
~# ll /etc/alternatives/node 
lrwxrwxrwx 1 root root 15 Jul 18 12:50 /etc/alternatives/node -> /usr/bin/nodejs*
```

Default Ubuntu Repository
```
~$ sudo apt install npm
~$ npm --version
3.5.2
~$ nodejs --version
v4.2.6
```

## Install a special version of node
```
sudo npm install -g n
sudo n 4.4.1
```

## Install a special version of npm
```diff
- # install a special version of node first. Otherwise, it might override npm version
sudo npm install -g npm@3.9.1
```

## Install package Globally
```
# need sudo
sudo npm install -g oas-raml-converter
```
If this problem happens:
```
$ oas-raml-converter --from RAML10 --to OAS api.raml 
/usr/bin/env: ‘node --harmony’: No such file or directory
```
Then, change first line of oas-raml-converter
```
sudo vim /usr/local/bin/oas-raml-converter
#!/usr/bin/node --harmony
```
