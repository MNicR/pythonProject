# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import sklearn
from sklearn import linear_model
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

#patients = pd.read_csv("patient_nos.csv")
average_quarterly_earnings = pd.read_csv("Average_Quarterly_Earnings.csv", index_col=0)

#average_quarterly_earnings=average_quarterly_earnings.drop(['Statistic', 'Size of Employees per Enterprise', 'Economic Sector NACE Rev 2', 'UNIT'])

#missing = patients.isnull
#print(missing)
missing_values_count = average_quarterly_earnings.isnull().sum()
#print(missing_values_count[2:16])




#patients=patients.drop(["field1"], axis=1 )
#print(patients)


#patients=pd.DateFrame(np.random.randn())
#patients.iloc[:18, 2] = NA



#print(patients.head())
#print(patients.shape)
#print(patients.columns)
#print(patients.isnull().sum())
print(average_quarterly_earnings[['Quarter', 'VALUE']])








