# Commands

## sed
* remove trailing spaces
```
sed -i 's/[ \t]*$//' <filename, or *>
```

## Number of Cores/CPUs/Processors
```
$ lscpu
$ nproc
$ grep processor /proc/cpuinfo
```

## grep
* invert match: grep -v

## find
* find all *.sh files and show detailed information
  * ```-maxdepth 1``` means no recursive, only show files under /home/username
  * ```-mtime +8``` means more than 9 days ago. +0 means more than one data ago
  * ```-mmin +1``` means more than 2 minutes ago.
```
/usr/bin/find /home/username -maxdepth 1 -name "*.sh" -type f -mtime +8 -exec ls -lh {} \;
```
* find all *.sh files and delete them
```
/usr/bin/find /home/username -maxdepth 1 -name "*.sh" -type f -mtime +8 -delete
```

## Process with a given port
```
pid=`lsof -i:"<PORT>" -t`
```
```
lsof -i tcp:${PORT_NUMBER} | awk 'NR!=1 {print $2}' | xargs kill
```

## A port is taken or not
* netstat -tap
  * all tcp ports
* netstat -tlnp
  * -t : tcp
  * -l : listening only
  * -n : numeric
  * -p : process id and program
```
function taken {
  if netstat -tlnp | grep ":$@" >/dev/null 2>&1; then
    true
  else
    false
  fi
```
If a port is know, it is easier to use lsof to find out the process id, instead of parsing netstat output.

# Tools
## Meld
* http://meldmerge.org/
* Can be setup as git diff
