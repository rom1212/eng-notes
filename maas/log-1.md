# logs
## log01.kernel-opts
cloud-config-url=http://172.23.48.5:5240/MAAS/metadata/latest/enlist-preseed/?op=get_enlist_preseed
* should -> AnonMetaDataHandler.get_enlist_preseed -> preseed.py:render_enlistment_preseed,
  * get_preseed_context: metadata_enlist_url=absolute_reverse('enlist', base_url=base_url)
## log02.kernel-opts
cloud-config-url=http://172.23.48.5:5240/MAAS/metadata/latest/by-id/fycnr3/?op=get_preseed

