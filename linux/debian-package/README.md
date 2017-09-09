# Create Debian Package
## Docs
* Examples
  * http://www.king-foo.com/2011/11/creating-debianubuntu-deb-packages/
  * https://ubuntuforums.org/showthread.php?t=910717
  * https://askubuntu.com/questions/1345/what-is-the-simplest-debian-packaging-guide
* Official
  * http://packaging.ubuntu.com/html/
  * https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-binarycontrolfiles
## Example
```
# In this directory, run
$ dpkg-deb --build helloworld
# You will see helloworld.deb is created.
# To install this package, run
sudo dpkg -i helloworld.deb
# The package is installed in
/usr/local/bin/helloworld.sh
```

## Package Repository
https://www.aptly.info/tutorial/repo/

# Install Debian Package

## Install a deb file
https://unix.stackexchange.com/questions/159094/how-to-install-a-deb-file-by-dpkg-i-or-by-apt
* sudo apt install ./name.deb 
  * pay attention to ./ before name.deb
  * pros: can make use of apt for dry-run, and dependency check
* sudo dpkg -i /path/to/deb/file, sudo apt-get install -f
* gdebi


## Check dependency
### Use apt
This method depends on the output of apt, e.g.
```
apt install ./name.deb --dry-run
```
Find the following lines if there are dependencies not satisfied.
```
The following additional packages will be installed:
```
and
```
2 newly installed
```



