# Bash
## bash file dir
```
DIR="$( dirname ${BASH_SOURCE[0]} )"
```

## Useful Snippets
* File Exists
```
if [ ! -f /tmp/foo.txt ]; then
    echo "File not found!"
fi
```

## Loop
```
#!/bin/bash
for number in 1 2 3 4 5
do
echo $number
done
```
## Misc
```
DATE=`date '+%Y-%m-%dT%H:%M:%S'`
```

## default value
https://stackoverflow.com/questions/2013547/assigning-default-values-to-shell-variables-with-a-single-command-in-bash
```
FOO=${VARIABLE:-default}  # If variable not set or null, use default.
Or, which will assign default to VARIABLE as well:

FOO=${VARIABLE:=default}  # If variable not set or null, set it to default.
```
