# golang cmd
## Run command
```go
func runCommand(t *testing.T, command string, args []string) {
        cmd := exec.Command(command, args...)
        out, err := cmd.CombinedOutput()
        if err != nil && testing.Verbose() {
                fmt.Println("command:", command, args, ", output:", string(out))
        }
        assert.NoError(t, err)
}
```

## Set working directory
https://stackoverflow.com/questions/43135919/how-to-run-a-shell-command-in-a-specific-folder-with-golang
```go
cmd:= exec.Command("git", "log")
cmd.Dir = "your/intended/working/directory"
out, err := cmd.Output()
```
