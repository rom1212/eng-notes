# src/maasserver/
## compose_preseed.py
* _compose_cloud_init_preseed
  * <- compose_commissioning_preseed
  * <- compose_curtin_preseed
  
## api/support.py
* OperationsHandlerMixin
  * dispatch: get "op", and find exported functions by self.exports.
  * class OperationsHandler(OperationsHandlerMixin, piston3.handler.BaseHandler, metaclass=OperationsHandlerType):

## metadataserver/urls.py
* meta_data_anon_handler = OperationsResource(AnonMetaDataHandler)
  * class AnonMetaDataHandler(VersionIndexHandler) in metadataserver/api.py
    * operations
      * get_enlist_preseed
      * get_preseed
      * netboot_off
    * class VersionIndexHandler(MetadataViewHandler)
      * class MetadataViewHandler(OperationsHandler)
        * create = update = delete = None
        * def read(self, request, mac=None): return make_list_response(sorted(self.subfields))

