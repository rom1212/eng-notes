## Vlan
## Create Interface without vlan
Just this is fine. No need extra parameters. Whether it is up or not depends on it is connected with other devices.
```
#
interface 10GE1/0/1
```

## VID 1
VID 1 is defined **by default** for all ports with untagged (UT), i.e. each port will accept traffic for VID 1 (i.e. the default VID), and remove the tag (i.e. untag) and send out of the port, e.g.
```
<xxxxxx>display vlan
The total number of vlans is : 2
--------------------------------------------------------------------------------
U: Up;         D: Down;         TG: Tagged;         UT: Untagged;
MP: Vlan-mapping;               ST: Vlan-stacking;
#: ProtocolTransparent-vlan;    *: Management-vlan;
MAC-LRN: MAC-address learning;  STAT: Statistic;
BC: Broadcast; MC: Multicast;   UC: Unknown-unicast;
FWD: Forward;  DSD: Discard;
--------------------------------------------------------------------------------

VID          Ports
--------------------------------------------------------------------------------
   1         UT:40GE1/0/1(D)    40GE1/0/2(D)    10GE1/0/1(D)    10GE1/0/2(D)
                10GE1/0/3(D)    10GE1/0/4(D)    GE1/0/1(U)      GE1/0/2(U)
                GE1/0/3(U)      GE1/0/4(U)      GE1/0/5(U)      GE1/0/6(U)
                GE1/0/7(U)      GE1/0/8(U)      GE1/0/9(U)      GE1/0/10(U)
                GE1/0/11(U)     GE1/0/12(U)     GE1/0/13(D)     GE1/0/14(D)
                GE1/0/15(D)     GE1/0/16(D)     GE1/0/17(D)     GE1/0/18(D)
                GE1/0/19(D)     GE1/0/20(D)     GE1/0/21(D)     GE1/0/22(D)
                GE1/0/23(D)     GE1/0/24(D)     GE1/0/25(D)     GE1/0/26(D)
                GE1/0/27(D)     GE1/0/28(D)     GE1/0/29(D)     GE1/0/30(D)
                GE1/0/31(D)     GE1/0/32(D)     GE1/0/33(D)     GE1/0/34(D)
                GE1/0/35(D)     GE1/0/36(D)     GE1/0/37(D)     GE1/0/38(D)
                GE1/0/39(D)     GE1/0/40(D)     GE1/0/41(D)     GE1/0/42(D)
                GE1/0/43(D)     GE1/0/48(U)
```
