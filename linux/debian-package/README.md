# Create Debian package
## Docs
* http://www.king-foo.com/2011/11/creating-debianubuntu-deb-packages/
* https://ubuntuforums.org/showthread.php?t=910717
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
