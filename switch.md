# Huawei Switch
## Commands
* ? - all available commands
* display ?  - show all the sub-commands
  * display aaa domain  
  * display aaa local-user
  
  ```
  <xxx-xxx-xx>display aaa domain
---------------------------------------------------------------------
Domain-name                              State  Access-limit   Online
---------------------------------------------------------------------
default                                  Active           --        0
default_admin                            Active           --        2
---------------------------------------------------------------------
  ```

```
<xxx-xx-xx>display aaa local-user
Type: F - Ftp, T - Telnet, M - Terminal, S - Ssh, N - Snmp, X - Dot1x
---------------------------------------------------------------------------------------------------
Username                         State   Type   Access-limit   Online   Admin-level   User-group-id
---------------------------------------------------------------------------------------------------
switch                           Active  T                --        2             3              --
admin123                         Active  F                --        0             3              --
---------------------------------------------------------------------------------------------------
```
