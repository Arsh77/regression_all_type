# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:16:53 2017

@author: ARSHABH SEMWAL
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')

x=dataset.iloc[: ,:-1].values
y=dataset.iloc[:,4].values

#encode the text in the dataset using labelencoder and onehotencoder
#---------------------------------x---------------------------------x------------------------
#applying class LabelEncoder from preprocessing library
from sklearn.preprocessing import LabelEncoder
labelencoder_x=LabelEncoder()
x[:,3]=labelencoder_x.fit_transform(x[:,3])
#aplyinh OneHotEncoder on x 
from sklearn.preprocessing import OneHotEncoder
onehotencoder_x=OneHotEncoder(categorical_features = [3])
x=onehotencoder_x.fit_transform(x).toarray()

#removing dummy variable trap
x=x[:,1:6]

from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)

one=np.ones((50,1)).astype(int)

# creating optimum model by backward elimination
# 'astype' is used change datatype from float to int 
x = np.append(arr = one , values = x , axis = 1)

import statsmodels.formula.api as sm
x_opt = x[:, [0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y , exog = x_opt ).fit()
regressor_OLS.summary()

x_opt = x[:, [0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y , exog = x_opt ).fit()
regressor_OLS.summary()

x_opt = x[:, [0,3,4,5]]
regressor_OLS = sm.OLS(endog = y , exog = x_opt ).fit()
regressor_OLS.summary()

x_opt = x[:, [0,3,5]]
regressor_OLS = sm.OLS(endog = y , exog = x_opt ).fit()
regressor_OLS.summary()

x_opt = x[:, [0,3]]
regressor_OLS = sm.OLS(endog = y , exog = x_opt ).fit()
regressor_OLS.summary()

x_opt_train , x_opt_test ,y_train , y_test= train_test_split(x_opt , y , test_size = 0.2, random_state=0)
regressor_lr = LinearRegression()
regressor_lr.fit(x_opt_train , y_train)
y_opt_pred = regressor_lr.predict(x_opt_test)



