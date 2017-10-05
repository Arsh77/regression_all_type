# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:47:53 2017

@author: ARSHABH SEMWAL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
x =dataset.iloc[: , 1:2].values
y=dataset.iloc[: ,2].values

# features scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x = sc_x.fit_transform(x)
sc_y = StandardScaler()
y = sc_y.fit_transform(y)

#  fitting svr

from sklearn.svm import SVR
regressor =SVR(kernel = 'rbf')
regressor.fit(x , y)

plt.scatter(x , y)
plt.plot(x , regressor.predict(x))
plt.show()

pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([6.5]))))


