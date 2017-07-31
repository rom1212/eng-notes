# Huawei Switches - 7800&6800&5800 Series
## Documents
* configuration guide - Ethernet Switching: http://support.huawei.com/enterprise/en/doc/DOC1000074869
  * good introduction about switching
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

## Specifications
* 5800, e.g. CE5855-48T4S2Q-EI: 48 base-T ports (mostly used for server management ports), 4S (4x10GE), 2Q(2x40GE) for uplinks
* 6800, e.g. CE6850U-48S6Q-HI: 48x10GE can be used for app traffic (link to servers), and 6x40GE can be used for uplinks
* 7800, e.g. CE7850-32Q-EI (only one model): 32x40GE mostly for post or spine

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
  * display stack
  ```
  <xxx-xx-xxxx-xx>display stack  (aggregate info from: display stack member n)
--------------------------------------------------------------------------------
MemberID Role     MAC              Priority   DeviceType         Description
--------------------------------------------------------------------------------
+1       Master   xxxx-xxxx-xxxx   150        CE6850U-48S6Q-HI
 2       Standby  xxxx-xxxx-xxxx   150        CE6850U-48S6Q-HI
--------------------------------------------------------------------------------
+ indicates the device through which the user logs in.
# get switch model information here :-)
<xxx-xx-xxxx-xx>display stack topology
Stack Topology:
----------------------------------------------
            Stack-Port 1      Stack-Port 2
MemberID   Status Neighbor   Status Neighbor
----------------------------------------------
1          up     2          --     --
2          up     1          --     --
----------------------------------------------

Stack Link:
----------------------------------------------------------------------------
Stack-Port       Port               Status     PeerPort           PeerStatus
----------------------------------------------------------------------------
Stack-Port1/1    40GE1/0/5          up         40GE2/0/5          up
Stack-Port1/1    40GE1/0/6          up         40GE2/0/6          up
Stack-Port2/1    40GE2/0/5          up         40GE1/0/5          up
Stack-Port2/1    40GE2/0/6          up         40GE1/0/6          up
----------------------------------------------------------------------------
# each switch uses 2 40GE ports to peer with the other one.
```
  * display arp
```
<xxxx>display arp
ARP Entry Types: D - Dynamic, S - Static, I - Interface
EXP: Expire-time

IP ADDRESS      MAC ADDRESS    EXP(M) TYPE/VLAN INTERFACE       VPN-INSTANCE
------------------------------------------------------------------------------
172.xx.xx.xx    xxxx-xxxx-xxxx        I         MEth0/0/0
172.xx.xxx.253  xxxx-xxxx-xxxx   11   D         MEth0/0/0
172.xx.xxx.254  xxxx-xxxx-xxxx   11   D         MEth0/0/0
172.xx.xx.211   xxxx-xxxx-xxxx        I         Vlanif401m
172.xx.xx.254   xxxx-xxxx-xxxx        I         Vlanif401n
172.xx.xx.12    xxxx-xxxx-xxxx    7   D/401n    10GE1/0/12
------------------------------------------------------------------------------
Total:9         Dynamic:6       Static:0    Interface:3
# for comparison, linux arp output
~# arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.xx.xx.1              ether   xx:xx:xx:xx:xx:xx   C                     eth0
10.xx.xx.2              ether   xx:xx:xx:xx:xx:xx   C                     eth0
10.xx.xx.3              ether   xx:xx:xx:xx:xx:xx   C                     eth0
```
  * display current-configuration
```
<xxx-xx-xxxx-xx>display current-configuration
!Software Version V100R005C10SPC200
!Last configuration was updated at 2017-xx-xx 09:40:03+00:00 by SYSTEM automatically
!Last configuration was saved at 2017-xx-xx 08:53:14+00:00 by xxx
#
sysname xxx-xx-xxxx-xx
#
FTP server enable
#
device board 1 board-type CE6850U-48S6Q-HI
device board 2 board-type CE6850U-48S6Q-HI
#
drop-profile default
#
dcb pfc
#
dcb ets-profile default
#
vlan batch 401x 401x
#
telnet ipv6 server disable
#
diffserv domain default
...
...
```
