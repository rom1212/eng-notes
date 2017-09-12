Java Runtime Errors
* @JsonProperty
  * If two data member are marked with the same @JsonProperty, compiling works, but it is runtime error, e.g. 
  ```java
  @JsonProperty('publishDate')
  private String publishDate;
  
  @JsonProperty('publishDate')
  private String publishInfo;
  ```
  ```
INFO  [2017-09-12 17:34:34,253] org.reflections.Reflections: Reflections took 352 ms to scan 1 urls, producing 154 keys and 342 values 
Exception in thread "main" java.lang.IllegalArgumentException: Conflicting getter definitions for property "publishDate": com.pinterest.deployservice.bean.BuildBean#getPublish_date(0 params) vs com.pinterest.deployservice.bean.BuildBean#getPackages(0 params)
	at com.fasterxml.jackson.databind.introspect.POJOPropertyBuilder.getGetter(POJOPropertyBuilder.java:243)
	at com.fasterxml.jackson.databind.introspect.POJOPropertyBuilder.getAccessor(POJOPropertyBuilder.java:364)
	at com.fasterxml.jackson.databind.introspect.POJOPropertyBuilder.getPrimaryMember(POJOPropertyBuilder.java:396)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:256)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:159)
	at io.swagger.converter.ModelConverterContextImpl.resolve(ModelConverterContextImpl.java:99)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:138)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:103)
	at io.swagger.converter.ModelConverterContextImpl.resolveProperty(ModelConverterContextImpl.java:79)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:373)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:159)
	at io.swagger.converter.ModelConverterContextImpl.resolve(ModelConverterContextImpl.java:99)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:138)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:103)
	at io.swagger.converter.ModelConverterContextImpl.resolveProperty(ModelConverterContextImpl.java:79)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:373)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:159)
	at io.swagger.converter.ModelConverterContextImpl.resolve(ModelConverterContextImpl.java:99)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:138)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:103)
	at io.swagger.converter.ModelConverterContextImpl.resolveProperty(ModelConverterContextImpl.java:79)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:119)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:103)
	at io.swagger.converter.ModelConverterContextImpl.resolveProperty(ModelConverterContextImpl.java:79)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:373)
	at io.swagger.jackson.ModelResolver.resolve(ModelResolver.java:159)
	at io.swagger.converter.ModelConverterContextImpl.resolve(ModelConverterContextImpl.java:99)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:138)
	at io.swagger.jackson.ModelResolver.resolveProperty(ModelResolver.java:103)
	at io.swagger.converter.ModelConverterContextImpl.resolveProperty(ModelConverterContextImpl.java:79)
	at io.swagger.converter.ModelConverters.readAsProperty(ModelConverters.java:58)
	at io.swagger.jaxrs.Reader.parseMethod(Reader.java:750)
	at io.swagger.jaxrs.Reader.read(Reader.java:275)
	at io.swagger.jaxrs.Reader.read(Reader.java:147)
	at io.swagger.jaxrs.config.BeanConfig.setScan(BeanConfig.java:172)
	at com.pinterest.teletraan.TeletraanService.run(TeletraanService.java:192)
	at com.pinterest.teletraan.TeletraanService.run(TeletraanService.java:65)
	at io.dropwizard.cli.EnvironmentCommand.run(EnvironmentCommand.java:42)
	at io.dropwizard.cli.ConfiguredCommand.run(ConfiguredCommand.java:76)
	at io.dropwizard.cli.Cli.run(Cli.java:70)
	at io.dropwizard.Application.run(Application.java:73)
	at com.pinterest.teletraan.TeletraanService.main(TeletraanService.java:206)  
  ```
