# HTTP
## URL
* https://en.wikipedia.org/wiki/URL
* fragment is the concept of a browser. On the server side, we cannot get fragment.
  * https://stackoverflow.com/questions/25489843/http-server-get-url-fragment


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

## ReverseProxy
* How it is tested: 
  * https://golang.org/src/net/http/httputil/reverseproxy_test.go
* https://golang.org/pkg/net/http/httputil/#ReverseProxy
  * NewSingleHostReverseProxy is a simple director
  * customized,
```go
	pro := &httputil.ReverseProxy{
		Director: func(req *http.Request) {
			// Change: req.URL.Scheme, req.URL.Host etc, see NewSingleHostReverseProxy
		},
		Transport: &oauth2.Transport{
   // set Base and Source
		},
		// Other fields, e.g. FlushInterval
	}
	handler := http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		pro.ServeHTTP(w, r)
	})
	port, err := portpicker.PickUnusedPort()
 http.ListenAndServe(fmt.Sprintf(":%d", port), handler)
```
