# ReverseProxy
* Why "Reverse"?
  * Because it only "proxy" the response back. It changes the request.
* "ReverseProxy is an HTTP Handler that takes an incoming request and sends it to another server, proxying the response back to the client."
* Director func(*http.Request)
  * // Director must be a function which modifies
  * // the request into a new request to be sent
  * // using Transport. Its response is then copied
  * // back to the original client unmodified.
  *  // Director must not access the provided Request
  *  // after returning.

* https://golang.org/pkg/net/http/httputil/
* https://www.integralist.co.uk/posts/golang-reverse-proxy/

# URL
* URL path: everthing comes after the domain name. It can be empty.
  * https://play.golang.org/p/m2wosNkr3Mc
```go
func main() {
	fmt.Println("Hello, playground")
	fmt.Printf("path:<%s>\n", path.Join("", ""))
	fmt.Printf("path:<%s>\n", path.Join("", "/good"))
	fmt.Printf("path:<%s>\n", path.Join("", "/good/"))
	fmt.Printf("path:<%s>\n", path.Join("/more", "/good"))
	fmt.Printf("path:<%s>\n", path.Join("/more/", "/good"))
	fmt.Printf("path:<%s>\n", path.Join("/more/", "/good/"))

	myurl, err := url.Parse("http://this.com")
	fmt.Printf("url:%#v, err: %v\n", myurl, err)

	myurl, err = url.Parse("http://this.com/mypath")
	fmt.Printf("url:%#v, err: %v\n", myurl, err)

	myurl, err = url.Parse("http://this.com/mypath/")
	fmt.Printf("url:%#v, err: %v\n", myurl, err)
}
```
Output
```
path:<>
path:</good>
path:</good>
path:</more/good>
path:</more/good>
path:</more/good>
url:&url.URL{Scheme:"http", Opaque:"", User:(*url.Userinfo)(nil), Host:"this.com", Path:"", RawPath:"", ForceQuery:false, RawQuery:"", Fragment:""}, err: <nil>
url:&url.URL{Scheme:"http", Opaque:"", User:(*url.Userinfo)(nil), Host:"this.com", Path:"/mypath", RawPath:"", ForceQuery:false, RawQuery:"", Fragment:""}, err: <nil>
url:&url.URL{Scheme:"http", Opaque:"", User:(*url.Userinfo)(nil), Host:"this.com", Path:"/mypath/", RawPath:"", ForceQuery:false, RawQuery:"", Fragment:""}, err: <nil>
```
