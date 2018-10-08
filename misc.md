Notations:
* TTT???
* DONOT

iSCSI performance:
* https://social.technet.microsoft.com/Forums/windows/en-US/abbe6ab5-de77-47e1-8097-ab5a61c9a54f/1gb-iscsi-typical-speeds?forum=winserverhyperv
* https://www.monperrus.net/martin/performance+of+read-write+throughput+with+iscsi

Turn any browser into an editor:
```
data:text/html, <body contenteditable style="font: 2rem/1.5 monospace;max-width:60rem;margin:0 auto;padding:4rem;">
```


https://jingyan.baidu.com/article/eae07827bf73a81fed548576.html

http://finance.sina.com.cn/realstock/company/sh600000/nc.shtml

# Windows
## Recover Unsaved Word document (Word 2016)

The document was worked on for sometime, and then the computer was shutdown/sleep. When login again, we found that the changes are not there. The document was a onedrive document opened by Word 2016.

Tried several things:
  * First try:
    * http://www.knowledgewave.com/blog/how-to-recover-an-unsaved-word-document
    * Use Info->"Manage Document"->Recover Unsaved Documents
      * cannot found the old document (xxx.asd) in the folder, e.g. C:\Users\xxx\AppData\Local\Microsoft\Office\UnsavedFiles, and sub-folders.
  * Second try:
    * Use "Options"->Save-> AutoRecover file location: e.g. C:\Users\xxx\AppData\Roaming\Microsoft\Word\
      * in the folder, found one file like this: ~Wxxx.asd
    * Use Info->"Manage Document"->Recover Unsaved Documents, and change the default load location to the above location, and load that file, and it works!!!! yeah!!!
      
## OpenVPN
* Download
  * https://openvpn.net/index.php/open-source/downloads.html, e.g. OpenVPN 2.4.4 -- released on 2017.09.26
* After starting, lower right corner, expand, right click, "Import file..."
* config file
```
 ###OpenVPN Client.conf###
client

dev tun

 #For windows client you will need TAP-Win32 adaptor name#
;dev-node MyTap

proto udp

# VPN end point
remote xx.xxx.x.xx 1194

resolv-retry infinite

nobind

persist-key
persist-tun

# pay attention to the path here. "\" doesn't work.
ca C:/Users/xxx/ca.crt
cert C:/Users/xxx/xxxx.crt
key C:/Users/xxx/xxxx.key

ns-cert-type server

comp-lzo

verb 
```

# PaaS/Saas software
* https://www.gremlin.com/
* http://www.seleniumhq.org/projects/webdriver/

stackoverflow salary:
* https://stackoverflow.blog/2018/09/05/developer-salaries-in-2018-updating-the-stack-overflow-salary-calculator/

# C++ compiler
* compiler https://llvm.org/
