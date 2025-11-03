import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\DATA SCIENCE\Sept-19th\Sept-19th-Data.csv")
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer()
imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])

from sklearn.preprocessing import LabelEncoder

labelencoder_x = LabelEncoder()
#labelencoder_x.fit_transform(x[:,0])
x[:,0] = labelencoder_x.fit_transform(x[:,0])

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=0)


from sklearn.preprocessing import Normalizer

sc_x = Normalizer()

x_train = sc_x.fit_transform(x_train)


x_test = sc_x.transform(x_test)
