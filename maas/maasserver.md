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
* render_preseed()
  * load_preseed_template()
  * context = get_preseed_context
  * context.update(get_node_preseed_context())
  * ```return template.substitute(**context).encode("utf-8")```
* get_preseed_template()
  * PRESEED_TEMPLATE_LOCATIONS: "/etc/maas/preseeds", "/usr/share/maas/preseeds",
    * content is from maaas/contrib/preseeds_v2/
      * commissioning: {{preseed_data}}
      * curtin: {{preseed_data}}
      * enlist, enlist_userdata,
      * curtin_userdata, curtin_userdata_custom, curtin_userdata_windows, curtin_userdata_centos, curtin_userdata_suse, 
      * for Ubuntu, there is no _osystem_xxx etc suffix.
* get_node_preseed_context:
  * 'preseed_data': compose_preseed(get_preseed_type_for(node), node)
  * maasserver/compose_preseed.py:compose_preseed()
    * compose_commissioning_preseed
      * metadata_url = absolute_reverse('metadata', base_url=base_url)
      * poweroff_timeout
      * _compose_cloud_init_preseed
    * compose_curtin_preseed
      * metadata_url = absolute_reverse('curtin-metadata', base_url=base_url)
      * _compose_cloud_init_preseed
* get_preseed_type_for(node)
  ```
    if is_commissioning_preseed:
        return PRESEED_TYPE.COMMISSIONING
    else:
        return PRESEED_TYPE.CURTIN
  ```
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

