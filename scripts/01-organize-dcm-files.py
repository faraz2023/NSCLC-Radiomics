# PLEASE NOTE: This script can completely change your data's file system by moving, and not compying dcm files. Please use carefully
# We move modify the files system so at the end we get the slices of each patient scan in a single subdirectory
# in the end, we have "./lung_data/LUNG1-???/*.dcm" for each patient

import os
import shutil

# Create the output folder
output = os.path.join(".", "lung_data")
if not os.path.exists(output):
    os.mkdir(output)

# The data path, based on classical folder namings
data_path = os.path.join('.', 'classical_names')
data_path = os.path.join(data_path, 'NSCLC-Radiomics')


# We iterate over single patients
for patient in os.listdir(data_path):

    # check to see if actually a patient folder
    if patient.startswith('LUNG1-'):
        patient_path = os.path.join(data_path, patient)

        # iterating patient's subdirectories
        for fol in os.listdir(patient_path):

            # get the directory with all the slices
            if(fol.startswith('1.3.6.1.4.1.3')):

                # prepare for moving the .dcm files by creating a respective output directory
                patient_slices_path = os.path.join(patient_path, fol)
                patient_output = os.path.join(output, patient)
                os.mkdir(patient_output)

                #there is a subdirectory that we need to traverse
                for single_folder in os.listdir(patient_slices_path):
                    if not single_folder.startswith('.'):
                        patient_slices_path = os.path.join(patient_slices_path, single_folder)

                        #move all dcm files to respective output folder
                        for dcm in os.listdir(patient_slices_path):
                            shutil.move(os.path.join(patient_slices_path, dcm), patient_output)