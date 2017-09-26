# cloud-init how
## Steps
* /etc/init/*: cloud-init init
* cloud-init init
  * cloudinit/cmd/main.py -> main_init() -> attempt_cmdline_url(path="/etc/cloud/cloud.cfg.d/91_kernel_cmdline_url.cfg"):
    * summary:
      * get "cloud-config-url" or "url" from kernel command line parameters
      * get content from that url, and write to "/etc/cloud/cloud.cfg.d/91_kernel_cmdline_url.cfg", which will be used by cloud-init later.
    * details
    ```
    * cmdline = util.get_cmdline()
      * get kernel command line (parameters) from "/proc/cmdline" (or "/proc/1/cmdline" if it's lxd container)
      * kernel command line is sent by PXE boot config from PXE server. (with cc:xxx:end) ???TTT
        * https://github.com/maas/maas/blob/master/src/provisioningserver/tests/test_kernel_opts.py
    * cmdline_name, url = parse_cmdline_url(cmdline)
    * kwargs = {'url': url, 'timeout': 10, 'retries': 2}
    * resp = util.read_file_or_url(**kwargs)
    * data = resp.contents
    * util.write_file(path, data, mode=0o600)
    ```
## cloud-init init
* 
