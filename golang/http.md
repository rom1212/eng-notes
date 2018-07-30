# HTTP
## Request
* query string
  * https://stackoverflow.com/questions/15407719/in-gos-http-package-how-do-i-get-the-query-string-on-a-post-request
  * r.URL.Query()
  ```go
  // This is a list. Not sure whether there is a default lengh???
  queryID = req.URL.Query()["bookId"][0]
  ```
