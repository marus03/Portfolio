import numpy as np
import pandas as pd
import matplotlib as plt


data = "onlinefoods.csv"
df = pd.read_csv(data)



# flash at our dataset

pd.set_option('display.max_columns', None)
print(df.head())
# shape of our dataset
shape = df.shape
print(shape)
print(df.info())

# Data cleaning
print(df.isnull().values.any())
# Output: False -> There are no missing values in the entire dataset and we don't need to find them.
