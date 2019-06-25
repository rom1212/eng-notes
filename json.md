# json

## Multi-line

No multi-line string with control character. Must be escaped. This is understandable because json is supposed to be read by machine, not human. That' why terraform is using HCL format which is indended for human.

According to json specification (http://json.org/), 
```
A string is a sequence of zero or more Unicode characters, wrapped in double quotes, using backslash escapes.

i.e.

"< any Unicode character except " or \ or control character>"
```

docs:
  * https://stackoverflow.com/questions/2392766/multiline-strings-in-json
  * https://www.gun.io/blog/multi-line-strings-in-json
  ```
  JSON is an extremely rigid schema. It's great, but it has a couple of shortcomings, the largest of which is the inability to store multi-line strings. 
  ```


### Go
Normal string
```
"{ \"some key\": \"input1 \\\n input1 \" }"
```
because Go does escaping first, so \\\n is translated to \n, and the above json is translated to 
```
{ "some key": "input1 \n input1 " }
```

Raw string
```
`{ "some key": "input1 \n input1 " }`
```

### Shell
Shell with escaping:
```
"{ \"some key\": \"input1 \\\n input1 \" }"
```
because shell does escaping first, so \\\n is translated to \n, and the above json is translated to 
```
{ "some key": "input1 \n input1 " }
```

Shel raw string without escaping:
```
'{ "some key": "input1 \n input1 " }'
```

### Python
Raw string
```
r`some thing`
```

