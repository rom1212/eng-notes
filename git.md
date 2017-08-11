# git config for ssl and proxy
```
git config --global http.sslVerify false
git config --global https.sslVerify false
git config --global http.proxy http://10.xx.xx.xx:3128
git config --global https.proxy http://10.xx.xx.xx:3128
```

# commands
* git push
  * git push origin xxx
    * where xxx might be the same name of the branch name.
    * After the first push, i.e. the remote branch has been created, we can just use git push ???TTT
* git log
  * output to file with diff info: ```git log -p [file name] > log.txt```
* git show
  * show a file at a given commit:
    ```
    git show <commit>:<path/to/file>, e.g. git show 3d5axxxxxyyyxyxyxy5680:pom.xml
    ```
  * only show filenames:
    ```
    git show --name-only <commit id>
    ```
* git diff
  * git diff mingzhao..master (use .. instead of ..., which might cause problems, e.g. mingzhao...master and master...mingzhao are different)
  * git diff --name-only mingzhao..master
  * git diff <commit a> <commit b> [filename]
* git branch -r  : remote branches
* merge local commits into one
  * git rebase -i HEAD~5 # merge the last 5 commits. Use "pick" for the first commit (most recent), and use "squash" or "s" for the other previous commit
  * It will prompts about the commit message, and we can edit that.
  * Seems that this doesn't have anything to do with master branch. To rebase with master, we need to use "git rebase master"
* git revert commit_id
  * it automatically creates a commit which does the reversion.
