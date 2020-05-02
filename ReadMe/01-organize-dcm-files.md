# 01-organize-dcm-files

The original NSCLS data is messy. Each patient has two subdireories and each subdirectory you will find more subdirectories. 
This script **moves** each patient's data into a respective patient directory in the output folder (currently designated as "*lung_data*"). 

You should be careful when using the script as it **moves** the data and does not just **copy** it. 

I have used **os** and **shutil** to do the work. 

The rest is documented withing the script
