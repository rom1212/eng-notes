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

## ioutil.ReadFile
* func ReadFile(filename string) ([]byte, error)
  * https://golang.org/pkg/io/ioutil/#example_ReadFile
```
// Can be used for quick debugging
package main

import (
	"fmt"
	"io/ioutil"
	"log"
)

func main() {
	content, err := ioutil.ReadFile("testdata/hello")
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("File contents: %s\n", content)

}
```

## ioutil.ReadAll()
* https://golang.org/pkg/io/ioutil/#example_ReadAll
* To find out how go handlers reading and EOF, read this function: bytes.Buffer.ReadFrom()
  * https://golang.org/src/bytes/buffer.go

# Write to file
## Write string to file
```go
	decoder := json.NewDecoder(r.Body)
	var request Request
	err := decoder.Decode(&request)
	if err != nil {
		panic(err)
	}
	defer r.Body.Close()

	b, err := json.MarshalIndent(request, "", "    ")
        ioutil.WriteFile("/tmp/request.json", b, os.ModePerm)
	// ioutil.WriteFile("/tmp/request.json", []bytes(someString), os.ModePerm)
```

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

# File and Directory
## Check File
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

## File Location/Directory
```
func currFileDir() string {
	_, thisfile, _, _ := runtime.Caller(0)
	return path.Dir(thisfile)
}
```

## Running Binary Directory
```go
import (
    "fmt"
    "log"
    "os"
    "path/filepath"
)

func main() {
    dir, err := filepath.Abs(filepath.Dir(os.Args[0]))
    if err != nil {
            log.Fatal(err)
    }
    fmt.Println(dir)
}
```

## Create Directory
* MkDirAll
```
os.MkdirAll(folderPath, os.ModePerm);
```
Have to use os.ModePerm, otherwise, it cannot create the second level directory. See:
https://github.com/golang/go/issues/15210

# Path

## Join Path
```go
import "path/filepath"
//sep := string(os.PathSeparator)
path := filepath.Join("this/path/", "./tmp/")  // not ending "/", i.e. "this/path/tmp"
```

## copyFileWithSudo
```go
func copyFileWithSudo(from, to string) {
        // Create directory
        todir := filepath.Dir(to)
        runCommand(t, "sudo", []string{"mkdir", "-p", todir})
        for todir != "/" {
                runCommand(t, "sudo", []string{"chmod", "755", todir})
                todir = filepath.Dir(todir)
        }

        runCommand(t, "sudo", []string{"cp", from, to})
        runCommand(t, "sudo", []string{"chmod", "644", to})
}
```

## Directory Traversal Attack
* https://en.wikipedia.org/wiki/Directory_traversal_attack
* https://github.com/golang/go/issues/25849
* https://github.com/mholt/archiver/pull/65
  * with [this improvement](https://github.com/mholt/archiver/commit/7ef86db1333bd7d433a9ea78f19bbd8cb5007d63#diff-635e4219ee55ef011b2b32bba065606b)
  * change to within(), seems not good because filepath.Rel doesn't work with relative path. [commit](https://github.com/mholt/archiver/commit/d48ce61eb2c501388e99ee300b8c7e622c7cfc88?diff=split)
