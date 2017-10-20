


# How To
## Docs
https://monoinfinito.wordpress.com/series/setting-up-a-linux-gatewayrouter-a-guide-for-non-network-admins/

## Enable IP forwarding
* http://www.ducea.com/2006/08/01/how-to-enable-ip-forwarding-in-linux/
* Enable IP forwarding
```
# check ip-forwarding enabled or not
sysctl net.ipv4.ip_forward
cat /proc/sys/net/ipv4/ip_forward

# Enable on the fly
sysctl -w net.ipv4.ip_forward=1
echo 1 > /proc/sys/net/ipv4/ip_forward

# Permanet
vim /etc/sysctl.conf
```

