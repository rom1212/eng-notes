# Create /dev/ipmi0
* modprobe ipmi_devintf; modprobe ipmi_si
  * https://www.thomas-krenn.com/en/wiki/Configuring_IPMI_under_Linux_using_ipmitool
* If it still doesn't exist, try this
  * mknod /dev/ipmi0 c `cat /proc/devices | grep ipmidev |cut -d " " -f 1` 0
  * mknod /dev/ipmi0 c <ipmidev device number> 0
  * https://forum.likg.org.ua/ipmi/create-dev-ipmi0-device-manually-t355.html

# Install IPMITool
* sudo apt install ipmitool

# Show IPMI Info
* sudo ipmitool lan print
