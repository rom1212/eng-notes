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
## Write a Test
```
vue init webpack my-project  # pay attention to the output information on how to do next
cd my-project
npm install # takes a long time for pulling all the depenendcies
npm run dev # add --host 0.0.0.0 to webpack-dev-server in package.json if want external access

# test
sudo apt-get install libfontconfig
npm run unit

# Add a test with src/components/List.vue and test/unit/List.spec.js
npm run unit

# next Similating User Input
```
## Problem with localhost
* If we also want other hosts to access the dev server, we need to expose it to 0.0.0.0
* open package.json
* under "scripts"
  * "dev" is invoked when running "npm run dev"
  * add  --host 0.0.0.0 to webpack-dev-server command
  
# Learning Log
* session #1 - about 2'45''
  * install npm
  * read vuejs basic
  * follow example to run vue init, solve problem of external access for webpack-dev-server
  * add one simple test, and test pass
