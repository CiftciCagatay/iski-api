# -*- coding: utf-8 -*-
import pickle
import matplotlib.pyplot as plt

filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))

plt.scatter(X_train, y_train, color = 'red', alpha = 0.1)
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, y_test, color = 'orange', alpha = 0.1)
plt.plot(X_train, model.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()