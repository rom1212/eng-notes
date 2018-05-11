# git config for ssl and proxy
* doc: https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration
```
git config --global http.sslVerify false
git config --global https.sslVerify false
git config --global http.proxy http://10.xx.xx.xx:3128
git config --global https.proxy http://10.xx.xx.xx:3128
```

If there is no color (e.g. git diff doesn't show color on CentOS),
```
git config --global color.ui true
```

# commands
* check repo and branches
  * git remote -v 
  * git branch -r (--remote)
* git push
  * git push origin xxx
    * where xxx might be the same name of the branch name.
    * After the first push, i.e. the remote branch has been created, we can just use git push ???TTT
  * push to a new repo, e.g. bb
    * git remote add bb https://github.com/xxx/teletraan.git
    * git push bb branch_name
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
  * git diff mingzhao..master (use .. instead of ..., which might cause problems, e.g. mingzhao...master and 
     master...mingzhao are different)
  * git diff --name-only mingzhao..master
  * git diff <commit a> <commit b> [filename]
* git branch -r  : remote branches
* merge local commits into one
  * git rebase -i HEAD~5 # merge the last 5 commits. Use "pick" for the first commit (most recent), and use "squash" or "s"
    for the other previous commit
  * It will prompts about the commit message, and we can edit that.
  * Seems that this doesn't have anything to do with master branch. To rebase with master, we need to use "git rebase master"
* amend (merge commit to the previous one)
  * git commit --amend  (optional -a, -m). It prompts to change the message, just Ctrl-X)
* git revert commit_id
  * it automatically creates a commit which does the reversion.
* ```git cherry-pick <commit>```
  * where ```<commit>``` is usually from another branch 
* get current branch name
  * ``` CBN=`git rev-parse --symbolic-full-name --abbrev-ref HEAD` ```
* git rebase vs git reset
  * git reset --hard <commit>
  * git rebase master
* quickly clean up repository
  * rm -rf . 
  * git reset --hard
 

# Keep a fork up to date
https://gist.github.com/CristinaSolana/1885435
* Clone your fork:
```
git clone git@github.com:YOUR-USERNAME/YOUR-FORKED-REPO.git
```
* Add remote from original repository in your forked repository: 
```
    cd into/cloned/fork-repo
    git remote add upstream https://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git  # or git remote add upstream git://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git
    git fetch upstream
```    
* Updating your fork from original repo to keep up with their changes:
```
git pull upstream master
```

# PR after Review
Case: after sending out PR, upstream also changed. If we only update changed files, PR will not compare with the newest upstream file, and so we musht somehow sync our patch branch with the base branch. 

We cannot do rebase for our patch, because our patch is alread pushed, and rebase will make local diverge from remote, and we cannot push the changes with after rebase. Not sure why we can push the merged commits, but cannot push rebased commits??? TTT - rebase changes the parent and merge doesn't??? not sure.

However, we can still forcely push the changes to the patch branch, e.g.
```
git remote add upstream https://github.com/xxx/xxx.git
git fetch upstream  # this is fetch, not pull because pull will do the merge.
git checkout patch-n
Options 1) git rebase -i upstream/master  
# If there are so many changes, rebase could be a headach. We can redo our changes
Options 2) git reset --hard xxx, git merge upstream/master, redo our changes.
git push origin patch-n --force (or -f)
```

Merge is also an option, but it could mess-up the base.
```
git remote add upstream https://github.com/xxx/xxx.git
git fetch upstream  # this is fetch, not pull because pull will do the merge.
git checkout patch-n
git merge upstream/master
```

It might have problem when doing the merge for the upstream master, because upstream needs to figure out how to merge and do the squash so that my changes/commits will appear mostly as one commit in the master.

github provides three options:
* Merge: which is basically "git merge"
* squash and merge: which is "git merge --squash"
* rebase

# git for windows
* download: https://git-scm.com/download/win or https://git-scm.com/download/win
* how to install: http://www.techoism.com/how-to-install-git-bash-on-windows/
* credential manager
  * https://github.com/Microsoft/Git-Credential-Manager-for-Windows/blob/master/Docs/CredentialManager.md
  * remove stored credential  (one for a URL)
    * git credential-manager remove
    * git credential-manager clear (safter to run twice)
