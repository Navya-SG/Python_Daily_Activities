**GitHub -** https://github.com/Navya-SG/First\_trial.git

 	 git@github.com:Navya-SG/First\_trial.git

### **GIT**



**GIT** - called as version control



**version control system** - tool to manage changes in files over time.



**uses - VCS**

* maintain complete history of changes - include who/when - made
* revert to prev versions - when error occurs/rollback needed
* work collaboratively - parallel, wihtout overwriting
* identify and resolve conflicts - ensure - merged changes are accurate/consistent



**TYPES - VCS**

**1.Local version control**

 	-> simple but risky

 	-> changes tracked by own comp only

 	-> system crash - data lost

 		**eg**: saving multiple copies manually



**2.Centralized version control (CVCS)**

 	-> one main server - hold all files

 	-> anyone can access files

 	-> id server fail - all data lost

 		**eg**: subversion(SVN),perforce



**3.Distributed Version Control (DVCS)**

 	-> everyone has full copy of history

 	-> track changes in offline too

 	-> safe \& faster

 	-> if one system crashes, others still have copy

 		**eg**: Git



**Key concepts of VCS**

* **Repository** - folder, tract changes
* **Commit** - snapchat of proj/file, along with msg of what changed
* **Branch** - side-path where you try something new,without affecting main work
* **Merge** - 2 path(branch) together
* **Conflict** - when 2 people change same part(VCS ask - which change to keep?)
* **Log** - history of all commit, show what/who - changed



**what is GIT?**

 -> **distributed VCS** - every contributer has complete copy of file

 -> helps - tracK changes/collaboration/keep history

 -> fast,efficient,flexibility



**GIT**-> Standard choice - open source \& professional development



**History**

 - April,2005 - Linus Torvald

 - 2008 - GitHub launched



**GIT INSTALLATION**



**GIT WORKING**



**GIT REPOSITORY**

git init -> initiating git (start tracking changes)

git commit -m -> saves snapshot of your staged changes with descriptive msg(-m)

git checkout -b(branch name 1st time creating use "" or without "") -> create new branch or to switch branch

git status -> to check status (modifications)

git add . -> staging(selecting what to include to main repo) and marked for snapshot

git log -> to see who did what changes,when,why

git push -> uploads local branch to remote repository(from git,github)

git pull -> downloads and merges the latest change in remote repository

git clone -> clone existing repository completely

git fetch -> doesnot merge

git branch -> shows in which branch we are

git checkout (head branch name),git merge (branch name)-> combines changes from diff branches into one unidified branch

git mergetool ->



**remote repository(work only after creating)** -> git fetch, git pull, git push, git clone



**GITHUB** -> remote hosting platform

       -> host and collaborate online repo



**GIT Advanced command**



git rebase main -> takes latest version of main

git cherry-pick -> pick particular commit from another branch and applies to current branch (git commit coo3\[the specific commit id is mentioned])

git cherry-pick --continue -> to clear the conflict created due to commit id

git reset -> rewrites commit history, completely removes

git reset --soft HEAD~1 -> moves head back by 1 commit,keep changes in staging area,files still marked for commit

git reset --mixed HEAD~1 -> changes moved to working directory

git reset --hard HEAD~1 -> removes everything

git revert -> create new commit created on main branch that undones the old one, use on public

git restore -> restores the current working copy with last committed version, discarding any uncommitted changes

git clean -> to unorder thing

git clean -f -> untracked files

git clean -fd -> delete untracked files and directories

git clean -n -> deletes anything

git diff -> changes made latest

git blame -> who modified each line

git stash -> can't commit this half-finished experiment, so temporarily saves working directory and index state WIP on main

git stash pop -> delete the stash, most recent stash

git tag <tag\_name> -> mark release points-great for versioning, label current command



**GIT - combine work**

**-> Merge**(preserve history) - latest update in any branch only merged to main branch

**-> Rebase**(linear history) - update in each separate branch is updated in main branch



**GIT - TEAM COLLOBORATION**

**key features** -> issues

 	     -> pull request



**Git issue** -  way to track tasks, bugs, questions - like digital to\_do\_list for repository



**PULL REQUEST (PR)**

way to propose changes from one branch into another and ask for review before merging.(review and approve)

**Steps:**

git add .

git commit -m "message"

git push origin "name"



**GIT BRANCHING - TEAM STRUCTURE**



**NAMING CONVERISONS**

**main/master ->** production ready code

**feature1/,feature2/,.. ->** new features

**hotfix/ ->** immediate fix to production

**release/ ->** final testing

**develop/ ->** integration of all completed features



**GIT FLOW WORK FLOW**

structured workflow best suited for proj - clear versioned released cycles

**\[feature - develop - release - main]**



**TRUNC BASED DEVELOPMENT**

-> developers commit directly or via very short lived branches

-> use feature flags



**GIT IGNORE/ATTRIBUTE**

ignore - files,folders



**CI/CD** - continuous integrity,development

