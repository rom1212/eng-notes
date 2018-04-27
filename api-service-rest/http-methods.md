# HTTP Methods
* https://stackoverflow.com/questions/630453/put-vs-post-in-rest

## Rule
```diff
- Better is to choose between PUT and POST based on idempotence of the action.
```

## POST
* POST is used to create.
 * POST /expense-report
* A POST is not idempotent
```
The POST method is used to request that the origin server accept the entity enclosed 
in the request as a new subordinate of the resource identified by the Request-URI in the Request-Line
```
```
POST updates a resource, adds a subsidiary resource, or causes a change. A POST is not idempotent, 
in the way that x++ is not idempotent. 
```

## PUT
* That is, PUT is used to create (a specified URI resource, not general, e.g. /books, it has to be /books/xxxx) or update.
* PUT is idempotent
  * PUT  /expense-report/10929
```
The PUT method requests that the enclosed entity be stored under the supplied Request-URI. 
If the Request-URI refers to an already existing resource, the enclosed entity SHOULD be
considered as a modified version of the one residing on the origin server. 
If the Request-URI does not point to an existing resource, and that URI is capable of being
defined as a new resource by the requesting user agent, the origin server can create the resource with that URI.
```
```
PUT implies putting a resource - completely replacing whatever is available at the given URL with a different thing. 
By definition, a PUT is idempotent. Do it as many times as you like, and the result is the same. x=5 is idempotent. 
You can PUT a resource whether it previously exists, or not (eg, to Create, or to Update)!
```


