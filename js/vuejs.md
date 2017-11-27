# Docs
* https://vuejs.org/v2/guide/

# Install on Ubuntu 16.04
## Install nodejs and npm
* https://github.com/vuejs/vue-cli
```
$ curl -sL https://deb.nodesource.com/setup_6.x -o nodesource_setup.sh
$ sudo bash nodesource_setup.sh
$ sudo apt-get install nodejs
$ node -v
v6.12.0
$ npm -v
3.10.10
sudo npm install -g vue-cli
```

# Run webpack server

## Docs
* https://github.com/vuejs/vue-cli
* https://scotch.io/tutorials/how-to-write-a-unit-test-for-vuejs
## Commands
```
vue init webpack my-project  # pay attention to the output information on how to do next
cd my-project
npm install # takes a long time for pulling all the depenendcies
npm run dev
```
## Problem with localhost
* open package.json
* under "scripts"
  * "dev" is invoked when running "npm run dev"
  * add  --host 0.0.0.0 to webpack-dev-server command
