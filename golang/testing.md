# How to Test
## Learn from golang test itself
* for testing exec.Command: https://golang.org/src/os/exec/exec_test.go
* https://joeshaw.org/testing-with-os-exec-and-testmain/

## Test logging
* t.Logf("output: %s", output)

## Mock
* https://medium.com/agrea-technogies/mocking-dependencies-in-go-bb9739fef008
* http://squarism.com/2014/11/28/mocking-in-golang/
* http://goinbigdata.com/testing-go-code-with-testify/
* goconvey: http://callistaenterprise.se/blogg/teknik/2017/03/03/go-blog-series-part4/
* testify vs gomock

## Test exec.Commmand
* https://npf.io/2015/06/testing-exec-command/

## Integration test
https://www.philosophicalhacker.com/post/integration-tests-in-go/
* --short
* --integ (own flag)

## Temporary Directory and File
* io.ioutil.TempDir(dir, prefix)
  * Creates the temporary directory in <dir> with a <prefix>. e.g.
    * ioutil.TempDir("", "fu"): creates a temp directory /tmp/fu12331431243/
* io.ioutil.TempFile(dir, prefix)
  * Creates a temporary file in <dir> with <prefix> (not used this before)
* These are helpful functions even when we need directoires/files be created because it simplifies error check:
```go
func tempDir(t *testing.T) string {
	dir, err := ioutil.TempDir("", "fu")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	return dir
}

func tempFile(t *testing.T) string {
	tempFile, err := ioutil.TempFile("", "fu")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	filename := tempFile.Name()
	if err :=tempFile.Close(); err != nil {
		t.Fatalf("err: %s", err)
	}	
	
	return filename
}
```

* If we just want a tempory file or directory without creating them (or without them being existed)
```go
func tempDir(t *testing.T) string {
	dir, err := ioutil.TempDir("", "fu")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	//Since ioutil.TempDir creates the directory.
	if err := os.RemoveAll(dir); err != nil {
		t.Fatalf("err: %s", err)
	}

	return dir
}

// Code is more work than the below one, but only return one variable for easy cleanup
func tempFile(t *testing.T) string {
	tempFile, err := ioutil.TempFile("", "fu")
	if err != nil {
		t.Fatalf("err: %s", err)
	}
	filename := tempFile.Name()

	if err :=tempFile.Close(); err != nil {
		t.Fatalf("err: %s", err)
	}

	fmt.Println("filename: ", filename)

	if err := os.Remove(filename); err != nil {
		t.Fatalf("err: %s", err)
	}

	return filename
}

// more compact, but needs to return both temporary file and directory if we want to clean it up.
func tempFile(t *testing.T) (string, string) {
	dir := tempDir(t)
	return filepath.Join(dir, "foo"), dir
}

```
* ioutil.go and ioutil_test.go
  * https://github.com/golang/go/blob/master/src/io/ioutil/ioutil.go
  * https://github.com/golang/go/blob/master/src/io/ioutil/ioutil_test.go
  
## Test Working Directory
```go
  func TestGetFilename(t *testing.T) {
    _, filename, _, _ := runtime.Caller(0)
    fmt.Println("Current test filename: " + filename)
  }
```
