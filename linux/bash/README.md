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
