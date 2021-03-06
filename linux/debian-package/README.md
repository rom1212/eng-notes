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
  * check installed packages: dpkg --get-selections
  * to uninstall: sudo dpkg -r <package name, e.g. helloworld>
* gdebi

## Check  Installed Packages
* apt list --installed
* dpkg --get-selections | grep -v deinstall


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
x newly installed   # where x is equal or larger than 2
```

### Use dpkg-deb
* find out the depends of a debian file
```
dpkg-deb -f helloworld.deb Depends
```
* find out the installed debian packages
https://askubuntu.com/questions/17823/how-to-list-all-installed-packages
```
dpkg --get-selections | grep -v deinstall
```
* cons: it's not straight forward to check the versions.

# Cleanup Debian Package
## Never needed packages
```
sudo apt autoremove
```
## Remove or Purge ???
https://unix.stackexchange.com/questions/118880/should-i-use-apt-get-remove-or-apt-get-purge
