# Make file
## Docs
* www.gnu.org/software/make/manual/make.html
  * "default goal" - default target: 
    * "By default, make starts with the first target (not targets whose names start with ‘.’). This is called the default goal. "
## Example
Make sure use tab for the lines below target.
```
default:
        @echo "Usage: To check code, run: make check"
check:
        ./check-code.sh
build:
        mvn package
clean:
        mvn clean
```

## Suppress output from commands with @ in the beginning of the line.
```
run:
     @java myprogram
```     
