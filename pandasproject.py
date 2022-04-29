#!/usr/bin/env python3
#Jeremiah Williams

import pandas as pd

d = pd.read_csv('mobile_os_usage.csv', sep='\t')

#What is the shape of the data set?

print (d.shape)
print (" ")

#What columns are available in the data set?

print (" ")
print ("------------------------------------")
print (d.columns)

#What are the first 5 values in the dataset?

print (" ")
print ("--------------------------------------")
print (d.head())

#What is the last row in the data set?
print(" ")

row_number = d.shape[0]
get_last =row_number - 1
print(d.loc[get_last])

#What are the values of rows 34, 66, and 53?
print(" ")
print(d.iloc[[33,65,52]])