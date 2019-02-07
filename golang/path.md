# golang path
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

## 
* https://github.com/golang/go/issues/25849
* https://github.com/mholt/archiver/pull/65
  * with [this improvement](https://github.com/mholt/archiver/commit/7ef86db1333bd7d433a9ea78f19bbd8cb5007d63#diff-635e4219ee55ef011b2b32bba065606b)
  * change to within(), seems not good because filepath.Rel doesn't work with relative path. [commit](https://github.com/mholt/archiver/commit/d48ce61eb2c501388e99ee300b8c7e622c7cfc88?diff=split)
