# Error Code
* 300 - multiple choices
  * could be used to return the results, if there are multiple results for an query id, and the clients are supposed to handle, e.g. normally, a serial number only corresponds to one book, if somehow a serial number returns multiple books, we could use 300 to return those multiple books.

* 400 - bad request

* 401
  * auth header problems
  * authentication failed
  * or anything related to auth except 403 (authorization failed)

* 404 
  * the entity is not found
  
* 422
  * unproccessable Entity
  * mostly during server validation of the input data.
  
