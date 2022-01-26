# <center> MLOPs </center> 

## Table of Contents

1. Version Control   
2. Git
3. Data Version Control(DVC)
4. Unit Testing in Python


## 1. Version Control

### What is Version Control ?
     
Version Control is used to track and control changes to source code. It is an essential tool to ensure the integrity of the codebase. Version control facilitates a continuous, simple way to develop software.

We have many resources online available to know the importance of version control. 

#### Creating a repository

Git commands to get familiar with   
    
    git status
1. The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. 
2. Status output does not show you any information regarding the committed project history.
_____

    git add <filename>
    <or>
    git add .

1. This command updates the index using the current content found in the working tree, to prepare the content staged for the next commit. 
2. It typically adds the current content of existing paths as a whole, but with some options it can also be used to add content with only part of the changes made to the working tree files applied, or remove paths that do not exist in the working tree anymore.
___

    git commit -m "<message you want to add to retrack the commits>"
    
    ## Replace master in the below message based on the branch you are working with
    git push origin master 

    ## Creating new branch
    git checkout -b <new branch name>

    ## switching to existing branch
    git checkout <branch name>

    ## get all the branches from the git online repo
    git fetch --all
    


###  Why is Version Control necessary?
> Backing up Code   
> Sharing and reusing code  
> Reverting Code    
> Collaboration




