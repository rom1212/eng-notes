# Huawei Switch
## Commands
* ? - all available commands
* display ?  - show all the sub-commands
  * display aaa xxx    
```
  <xxx-xxx-xx>display aaa domain
---------------------------------------------------------------------
Domain-name                              State  Access-limit   Online
---------------------------------------------------------------------
default                                  Active           --        0
default_admin                            Active           --        2
---------------------------------------------------------------------
<xxx-xx-xx>display aaa local-user
Type: F - Ftp, T - Telnet, M - Terminal, S - Ssh, N - Snmp, X - Dot1x
---------------------------------------------------------------------------------------------------
Username                         State   Type   Access-limit   Online   Admin-level   User-group-id
---------------------------------------------------------------------------------------------------
switch                           Active  T                --        2             3              --
admin123                         Active  F                --        0             3              --
---------------------------------------------------------------------------------------------------
<xxx-xx-xxxx-xx>display aaa offline-record
-----------------------------------------------------
Offline record switch          : Enable
-----------------------------------------------------
User name                      : switch
Domain name                    : default_admin
User access type               : Telnet
User IP address                : 192.168.xx.xxx
User ID                        : 59
User authen state              : Success
User author state              : Success
User login time                : 2017-07-28 01:55:40
User offline time              : 2017-07-28 02:15:33
User offline reason            : Idle timeout
<xxx-xx-xxxx-xx>display aaa task
--------------------------------------------
Task-name                            Task-id
--------------------------------------------
ospf                                       1
rip                                        2
ripng                                      3
ntp                                        4
key-chain                                  5
patch                                      6
rpm                                        7
bgp                                        8
tunnel                                    10
igmp                                      11
...
...
<xxx-xx-xxxx-xx>display aaa task-group
------------------------------------------------------
Task-group-name                          Task-group-id
------------------------------------------------------
manage-tg                                            1
system-tg                                            2
monitor-tg                                           3
visit-tg                                             4
------------------------------------------------------
Total 4, 4 printed
<xxx-xx-xxxx-xx>display aaa user-group
------------------------------------------------------
User-group-name                          User-group-id
------------------------------------------------------
manage-ug                                            1
system-ug                                            2
monitor-ug                                           3
visit-ug                                             4
------------------------------------------------------
Total 4, 4 printed
```
