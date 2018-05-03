# Daemon
## What makes a daemon
```
I can't copy the list verbatim because of copyright (see the About section), but here's the summary:

    fork (first time) -- so we aren't a group leader, and let the parent exit.
    call setsid() -- to become leader of a new session. This call only works if we are not a group leader. This new session has no controlling terminal.
    fork (second time) -- so we aren't a session leader (and thus can't regain a controlling terminal), and let the parent exit.
    cd to root directory -- so we don't prevent other directories from being umount-ed.
    set umask to desired value (optional) -- because we could've inherited a mask we didn't want.
    close stdin, stdout, stderr (or just reopen them to point elsewhere)
```
See
* https://stackoverflow.com/questions/958249/whats-the-difference-between-nohup-and-a-daemon

## DenyHosts
*  Use double fork
  * /etc/rc.d/init.d/denyhosts: ```/usr/bin/denyhosts.py --daemon xxx```
    * /usr/bin/denyhosts.py: ```dh = DenyHosts(f, prefs, lock_file, ignore_offset, first_time, noemail, daemon)```
      * /usr/lib/python2.7/site-packages/DenyHosts/deny_hosts.py: 
        ```
        retCode = createDaemon()
        self.runDaemon(logfile, last_offset)
        ```
        * https://github.com/denyhosts/denyhosts/blob/master/DenyHosts/daemon.py
          * double fork
