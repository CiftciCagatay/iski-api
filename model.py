# -*- coding: utf-8 -*-

# Import libraries
import numpy as np
import pandas as pd
import pickle

# Import datasets
dataset = pd.read_csv('data.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, 1].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

X_enc = le.fit_transform(X[:, 0])
y_temp = []
n = 7 * 24

for i in range(X_enc.size):
    X_enc[i] = X_enc[i] % n
    a = n * int(np.floor(i / n))
    y_temp.append(y[i] - y[a])
    
X_enc = X_enc.reshape((X.size, 1))

X_train = X_enc[:1000]
y_train = y_temp[:1000]
X_test = X_enc[1000:]
y_test = y_temp[1000:]

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, y_train)

filename = 'model.sav'
pickle.dump(lr, open(filename, 'wb'))