# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import sklearn
from sklearn import linear_model
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

patients = pd.read_csv("patient_nos.csv")
missing = patients.isnull
print(missing)
patients[['date', 'total', 'field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9','field10', 'field11', 'field12', 'field13', 'field14', 'field15']] = patients[['Date', 'Total', 'field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9', 'field10', 'field11', 'field12', 'field13', 'field14', 'field15']].fillna(0)
print(patients)

#missing_values_count = patients.isnull().sum()
#print(missing_values_count[2:16])

#patients=patients.dropna(axis = 1, how = 'all')
#cleaned = patients.dropna()

#patients=pd.DateFrame(np.random.randn())
#patients.iloc[:18, 2] = NA



#print(patients.head())
#print(patients.shape)
#print(patients.columns)
#print(patients.isnull().sum())

#print(cleaned)




