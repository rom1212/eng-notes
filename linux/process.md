# Linux Process
## Docs
* man proc: http://man7.org/linux/man-pages/man5/proc.5.html
  * cat /proc/xxx/status
  * cat /proc/[pid]/comm
    * explains that comm can be changed for each thread
    * http://man7.org/linux/man-pages/man2/prctl.2.html, futher explains that change the name is actually change "comm"
  * cat /proc/[pid]/cmdline
## Process Name
* process name is actually the name of the executable, known as "comm"
* it can be shown by
  * ps -o comm -p <pid>
    * shown as COMMAND
  * cat /proc/xxx/status
    * Name: xxx
 

## ps
* process state
  * https://askubuntu.com/questions/360252/what-do-the-stat-column-values-in-ps-mean
  * Sl - sleep multi-threaded
  * Ss - sleep, leader
* parent process, cmd width, start time, elapsed time
  * ps -e -o pid,ppid,stime,etime,cmd:600,etime=
  * can be use if the command is too long to fit into screen
* process tree
  * ps auxf
* Process info
http://man7.org/linux/man-pages/man1/ps.1.html
```
# capital O?
processinfo=`ps -p $pid -O etimes,etime,uid,euser=USER,comm=NAME`
```
