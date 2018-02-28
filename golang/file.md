# Read from file

## bufio.NewReader()
```go
  // assumes that input only has one line
	reader := bufio.NewReader(os.Stdin)
	s, err := reader.ReadString('\n')  // no error for the first read
	if err != nil {
		panic(err)
	}

	s, err = reader.ReadString('\n')  // the error will be io.EOF = errors.New("EOF")
	if err != nil {
		fmt.Println("error:", err)  // this time will print out the error
	}
```

## ioutil.ReadAll()
* https://golang.org/pkg/io/ioutil/#example_ReadAll
* To find out how go handlers reading and EOF, read this function: bytes.Buffer.ReadFrom()
  * https://golang.org/src/bytes/buffer.go

