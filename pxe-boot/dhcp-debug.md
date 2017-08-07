# dhcpdump
```
xxx@xxx:~$ sudo dhcpdump -i enp129s0f0  -h ^48:d5:39:xx:xx
# 48:d5:39:xx:xx:aa is the machine that powered on.
# 2c:9d:1e:xx:xx:xx is the machine with dhcpd and serves dhcp requests.

  TIME: 2017-08-08 01:22:39.798
    IP: 0.0.0.0 (48:d5:39:xx:xx:aa) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 1 (BOOTPREQUEST)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: 394418d7
  SECS: 8
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: 0.0.0.0
SIADDR: 0.0.0.0
GIADDR: 0.0.0.0
CHADDR: 48:d5:39:xx:xx:aa:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: .
OPTION:  53 (  1) DHCP message type         1 (DHCPDISCOVER)
OPTION:  55 ( 36) Parameter Request List      1 (Subnet mask)
                                              2 (Time offset)
                                              3 (Routers)
                                              4 (Time server)
                                              5 (Name server)
                                              6 (DNS server)
                                             11 (Resource location server)
                                             12 (Host name)
                                             13 (Boot file size)
                                             15 (Domainname)
                                             16 (Swap server)
                                             17 (Root path)
                                             18 (Extensions path)
                                             22 (Maximum datagram reassembly size)
                                             23 (Default IP TTL)
                                             28 (Broadcast address)
                                             40 (NIS domain)
                                             41 (NIS servers)
                                             42 (NTP servers)
                                             43 (Vendor specific info)
                                             50 (Request IP address)
                                             51 (IP address leasetime)
                                             54 (Server identifier)
                                             58 (T1)
                                             59 (T2)
                                             60 (Vendor class identifier)
                                             66 (TFTP server name)
                                             67 (Bootfile name)
                                            128 (???)
                                            129 (???)
                                            130 (???)
                                            131 (???)
                                            132 (???)
                                            133 (???)
                                            134 (???)
                                            135 (???)

OPTION:  57 (  2) Maximum DHCP message size 1260
OPTION:  97 ( 17) UUID/GUID                 004a1fd7451feae6 .J..E...
                                            118d82a4c64f47ed .....OG.
                                            82               .
OPTION:  93 (  2) Client System             0000             ..
OPTION:  94 (  3) Client NDI                010201           ...
OPTION:  60 ( 32) Vendor class identifier   PXEClient:Arch:00000:UNDI:002001
---------------------------------------------------------------------------

  TIME: 2017-08-08 01:22:39.798
    IP: xx.xx.xx.6 (2c:9d:1e:xx:xx:xx) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 2 (BOOTPREPLY)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: 394418d7
  SECS: 8
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: xx.xx.xx.15
SIADDR: xx.xx.xx.6
GIADDR: 0.0.0.0
CHADDR: 48:d5:39:xx:xx:aa:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: pxelinux.0.
OPTION:  53 (  1) DHCP message type         2 (DHCPOFFER)
OPTION:  54 (  4) Server identifier         xx.xx.xx.6
OPTION:  51 (  4) IP address leasetime      30 (30s)
OPTION:   1 (  4) Subnet mask               255.255.255.0
OPTION:   3 (  4) Routers                   xx.xx.xx.254
OPTION:   6 (  4) DNS server                xx.xx.xx.6
OPTION:  15 (  4) Domainname                maas
OPTION:  28 (  4) Broadcast address         xx.xx.xx.255
OPTION:  42 (  4) NTP servers               xx.xx.xx.6
---------------------------------------------------------------------------

  TIME: 2017-08-08 01:22:43.798
    IP: 0.0.0.0 (48:d5:39:xx:xx:aa) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 1 (BOOTPREQUEST)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: 394418d7
  SECS: 8
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: 0.0.0.0
SIADDR: 0.0.0.0
GIADDR: 0.0.0.0
CHADDR: 48:d5:39:xx:xx:aa:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: .
OPTION:  53 (  1) DHCP message type         3 (DHCPREQUEST)
OPTION:  50 (  4) Request IP address        xx.xx.xx.15
OPTION:  55 ( 36) Parameter Request List      1 (Subnet mask)
                                              2 (Time offset)
                                              3 (Routers)
                                              4 (Time server)
                                              5 (Name server)
                                              6 (DNS server)
                                             11 (Resource location server)
                                             12 (Host name)
                                             13 (Boot file size)
                                             15 (Domainname)
                                             16 (Swap server)
                                             17 (Root path)
                                             18 (Extensions path)
                                             22 (Maximum datagram reassembly size)
                                             23 (Default IP TTL)
                                             28 (Broadcast address)
                                             40 (NIS domain)
                                             41 (NIS servers)
                                             42 (NTP servers)
                                             43 (Vendor specific info)
                                             50 (Request IP address)
                                             51 (IP address leasetime)
                                             54 (Server identifier)
                                             58 (T1)
                                             59 (T2)
                                             60 (Vendor class identifier)
                                             66 (TFTP server name)
                                             67 (Bootfile name)
                                            128 (???)
                                            129 (???)
                                            130 (???)
                                            131 (???)
                                            132 (???)
                                            133 (???)
                                            134 (???)
                                            135 (???)

OPTION:  57 (  2) Maximum DHCP message size 1260
OPTION:  54 (  4) Server identifier         xx.xx.xx.6
OPTION:  97 ( 17) UUID/GUID                 004a1fd7451feae6 .J..E...
                                            118d82a4c64f47ed .....OG.
                                            82               .
OPTION:  93 (  2) Client System             0000             ..
OPTION:  94 (  3) Client NDI                010201           ...
OPTION:  60 ( 32) Vendor class identifier   PXEClient:Arch:00000:UNDI:002001
---------------------------------------------------------------------------

  TIME: 2017-08-08 01:22:43.898
    IP: xx.xx.xx.6 (2c:9d:1e:xx:xx:xx) > 255.255.255.255 (ff:ff:ff:ff:ff:ff)
    OP: 2 (BOOTPREPLY)
 HTYPE: 1 (Ethernet)
  HLEN: 6
  HOPS: 0
   XID: 394418d7
  SECS: 8
 FLAGS: 7f80
CIADDR: 0.0.0.0
YIADDR: xx.xx.xx.15
SIADDR: xx.xx.xx.6
GIADDR: 0.0.0.0
CHADDR: 48:d5:39:xx:xx:aa:00:00:00:00:00:00:00:00:00:00
 SNAME: .
 FNAME: pxelinux.0.
OPTION:  53 (  1) DHCP message type         5 (DHCPACK)
OPTION:  54 (  4) Server identifier         xx.xx.xx.6
OPTION:  51 (  4) IP address leasetime      30 (30s)
OPTION:   1 (  4) Subnet mask               255.255.255.0
OPTION:   3 (  4) Routers                   xx.xx.xx.254
OPTION:   6 (  4) DNS server                xx.xx.xx.6
OPTION:  15 (  4) Domainname                maas
OPTION:  28 (  4) Broadcast address         xx.xx.xx.255
OPTION:  42 (  4) NTP servers               xx.xx.xx.6
---------------------------------------------------------------------------
```
