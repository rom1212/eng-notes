# Signal
* code/doc
  * https://golang.org/pkg/os/signal/
  * https://golang.org/src/syscall/syscall_linux.go?s=6754:6776#L270
* https://github.com/golang/go/issues/19798
* convert Signal to WaitStatus, where if it is not stopped or exited, its value is the Signal
  * However, somehow, the child process can choose to eat the signal and return 0.
