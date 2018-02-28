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
* 
