# Quotes
## Quote 1
* https://www.quora.com/What-is-the-best-backend-language-to-learn-for-web-app-development

### ===
Bearing this requirement on mind, you will find that any of other popular languages has some shortcomings. Php is outdated, difficult to separate business logic from presentation and not fast. Python and RoR are very easy to use but way too slow. Node.js meets the performance requirement but is hard to debug and build large sites as it’s a dynamic language and sometime unpredictable in results. Java and C# are cumbersome and only medium in performance though either is mature, easy to use and hire hands. While Erlang is robust and suitable for some scenarios, its syntax and mindset deviate far from the main stream, making it hard to learn.

Like Java and C#, Golang is static, easy to learn and use, and backed by a top firm with large resources, but faster, more flexible, and lighter. Last and not least important, its compiled executive binaries are free of library dependency on linux, making deployment way too easy.

### === 

## Quote 2
https://www.quora.com/What-are-the-advantages-and-disadvantages-of-Golang

### ===
Sometimes there may be more lines of code, but brevity is often not a virtue when it comes to producing reliable, reusable and readable code.

My comments: For example: exceptions are good to use, however, it is hard to find out where are the exceptions thrown in a funciton by just reading the code.

### ===

# Docs
* https://www.toptal.com/back-end/server-side-io-performance-node-php-java-go
  * Server-side I/O Performance: Node vs. PHP vs. Java vs. Go
  * good article about Non-blocking I/O
  
# Windows
## path
* default GOPATH is c:\users\xxxx\go\
* GOROOT (C:\go) is used to find out the stardard package (which is built-in go packages). If there is warning about a standard package imprting a non-standard package, that means some code in C:\go is importing something in c:\users\xxxx\go
