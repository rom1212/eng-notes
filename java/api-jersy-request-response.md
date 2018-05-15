# Jersy
## client response
* How to get list<String> as response from jersey2 client
* https://stackoverflow.com/questions/35313767/how-to-get-liststring-as-response-from-jersey2-client
```java
Response serviceResponse = client.target(url).
                    request(MediaType.APPLICATION_JSON).get(Response.class);
List<String> list = serviceResponse.readEntity(new GenericType<List<String>>() {
                });
```

## Error handling
http://www.codingpedia.org/ama/error-handling-in-rest-api-with-jersey/
