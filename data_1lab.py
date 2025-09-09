import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
 
 
# Read the file
 
cust = pd.read_csv("Advertising.csv")
 
# Let’s checkout the data -
 
print(cust.head())
 
print("No of Rows =" , cust.shape)
 
print("Column names  =" , cust.columns)
 
print("Info         = " , cust.info())
 
sns.pairplot(data=cust)

plt.show()

 