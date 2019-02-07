# string
* check empty string
```go
// both are ok: https://stackoverflow.com/questions/18594330/what-is-the-best-way-to-test-for-an-empty-string-in-go
if len(s) == 0 { ... }
if s == "" { ... }
```
* case-insensitive
https://golang.org/pkg/strings/#EqualFold

* string contains types, but can be converted to rune
  * If you iterate string, it will output the internal rune, but the index is still the index of bytes
  * But the size is still the size of bytes.
  * https://play.golang.org/p/WcaJRYd1tdf
  * https://mymemorysucks.wordpress.com/2017/05/03/a-short-guide-to-mastering-strings-in-golang/
  * https://stackoverflow.com/questions/19310700/what-is-a-rune
```
	chinesePhrase := "你好吗"

	fmt.Println("len(chinesePhrase):", len(chinesePhrase))
	for i, c := range chinesePhrase {
		fmt.Println(i, c)
	}

# len(chinesePhrase): 9
# 0 20320
# 3 22909
# 6 21527
```

* quote and escape
  * https://golang.org/pkg/strconv/#Quote
