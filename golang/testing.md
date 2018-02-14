# Temporary Directory and File
* io.ioutil.TempDir(dir, prefix)
  * Creates the temporary directory in <dir> with a <prefix>. e.g.
    * ioutil.TempDir("", "fu"): creates a temp directory /tmp/fu12331431243/
* io.ioutil.TempFile(dir, prefix)
  * Creates a temporary file in <dir> with <prefix> (not used this before)
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

// returns both temporary file and directory if we want to clean it up.
func tempFile(t *testing.T) (string, string) {
	dir := tempDir(t)
	return filepath.Join(dir, "foo"), dir
}

```
