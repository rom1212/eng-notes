#/bin/bash

for i in src/* ; do
  if [ -d "$i" ]; then
    #echo "$i"
    dirname=$(basename "$i")
    #echo $dirname
    tar -cvzf ${dirname}.tar.gz $i
  fi
done
