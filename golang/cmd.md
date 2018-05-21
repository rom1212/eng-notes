# golang cmd
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
