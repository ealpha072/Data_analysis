#importing all the required packages

import sys
import pandas as pd 
import matplotlib.pyplot as plt
#import googletrans

#reading data
myData = pd.read_csv('amazon.csv',thousands='.')
