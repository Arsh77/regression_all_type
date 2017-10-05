# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 03:23:06 2017

@author: ARSHABH SEMWAL
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
x = dataset.iloc[:, 1:2]
y = dataset.iloc[: ,2]

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x,y)
y_pred=regressor.predict(6.5)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 5)
x_poly = poly_reg.fit_transform(x)
regressor2 = LinearRegression()
regressor2.fit(x_poly , y)

"""
x_grid = np.arange(1 , 10 , 0.01)
x_grid = x_grid.reshape(len(x_grid) , 1)

plt.scatter(x, y , color = 'red')
plt.plot(x_grid , regressor2.predict(poly_reg.fit_transform(x_grid)) , color = 'blue')
plt.title('polynomial regression')
plt.xlabel('level')
plt.ylabel('salary')
plt.show()
"""
y_pred2 = regressor2.predict(poly_reg.fit_transform(6.5))
