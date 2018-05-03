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
