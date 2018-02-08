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
