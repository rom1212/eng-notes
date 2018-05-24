# Commands
## ps
* ps auxf - process tree
* ps alx - PPID
* ps -f -p <pid> # PPID
* http://man7.org/linux/man-pages/man1/ps.1.html
```
# capital O
processinfo=`ps -O etimes,etime,uid,euser=USER,comm=NAME -p $pid`
```

## sed
* remove trailing spaces
```bash
sed -i 's/[ \t]*$//' <filename, or *>

# remove trailing whitespace
function remove-trailing-whitespace() {
  sed -i 's/[ \t]*$//' $1
}
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
TTT???: is there a case that there are multiple processes with the same port? I guess not.
```
pid=`lsof -i:"<PORT>" -t`
```

```
# check whether we can find the process or not, otherwise kill will fail because no argument is given
if lsof -i tcp:3303; then
    lsof -i tcp:3303 | awk 'NR!=1 {print $2}' | xargs kill
    # or lsof -i tcp:3303 -t | xargs kill
fi

lsof -i tcp:${PORT_NUMBER} | awk 'NR!=1 {print $2}' | xargs kill
```

A port is taken or not
* netstat -tap
  * all tcp ports
* netstat -tlpn
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
If a port is know, it is easier to use lsof to find out the process id, instead of parsing netstat output. However, netstat is usually already installed, but lsof is not.

## chmod
Add read permission for all files and directories recursively. pay attention to capital "X".
```bash
sudo chmod a+rX -R .
```

## rsync
For more safety, use git to keep the history of dst (and src).
```bash
git init
git add .
git commit -am "first commit"
```
If git cost too much space, we can use a simple file to record all the file names and sizes
```
 find . -type f -printf '%P, size(b): %s\n'
 ```

This is the most safe way to do it. It will not overwrite any file that exist on the destination.
```bash
# show progress, ignore existing file/no overwrite, recursive, verbose
rsync -r -v --progress --ignore-existing --dry-run family-media-src/ family-media-dst/
```

Might consider --size-only if we want to copy fils with different size. However, it might be dangerous
if you want to copy something to src that is missing in the source.
```bash
rsync -r -v --progress --size-only --dry-run family-media-src/ family-media-dst/
```

For reference, for archive everything 
```
rsync -ra --progress --dry-run family-media-src/ family-media-dst/
```

## ls timestamp millisecond
```
ls -la --time-style=full-iso blah
```

## command, hash, type
* https://stackoverflow.com/questions/592620/check-if-a-program-exists-from-a-bash-script
* hash: no output if the command is already there/exists.

## run as another user
* su - need password for the target user that will ran as.
  * it is not "super user", it is "substitute user"
  * ```su - user``` will make it more like a real shell with environment variables, e.g.g HOME, and go to home directory, while ```su user``` just change to the other user.
* runuser
* sudo - much much secure - need password for the user of running sudo.
* https://www.cyberciti.biz/open-source/command-line-hacks/linux-run-command-as-different-user/

## sudo, /etc/sudoers
* /etc/sudoers and /etc/suoders.d/ are used to configure sudo command.
```
# syntax
<username or %groupname> <host>=[(<user that can be run as with -u option>[:<group that can be run as with -g option>)]] [NOPASSWD:|PASSWD:] <commands or ALL>

# root on Ubuntu a root user: can run on all hosts, run as any user, run as any group, run all commands 
root ALL=(ALL:ALL) ALL
# it's fine to run this command
sudo -u tt1 ls

# root user on CentOs
root    ALL=(ALL) ALL
# sudo -g tt1 ls /
# Sorry, user root is not allowed to execute '/bin/ls /' as root:tt1 on <host name>.

# cannot run as another user/group
<username> ALL= NOPASSWD: ALL, PASSWD: /usr/bin/su, PASSWD: /usr/sbin/runuser

sudo -u tt1 ls
[sudo] password for <currrent user>:
sudo -g tt1 ls
[sudo] password for <currrent user>:
```
 
* docs
  * https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file-on-ubuntu-and-centos

## umask
umask is the reverse side of permission bits, and so 022 corresponds to ```rxwr-xr-x```, and 077 corresponds to ```rwx------```.
* the default is first setup in /etc/login.defs
  *  ubuntu: 
  ```
  # Prefix these values with "0" to get octal, "0x" to get hexadecimal.
  UMASK           022
  ```
  * CentOS
  ```
  # The permission mask is initialized to this value. If not specified, 
  # the permission mask will be initialized to 022.
  UMASK           077
  ```
  * seems that if it not specified in /etc/logins.defs, and any where else it is 022.
* other places
  * /etc/profile (interactive only)
  * /etc/bashrc (interactive and non-interactive). subprocess is non-interactive.
  * http://bencane.com/2013/09/16/understanding-a-little-more-about-etcprofile-and-etcbashrc/
* problem related to umask is pip install virtualenv
  * please see https://github.com/rom1212/eng-notes/blob/master/python/README.md#virtualenv

# Tools
## Meld
* http://meldmerge.org/
* Can be setup as git diff
