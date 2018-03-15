# Read from file
## Reader
* read from input, and when EOF is found, it will return io.EOF error, however, the returned value is still good.
  * this is true for bufio.Reader.ReadString() and bufio.Scanner.Scan()

## bufio.NewReader()
* ReadString() - 
  * when there is EOF, it returns error as io.EOF, howerver, the data returned is still good. If ReadString encounters an error before finding a delimiter, it returns the data read before the error and the error itself (often io.EOF).
  * returns err != nil if and only if the returned data does not end in delim.
```go
  // assumes that input only has one line
	reader := bufio.NewReader(os.Stdin)
	s, err := reader.ReadString('\n')  // no error for the first read
	if err != nil {
		panic(err)
	}

	s, err = reader.ReadString('\n')  // the error will be io.EOF = errors.New("EOF")
	if err != nil {
		fmt.Println("error:", err)  // this time will print out the error. 
	}
```

## ioutil.ReadAll()
* https://golang.org/pkg/io/ioutil/#example_ReadAll
* To find out how go handlers reading and EOF, read this function: bytes.Buffer.ReadFrom()
  * https://golang.org/src/bytes/buffer.go

# Write to file

## Append to a file
```go
        // can append even the file doesn't exist
	file, err := os.OpenFile("/tmp/append.txt", os.O_APPEND|os.O_WRONLY|os.O_CREATE, 0600)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	for i, s := range os.Args {
		if _, err = file.WriteString(strconv.Itoa(i) + ":" + s + "\n"); err != nil {
			panic(err)
		}
	}
```

# Check File
https://stackoverflow.com/questions/12518876/how-to-check-if-a-file-exists-in-go
```go
// check file not exist
if _, err := os.Stat("/path/to/whatever"); os.IsNotExist(err) {
  // path/to/whatever does not exist
}

// check file exist
if _, err := os.Stat("/path/to/whatever"); err == nil {
  // path/to/whatever exists
}
```
