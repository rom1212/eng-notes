# Linux Process
## Docs
* man proc: http://man7.org/linux/man-pages/man5/proc.5.html
  * cat /proc/xxx/status
* 
## Process Name
* process name is actually the name of the executable, known as "comm"
* it can be shown by
  * ps -o comm -p <pid>
    * shown as COMMAND
  * cat /proc/xxx/status
    * Name: xxx
 
