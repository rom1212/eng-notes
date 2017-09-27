# DataSourceMAAS.py
* def read_maas_seed_url(seed_url, version=MD_VERSION):
  * seed_url is the base for a kind of metadata, e.g. /MAAS/metadata/.
  * it adds version to the path, i.e. /MAAS/metadata/<version>, e.g. /MAAS/metadata/2012-03-01, or /MAAS/metadata/latest
  * then, it adds data source fields to it, defined in DS_FIELDS
  ```
  DS_FIELDS = [
    # remote path, location in dictionary, binary data?, optional?
    ("meta-data/instance-id", 'meta-data/instance-id', False, False),
    ("meta-data/local-hostname", 'meta-data/local-hostname', False, False),
    ("meta-data/public-keys", 'meta-data/public-keys', False, True),
    ('meta-data/vendor-data', 'vendor-data', True, True),
    ('user-data', 'user-data', True, True),
  ]
  ```
  Then, the actual urls accessed will be url = "%s/%s/%s" % (seed_url, version, path),
  Two types of seed_url are used in maas
    * metadata (which is for comminssioning)
      * /MAAS/metadata/2012-03-01/meta-data/instance-id
      * /MAAS/metadata/2012-03-01/meta-data/local-hostname
      * /MAAS/metadata/2012-03-01/meta-data/public-keys
      * /MAAS/metadata/2012-03-01/meta-data/vendor-data
      * /MAAS/metadata/2012-03-01/user-data
    * curtin (which is for deploying)
      * /MAAS/metadata/curtin/2012-03-01/meta-data/instance-id
      * /MAAS/metadata/curtin/2012-03-01/meta-data/local-hostname
      * /MAAS/metadata/curtin/2012-03-01/meta-data/public-keys
      * /MAAS/metadata/curtin/2012-03-01/meta-data/vendor-data
      * /MAAS/metadata/curtin/2012-03-01/user-data
    
    
