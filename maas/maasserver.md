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


# metadataserver
## urls.py
* r'^[/]*(?P<version>[^/]+)/by-id/(?P<system_id>[\w\-]+)/$', meta_data_anon_handler
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
* r'^[/]*(?P<version>[^/]+)/maas-scripts, maas_scripts_handler (MAASScriptsHandler), 

## api.py
* MAASScriptsHandler - (replace CommissioningScriptsHandler)
* UserDataHandler
  * user_data = NodeUserData.objects.get_user_data(node)
    * where NodeUserData is written by maasserver/models/node.py: start_commissioning() - which is trigger by api/ui
      * commissioning_userdata = generate_user_data_for_status()
        * metadataserver/user_data/__init__.py: generate_user_data_for_status
          * metadataserver/template/commissioning.template
            * maas_run_remote_scripts.py
              * download_and_extract_tar("%s/maas-scripts/" % url)
                * metadataserver/urls.py: maas-scripts/
  * so, after host get user_data, it will call /maas-scripts/, and it's handlers.
 
    
* CurtinUserDataHandler
  * read -> get_curtin_userdata() -> get_curtin_yaml_config() + get_curtin_installer_url()
    * main_config = get_curtin_config(node)
      * template: maas/contrib/preseeds_v2/curtin_userdata
        * debconf_selections
    * cloud_config = compose_curtin_cloud_config(node) -> get_curtin_cloud_config
      * /etc/cloud/cloud.cfg.d/90_maas_datasource.cfg
      * /etc/cloud/cloud.cfg.d/90_maas_cloud_config.cfg
      * /etc/cloud/cloud.cfg.d/90_maas_ubuntu_sso.cfg
      * /etc/cloud/cloud.cfg.d/90_maas_cloud_init_reporting.cfg
    * archive_config = compose_curtin_archive_config(node)
      *  apt related
    * reporter_config = compose_curtin_maas_reporter(node)
    * swap_config = compose_curtin_swap_preseed(node)
    * kernel_config = compose_curtin_kernel_preseed(node)
      * 'kernel': kpackage
    * verbose_config = compose_curtin_verbose_preseed()
