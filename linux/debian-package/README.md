# Create Debian package
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
