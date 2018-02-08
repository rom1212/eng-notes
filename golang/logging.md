# glog
## logrotate
* Difficulties
  * glog creates new log file when size grows bigger than MaxSize
  * We need a way to clean up old files.  
  * We need a way to include only glog files 
  * We need a way not remove currently logged files.
    * by time: current logged file could be very long time ago.
    * by size: current logger file could be very big - by we can change MaxSize, e.g. 100M. So, we only do rotation when file size is bigger than 100M. 
* olddir, maxage, copy 
* only
