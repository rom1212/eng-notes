# Daemon
## DenyHosts
*  Use double fork
  * /etc/rc.d/init.d/denyhosts: ```/usr/bin/denyhosts.py --daemon xxx```
    * /usr/bin/denyhosts.py: ```dh = DenyHosts(f, prefs, lock_file, ignore_offset, first_time, noemail, daemon)```
      * /usr/lib/python2.7/site-packages/DenyHosts/deny_hosts.py: ```retCode = createDaemon(); self.runDaemon(logfile, last_offset)```
        * https://github.com/denyhosts/denyhosts/blob/master/DenyHosts/daemon.py
          * double fork
