# Makefile
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

# Environment variable
* check whether an environment variable is set or not
```
${STATE?"Need to set STATE"}
${DEST:?"Need to set DEST non-empty"}
```
The first variant (using just ?) requires STATE to be set, but STATE="" (an empty string) is OK — not exactly what you want, but the alternative and older notation.

Refs:
  * https://stackoverflow.com/questions/307503/whats-a-concise-way-to-check-that-environment-variables-are-set-in-a-unix-shell
  * http://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion

# Other Linux distributions
* https://www.whonix.org/, secure Linux for surfing internet.

# systemd
* https://linoxide.com/linux-how-to/systemd-boot-process/
* https://unix.stackexchange.com/questions/47695/how-to-write-startup-script-for-systemd

# simple email server
* yum install -y mailx
