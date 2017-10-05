# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 13:42:09 2017

@author: ARSHABH SEMWAL
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("Data.csv")

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2)

"""
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
"""

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)
pred_y=regressor.predict(X_test)
plt.scatter(X_train,Y_train)
plt.plot(X_train, regressor.fit(X_train))
