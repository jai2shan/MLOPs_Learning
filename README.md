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

#### Git

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

Create a new commit containing the current contents of the index and the given log message describing the changes.   
___

    git push origin main 
Updates remote refs using local refs, while sending objects necessary to complete the given refs.   
___  
    ## Creating new branch   
    git checkout -b <new branch name>

Creating new branches in git  
___

    ## switching to existing branch
    git checkout <branch name>
Switching to existing branches
___

    ## get all the branches from the git online repo
    git fetch --all

Fetch branches and/or tags (collectively, "refs") from one or more other repositories, along with the objects necessary to complete their histories. Remote-tracking branches are updated

###  Why is Version Control necessary?
> Backing up Code       
    
    git log
To view list of all commits

    git log --stat
To view details in logs
    
    git log --pretty=oneline
View all logs in one line

    git log --pretty=format:"%h %s" --graph

> Sharing   
> Reverting Code   

User can trace back to any commits made in the past

> Collaboration

### Why regular version control is not enough for ML?
![alt text](images/PROGRAMMINGvsML.png "Title")

## 2. Data Version Control(DVC)

In order to have reproducibility, consistent version tracking is essential. In the traditional software world, versioning code is enough because all behavior is defined by it. 

In ML, we also need to track model versions, along with the data used to train it, and some meta-information like training hyperparameters. 

We can track models and metadata in a standard version control system like Git, but data is often too large and mutable for that to be efficient and practical. It's also important to avoid tying the model lifecycle to the code lifecycle since model training often happens on a different schedule. The common reasons when ML model and data changes are:

> The model can be retrained based upon new training data   
Models may be retrained based on new training approaches   
Models may be self-learning     
Models may be deployed in a new application     
Models may be subject to attack and require revision    
Models might be rolled back to a previous serving version       
Companies/Government compliance may require audit or investigation on both ML model and data, hence we need access to all versions of the productionized ML model.      
Data may be able to reside in a restricted jurisdiction     
Data storage may not be immutable         

### Model Validation

Standard DevOps practice is test automation, usually in the form of unit tests and integration tests. Passing these tests is a prerequisite to deploying a new version. Having a comprehensive automated test can give a team great confidence, dramatically accelerate the pace of production deployments.

ML models are harder to test because no model gives 100% correct results. This means model validation tests need to be necessarily statistical in nature, rather than having a binary pass/fail status. In order to decide whether a model is good enough for deployment, one needs to decide on the right metrics to track the threshold of their acceptable values, usually empirically, and often by comparison with previous models or benchmarks. 


    Data Version Control, or DVC, is a data and ML experiment management tool that takes advantage of the existing engineering toolset that you're already familiar with (Git, CI/CD, etc.).

    DVC can be used as a Python library, simply install it with a package manager like pip or conda. Depending on the type of remote storage you plan to use, you might need to install optional dependencies: s3, azure, gdrive, gs, oss, ssh, etc.


[Please use this link to configure DVC](https://dvc.org/doc/install)

DVC's features can be grouped into functional components:

> Data and model versioning   
Data and model access       
Data pipelines      
Metrics, parameters and plots       
Experiments     

