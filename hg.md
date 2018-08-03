# hg basic commands
* hg status
* hg diff
* hg add
* hg commit -m ""
* hg amend
* hg help extensions: can find out what are the enabled extensions.
* hg update <commit>:
  * make the <commit> as the working commit.

# hg advanced commands
* git reset: ```hg strip --keep -r .```

Need to enable strip extension in ~/.hgrc
```
[extensions]
strip =
```
* merge commits: ```hg histedit <commit>```
```
[extensions]
histedit =
```
