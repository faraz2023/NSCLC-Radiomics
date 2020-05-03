# NSCLC-Radiomics
The repo where I keep my project for NSCLC-Radiomics data analytics. You can find a history of this readme file at ReadMe/Z-readme_archive

# Current Organization
v0.1 is not posted. You can open the notebook and follow the steps

## Instructions
The notebook has been written with full documentation. You can review the steps of the code there. 

My tool set does not include anything fancy, but for eas of use I have added my Conda env file. 
You can clone my environment with command:
```
conda env create -f ./Z-CondaEnv/ims_mini_project_env.yml

```

## Technologies

Python is the main tool that I have utlized for this project. You can find the environment file in **Z-Conda-Env** and replicated my environment. 
# Code Overview

### 01-organize-dcm-files.py
This script is dedicated to moving all the *.dcm* files for each patient in an immidiate subdirectory for the patient. The original data is messy in this matter and many directories and sub-directories makes file system traversal very difficult. 
