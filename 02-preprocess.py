import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pydicom
import os
import scipy.ndimage
import matplotlib.pyplot as plt

data_path = os.path.join('.', 'lung_data')
patients = [x for x in os.listdir(data_path) if not x.startswith('.')]
patients.sort()

print(patients)

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

#returns a dictionary where the key of each element is a patient ID and the value of each key is a list of all patient slices
def compelete_patient_reports(patients):
    all_patients_studies = {}
    for patient in patients:
        this_patient_path = os.path.join(data_path, patient)
        this_patient_slices = load_scan(this_patient_path)
        all_patients_studies[this_patient_slices[0].PatientName] = this_patient_slices

    return all_patients_studies


#print(compelete_patient_reports(patients).keys())