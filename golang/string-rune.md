# String
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
* split
https://golang.org/pkg/strings/#SplitN
```
// split into at most 2 fields, seperated by "="
fields := strings.SplitN(format, "=", 2)
```
# Escaped Characters
* https://golang.org/ref/spec#Rune_literals
```
\a   U+0007 alert or bell
\b   U+0008 backspace
\f   U+000C form feed
\n   U+000A line feed or newline
\r   U+000D carriage return
\t   U+0009 horizontal tab
\v   U+000b vertical tab, same as \013 (which is octal number)
\\   U+005c backslash
\'   U+0027 single quote  (valid escape only within rune literals)
\"   U+0022 double quote  (valid escape only within string literals)

'\000'  this is for octal digits, because it starts with a octal digit
'\007'  this is for octal digits, because it starts with a octal digit
'\377'
'\x07'
'\xff'
'\u12e4'
'\U00101234'
'\''         // rune literal containing single quote character
'aa'         // illegal: too many characters
'\xa'        // illegal: too few hexadecimal digits
'\0'         // illegal: too few octal digits
'\uDFFF'     // illegal: surrogate half
'\U00110000' // illegal: invalid Unicode code point
```
