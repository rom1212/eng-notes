# docs
* https://www.mercurial-scm.org/guide

# hg basic commands
* hg status
* hg diff
  * difference between two commits/revisions
  ```
  hg diff -r <commit2> -r <commit1>
  ```
* hg add
* hg commit -m ""
  * only change the message, and and edit opens for multi-line message: ```hg commit --amend```
* hg amend
* hg help extensions: can find out what are the enabled extensions.
* hg update <commit>:
  * make the <commit> as the working commit.

# hg advanced commands
* git reset: ```hg strip --keep -r .```

Need to enable strip extension in ~/.hgrc
```
# ~/.hgrc
[extensions]
strip =
```
* merge commits: 
  * merge and keep old nodes (commits): 
  ```
  # alias hgfold='hg histedit --keep'
  hg histedit --keep <commit>
  ```
  * simple merge: ```hg histedit <commit>```
  * enable
  ```
  # ~/.hgrc
  [extensions]
  histedit =
  ```
 
