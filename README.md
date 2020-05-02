# NSCLC-Radiomics
The repo where I keep my project for NSCLC-Radiomics data analytics

# Current Organization
You will find python scripts with number prefixes. The numbers indicate the order of execution for processing the data. 
It is assumed that you have downloaded the data from here: [NSCLC-Radiomics] (https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics) and have the data at the same direcotry as the github repo. 

## Instructions

You will find summary of code behaviour here. In addition, you can also find a detailed account of what each script does and use in **ReadMe** folder of the repo. 

## Technologies

Python is the main tool that I have utlized for this project. You can find the environment file in **Z-Conda-Env** and replicated my environment. 
# Code Overview

### 01-organize-dcm-files.py
This script is dedicated to moving all the *.dcm* files for each patient in an immidiate subdirectory for the patient. The original data is messy in this matter and many directories and sub-directories makes file system traversal very difficult. 
