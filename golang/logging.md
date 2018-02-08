# glog rotation
## logrotate
* Difficulties
  * glog creates new log file when size grows bigger than MaxSize
  * We need a way to clean up old files.  
  * We need a way to include only glog files 
  * We need a way not remove currently logged files.
    * by time: current logged file could be very long time ago.
    * by size: current logger file could be very big - by we can change MaxSize, e.g. 100M. So, we only do rotation when file size
    is bigger than 100M.
  * Most challenging is: small log files which is created for a long time.
  * olddir, maxage, copy 
* simple solution
  * set a small MaxSize, e.g. 10M, and set logrotate maxage to be 1 day. and "rotate 0", which basically deletes files that are created 1 day ago.

## glogrotate
https://github.com/realzeitmedia/glogrotate

## lumberjack
* https://github.com/natefinch/lumberjack
* https://gist.github.com/jasonlollback/f395512056699fab8fc1