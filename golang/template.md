# Golang Template
## Docs:
  * https://blog.gopheracademy.com/advent-2017/using-go-templates/
  * https://golang.org/pkg/text/template/
    * minus sign
  * https://golang.org/pkg/html/template/

## Examples
```go
// loop
{{range $member := .Members}}
This is a "$member"
{{end}}

// or, which is useful if we want to have one index to iterate multiple slices.
{{$Members := .Members}}
{{range $i, $ := $Members}}
{{$member := index $Members $i}}
This is a "$member"
{{end}}
```
