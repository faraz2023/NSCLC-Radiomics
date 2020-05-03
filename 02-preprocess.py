import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pydicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt

DATA_PATH = os.path.join('.', 'lung_data')
patients_ids = [x for x in os.listdir(DATA_PATH) if not x.startswith('.')]
patients_ids.sort()

#patients list is the final product where we have a list, and each element is a:
### dictionary of patient_id, Survival.time as the label, and eventually patient_image
patients_list = []
clinical_df = pd.read_csv('NSCLC Radiomics Lung1.clinical-version3-Oct 2019.csv')
for index, row in clinical_df.iterrows():
    if row['PatientID'] in patients_ids:
        this_patient_dict = {'patient_ID': row['PatientID'],
                             'survival_time': row['Survival.time']}
        patients_list.append(this_patient_dict)


print(patients_list)

#print(patients)

def load_scan(path):
    slices = [pydicom.dcmread(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    try:
        slice_thickness = np.abs(slices[0].ImagePositionPatient[2] - slices[1].ImagePositionPatient[2])
    except:
        slice_thickness = np.abs(slices[0].SliceLocation - slices[1].SliceLocation)

    for s in slices:
        s.SliceThickness = slice_thickness
        if s.AccessionNumber == '':
            s.AccessionNumber = "Blank_Accession_Number"

    return slices

# gets a list of patient names
#returns a dictionary where the key of each element is a patient ID and the value of each key is a list of all patient slices
def compelete_patient_reports(patients):
    all_patients_studies = {}
    for patient in patients:
        this_patient_path = os.path.join(DATA_PATH, patient)
        this_patient_slices = load_scan(this_patient_path)
        all_patients_studies[this_patient_slices[0].PatientName] = this_patient_slices

    return all_patients_studies

# Taking care of Hounsfield Unit (HU)
def get_pixels_hu(slices):

    image = np.stack([s.pixel_array for s in slices])

    # int16 should be enough for the pixel data. We use it to save memory
    image = image.astype(np.int16)

    # Set outside-of-scan pixels to 0 (in some machines it is set to -2000)
    # The intercept is usually -1024, so air is approximately 0
    image[image == -2000] = 0

    # Convert to Hounsfield units (HU)
    for slice_number in range(len(slices)):

        intercept = slices[slice_number].RescaleIntercept
        slope = slices[slice_number].RescaleSlope

        if slope != 1:
            image[slice_number] = slope * image[slice_number].astype(np.float64)
            image[slice_number] = image[slice_number].astype(np.int16)

        image[slice_number] += np.int16(intercept)

    return np.array(image, dtype=np.int16)

# visualizes a single patient. Two graphs: 1. Histogram for pixel hu ; 2. Image for
def single_patinet_visualization(patient):
    patient_scan = load_scan(os.path.join(DATA_PATH, patient))
    patient_pixels = get_pixels_hu(patient_scan)
    plt.hist(patient_pixels.flatten(), bins=80, color='c')
    plt.xlabel("Hounsfield Units (HU)")
    plt.ylabel("Frequency")
    plt.show()

    # Show a random slices
    plt.imshow(patient_pixels[30], cmap=plt.cm.gray)
    plt.show()

single_patinet_visualization(patients_list[0]['patient_ID'])


#print(compelete_patient_reports(patients).keys())