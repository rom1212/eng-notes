# apt-cyg
## Install apt-cyg
https://github.com/transcode-open/apt-cyg

## Usage
* apt-cyg install ImageMagick
* convert all jpg files to pdf
```
for file in *.jpg; do convert $file $file.pdf; done

for file in *.jpg; do echo $file $file.pdf; done
```
