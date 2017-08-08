# Interface Info from lshw
```
$ sudo lshw > lshw.txt
# search "Ethernet interface" in lshw.txt, e.g.
--------------------------------------------
     *-pci:0
        *-pci:0
        *-pci:1
             description: PCI bridge$
             product: Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D PCI Express Root Port 2$
             vendor: Intel Corporation$
             physical id: 2$
             bus info: pci@0000:00:02.0$
             version: 01$
             width: 32 bits$
             clock: 33MHz$
             capabilities: pci msi pciexpress pm normal_decode bus_master cap_list$
             configuration: driver=pcieport$
             resources: irq:26 ioport:2000(size=4096) memory:93000000-937fffff ioport:92000000(size=9437184)$
           *-network:0		
                description: Ethernet interface$
                product: 82599ES 10-Gigabit SFI/SFP+ Network Connection$
                vendor: Intel Corporation$
                physical id: 0$
                bus info: pci@0000:02:00.0$
                logical name: enp2s0f0$
                version: 01$
                serial: a4:c6:4f:xx:xx:11$  # this is the MAC address
                size: 10Gbit/s$
                width: 64 bits$
                clock: 33MHz$
                capabilities: pm msi msix pciexpress vpd bus_master cap_list rom ethernet physical fibre$
                configuration: autonegotiation=off broadcast=yes driver=ixgbe driverversion=4.2.1-k duplex=full firmware=0x800003df ip=xxx.xx.49.11 latency=0 link=yes multicast=yes port=fibre speed=10Gbit/s$
                resources: irq:0 memory:92400000-927fffff ioport:2020(size=32) memory:92804000-92807fff memory:930
           *-network:1 DISABLED$
                description: Ethernet interface$
                product: 82599ES 10-Gigabit SFI/SFP+ Network Connection$
                vendor: Intel Corporation$
                physical id: 0.1$
                bus info: pci@0000:02:00.1$
                logical name: enp2s0f1$
                version: 01$
                serial: a4:c6:4f:xx:xx:22$
                width: 64 bits$
                clock: 33MHz$
                capabilities: pm msi msix pciexpress vpd bus_master cap_list ethernet physical fibre$
                configuration: autonegotiation=off broadcast=yes driver=ixgbe driverversion=4.2.1-k firmware=0x800003df latency=0 link=no multicast=yes port=fibre$
                resources: irq:0 memory:92000000-923fffff ioport:2000(size=32) memory:92800000-92803fff memory:93600000-936fffff memory:93700000-937fffff$

     *-pci:2
          description: PCI bridge$
          product: Xeon E7 v4/Xeon E5 v4/Xeon E3 v4/Xeon D PCI Express Root Port 2$
          vendor: Intel Corporation$
          physical id: 2.2$
          bus info: pci@0000:80:02.2$
          version: 01$
          width: 32 bits$
          clock: 33MHz$
          capabilities: pci msi pciexpress pm normal_decode bus_master cap_list$
          configuration: driver=pcieport$
          resources: irq:34 memory:c8000000-c82fffff ioport:3c000000000(size=1048576)$
        *-network:0$
             description: Ethernet interface$
             product: I350 Gigabit Network Connection$
             vendor: Intel Corporation$
             physical id: 0$
             bus info: pci@0000:81:00.0$
             logical name: enp129s0f0$
             version: 01$
             serial: 48:d5:39:xx:xx:11$
             size: 1Gbit/s$
             capacity: 1Gbit/s$
             width: 32 bits$
             clock: 33MHz$
             capabilities: pm msi msix pciexpress bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autone
             configuration: autonegotiation=on broadcast=yes driver=igb driverversion=5.3.0-k duplex=full firmware=1.63, 0x800009fa ip=xxx.xx.48.11 latency=0 link=yes multicast=yes port=twisted pair speed=1Gbit/s$
             resources: irq:0 memory:c8100000-c81fffff memory:c8204000-c8207fff memory:3c000000000-3c00001ffff memory:3c000020000-3c000
        *-network:1 DISABLED$
             description: Ethernet interface$
             product: I350 Gigabit Network Connection$
             vendor: Intel Corporation$
             physical id: 0.1$
             bus info: pci@0000:81:00.1$
             logical name: enp129s0f1$
             version: 01$
             serial: 48:d5:39:xx:xx:22$
             capacity: 1Gbit/s$
             width: 32 bits$
             clock: 33MHz$
             capabilities: pm msi msix pciexpress bus_master cap_list ethernet physical tp 10bt 10bt-fd 100bt 100bt-fd 1000bt-fd autonegotiation$
             configuration: autonegotiation=on broadcast=yes driver=igb driverversion=5.3.0-k firmware=1.63, 0x800009fa latency=0 link=no multicast=yes port=twisted pair$
             resources: irq:0 memory:c8000000-c80fffff memory:c8200000-c8203fff memory:3c000040000-3c00005ffff memory:3c000060000-3c00007ffff$
```
