#importing all the required packages

import sys
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import googletrans

#reading data
myData = pd.read_csv('amazon.csv',thousands='.')

#describing the data
dataDesc = myData.describe(include="all")

#checking for missing values
myData.isna().sum()

#Breaking into smaller values
myData=myData.replace(to_replace = 0, value=np.nan)
myData.shape
newData = myData.dropna(subset =['number'])
newData.shape
newData.describe(include='all')
months = list(newData.month.unique())
forestFirePerMonth = newData.groupby('month')['number'].sum()
print(forestFirePerMonth)
print(months)
