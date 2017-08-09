# Restart the device
http://support.huawei.com/enterprise/en/doc/DOC1000062638?idPath=7919710%7C21782165%7C21782239%7C22318639%7C21059820
```
reboot [ fast | save diagnostic-information ]
```

# Config for next starup
```
# view the specified files for next startup
display startup
# e.g.
MainBoard:
  Configured startup system software:        flash:/CE5855EI-V100R005C10SPC200.cc
  Startup system software:                   flash:/CE5855EI-V100R005C10SPC200.cc
  Next startup system software:              flash:/CE5855EI-V100R005C10SPC200.cc
  Startup saved-configuration file:          NULL
  Next startup saved-configuration file:     flash:/vrpcfg.zip
  Startup paf file:                          default
  Next startup paf file:                     default
  Startup patch package:                     flash:/CE5855EI-V100R005SPH009.PAT
  Next startup patch package:                flash:/CE5855EI-V100R005SPH009.PAT

# config for next startup
startup system-software <system-file>
startup saved-configuration <configuration-file>
startup patch <patch-name> { all | slot slot-id } # optional
```

# Clear config
