# src/maasserver/
## compose_preseed.py
* _compose_cloud_init_preseed
  * <- compose_commissioning_preseed
  * <- compose_curtin_preseed
  
## api/support.py
* OperationsHandlerMixin
  * dispatch: get "op", and find exported functions by self.exports.
  * class OperationsHandler(OperationsHandlerMixin, piston3.handler.BaseHandler, metaclass=OperationsHandlerType):

## preseed.py
* get_preseed_template
 * PRESEED_TEMPLATE_LOCATIONS: "/etc/maas/preseeds", "/usr/share/maas/preseeds",
   * content is from maaas/contrib/preseeds_v2/
     * commissioning, curtin_userdata, curtin_userdata_custom, curtin_userdata_windows, enlist_userdata, curtin,  curtin_userdata_centos, curtin_userdata_suse, enlist
     * for Ubuntu, there is no _osystem_xxx etc suffix.
* 


## metadataserver/urls.py
* meta_data_anon_handler = OperationsResource(AnonMetaDataHandler)
  * class AnonMetaDataHandler(VersionIndexHandler) in metadataserver/api.py
    * operations
      * get_enlist_preseed
      * get_preseed
        * maasserver/preseed.py: get_preseed()
          * if COMMISSIONING_LIKE_STATUSES
            * render_preseed(
            node, PRESEED_TYPE.COMMISSIONING,
            osystem=Config.objects.get_config('commissioning_osystem'),
            release=Config.objects.get_config('commissioning_distro_series'))
            * maasserver/models/config.py:get_default_config
              * 'commissioning_osystem': DEFAULT_OS.name,
              * 'commissioning_distro_series': DEFAULT_OS.get_default_commissioning_release()
              * DEFAULT_OS = provisioningserver.drivers.osystem.ubuntu.UbuntuOS()
          * otherwise
            * render_preseed(
            node, get_preseed_type_for(node),
            osystem=node.get_osystem(), release=node.get_distro_series())
      * netboot_off
    * class VersionIndexHandler(MetadataViewHandler)
      * class MetadataViewHandler(OperationsHandler)
        * create = update = delete = None
        * def read(self, request, mac=None): return make_list_response(sorted(self.subfields))

