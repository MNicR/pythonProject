# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
import scipy
from scipy import stats
import sklearn
from sklearn import linear_model

#import patient numbers data in .csv format => patient_nos_1.csv

patient = pd.read_csv("patient_nos_1.csv")
#print(patient)

#finding null values

#patient_null_value = (patient.isnull().sum())
#print(patient_null_value)

#finding zero values

#patient_zero_value = patient == 0
#print(patient_zero_value)

#file = open ('patient_nos_1.csv', 'r')
#patients_read = file.read()
#file.close()
#print(patients_read)

#cleaning out zero values by removing rows with zero values in them
#patients_cleaned = patient[~(patient == 0).any(axis=1)]
#print(patients_cleaned)

#missing = patient.isnull
#print(missing)

#import average_quarterly_earnings

#average_quarterly_earnings = pd.read_csv("Average_Quarterly_Earnings.csv", index_col=0)
#print(average_quarterly_earnings)

#finding null values

#average_quarterly_earnings_null = (average_quarterly_earnings.isnull().sum())
#print(average_quarterly_earnings_null)

#average_quarterly_earnings_zero = average_quarterly_earnings == 0
#print(average_quarterly_earnings_zero)


#average_quarterly_earnings=average_quarterly_earnings.drop(['Statistic', 'Size of Employees per Enterprise', 'Economic Sector NACE Rev 2', 'UNIT'])

#print(patient.head())
#print(patient.shape)
#print(patient.columns)

#remove columns from dataframe that are not needed for draw the histogram x-axis = quarters for every year; y-axis = patient totals per quarter

df = pd.DataFrame(patient,columns=['Year','week_no','Quarter','date','patient_total_week','patient_total_year','patient_total_quarter'])
df_remove_columns = df.drop(['Year','week_no','date','patient_total_week','patient_total_year']), axis=1)
print(df_remove_columns)


#Draw Histogram to show quarterly patient total differences for every quarter for every year (2007 - 2014)

#x = np.arange(len(patient.head(Quarter)))  # the label locations
#width = 0.35  # the width of the bars

#fig, ax = plt.subplots()
#rects1 = ax.bar(x - width/4, patient_total_quarter, width, label='Quarter 1')
#rects2 = ax.bar(x + width/4, patient_total_quarter, width, label='Quarter 2')
#rects3 = ax.bar(x - width/4, patient_total_quarter, width, label='Quarter 3')
#rects4 = ax.bar(x + width/4, patient_total_quarter, width, label='Quarter 4')


# Add some text for labels, title and custom x-axis tick labels, etc.
#ax.set_ylabel('Patients')
#ax.set_title('Number of Patients')
#ax.set_xticks(x)
#ax.set_xticklabels(labels)
#ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

#fig.tight_layout()

#plt.show()





