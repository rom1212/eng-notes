# golang path
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
