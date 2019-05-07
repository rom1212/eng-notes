# HTTP
## Request
* query string
  * https://stackoverflow.com/questions/15407719/in-gos-http-package-how-do-i-get-the-query-string-on-a-post-request
  * r.URL.Query()
  ```go
  // This is a list. Not sure whether there is a default lengh???
  queryID = req.URL.Query()["bookId"][0]
  ```

## Test HTTPS
* Test server
  * httptest.NewTLSServer
* Client ignore certificate
```go
tr := &http.Transport{
 TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
}
client := &http.Client{Transport: tr}
```
* https://blog.dnsimple.com/2017/08/how-to-test-golang-https-services/
* 
