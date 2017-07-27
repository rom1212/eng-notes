# Huawei Switches - 7800&6800&5800 Series
## Documents
* interface management: http://support.huawei.com/enterprise/en/doc/DOC1000074394
  * Physical Interface Numbering Rules
    * stack ID/subcard ID/interface sequence number, e.g. a physical interface could be represented as 10GE1/0/1, ..., 10GE1/0/48, where 10G is the interface type (which could be 10GE, 40GE)
    * stack ID comes from the number of switches stacking together, and subcard ID is usually 0 for now since it is not supported yet.
* virtualization (stack, SVF): http://support.huawei.com/enterprise/en/doc/DOC1000074401
  * stack: http://support.huawei.com/onlinetoolsweb/virtual/en/dc/dcf/dc_cfg_css_1150.html
    * display stack configuration
    * http://dis-this.com/huawei-ce6800-istack/
    * http://support.huawei.com/onlinetoolsweb/special/switch-p001.html
    * http://support.huawei.com/enterprise/docinforeader!loadDocument1.action?contentId=DOC0000646941&partNo=10012


## Commands
* ? - all available commands
* display ?  - show all the sub-commands
  * display aaa    
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
  * display alarm
    * display alarm active/history/statistics
    * display alarm information - alarm configuration, all kinds of alarm settings
  * display als (automatic laser shutdown, for energy saving)
```
<xxx-xx-xxxx-xx>display als all
--------------------------------------------------------------------------------------
Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s)
--------------------------------------------------------------------------------------
10GE1/0/1          Disable      On             Auto           100           2
10GE1/0/2          Disable      On             Auto           100           2
10GE1/0/3          Disable      On             Auto           100           2
10GE1/0/4          Disable      On             Auto           100           2
10GE1/0/5          Disable      On             Auto           100           2
10GE1/0/6          Disable      On             Auto           100           2
10GE1/0/7          Disable      On             Auto           100           2
10GE1/0/8          Disable      Off            Auto           100           2
10GE1/0/9          Disable      On             Auto           100           2
10GE1/0/10         Disable      On             Auto           100           2
10GE1/0/11         Disable      On             Auto           100           2
10GE1/0/12         Disable      On             Auto           100           2
10GE1/0/13         Disable      On             Auto           100           2
10GE1/0/14         Disable      On             Auto           100           2
10GE1/0/15         Disable      On             Auto           100           2
10GE1/0/16         Disable      On             Auto           100           2
10GE1/0/17         Disable      On             Auto           100           2
10GE1/0/18         Disable      On             Auto           100           2
10GE1/0/19         Disable      On             Auto           100           2
10GE1/0/20         Disable      On             Auto           100           2
...
...
<xxx-xx-xxxx-xx>display als interface 10GE 1/0/1  (interface <interface type> <interface number>
--------------------------------------------------------------------------------------
Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s)
--------------------------------------------------------------------------------------
10GE1/0/1          Disable      On             Auto           100           2
--------------------------------------------------------------------------------------
<xxx-xx-xxxx-xx>display als slot 1
--------------------------------------------------------------------------------------
Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s)
--------------------------------------------------------------------------------------
10GE1/0/1          Disable      On             Auto           100           2
10GE1/0/2          Disable      On             Auto           100           2
10GE1/0/3          Disable      On             Auto           100           2
10GE1/0/4          Disable      On             Auto           100           2
10GE1/0/5          Disable      On             Auto           100           2
<xxx-xx-xxxx-xx>display als slot 2 (slot slot-id)
--------------------------------------------------------------------------------------
Interface          ALS Status   Laser Status   Restart Mode   Interval(s)   Width(s)
--------------------------------------------------------------------------------------
10GE2/0/1          Disable      On             Auto           100           2
10GE2/0/2          Disable      On             Auto           100           2
10GE2/0/3          Disable      On             Auto           100           2
10GE2/0/4          Disable      On             Auto           100           2
10GE2/0/5          Disable      On             Auto           100           2
```
