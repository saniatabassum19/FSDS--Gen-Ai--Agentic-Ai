import os
import pickle
from sklearn.metrics import mean_squared_error
import scipy.stats as stats
from scipy.stats import variation
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

dataset = pd.read_csv(
    r"C:\Users\DELL\OneDrive\Desktop\DATA SCIENCE\Sept-22 simple linear regression\Salary_Data.csv")


x = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

comparison = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(comparison)

plt.scatter(x_test, y_test, color='red')  # Real salary data (testing)
# Regression line from training set
plt.plot(x_train, regressor.predict(x_train), color='blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


m = regressor.coef_
print(m)

c = regressor.intercept_
print(c)

y_12 = m * 12 + c
print(y_12)

y_20 = m * 20 + c
print(y_20)

y_10 = m * 10 + c
print(y_10)


plt.scatter(x_train, y_train, color='red')  # Real salary data (training)
plt.plot(x_train, regressor.predict(x_train),
         color='blue')  # Predicted regression line
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# ==== best fit line hear ( what next )

coef = print(f"Coefficient: {regressor.coef_}")

intercept = print(f"Intercept: {regressor.intercept_}")

# future prediction code

exp_12_future_pred = 9312 * 100 + 26780
exp_12_future_pred

bias = regressor.score(x_train, y_train)
print(bias)

variance = regressor.score(x_test, y_test)
print(variance)

# can we implement statsticc to this dataset

dataset.mean()

dataset['Salary'].mean()

dataset.median()

dataset['Salary'].median()

dataset['Salary'].mode()

dataset.var()

dataset['Salary'].var()

dataset.std()

# for calculating cv we have to import a library first
variation(dataset.values)  # this will give cv of entire dataframe

variation(dataset['Salary'])  # this will give us cv of that particular column

dataset.corr()

# this will give us correlation between these t
dataset['Salary'].corr(dataset['YearsExperience'])

dataset.skew()  # this will give skewness of entire dataframe

dataset['Salary'].skew()  # this will give us skewness of that particular colum

dataset.sem()  # this will give standard error of entire dataframe

# this will give us standard error of that particular column
dataset['Salary'].sem()

# for calculating Z-score we have to import a library first
dataset.apply(stats.zscore)  # this will give Z-score of entire dataframe

# this will give us Z-score of that particular column
stats.zscore(dataset['Salary'])

a = dataset.shape[0]  # this will gives us no.of rows
b = dataset.shape[1]  # this will give us no.of columns
degree_of_freedom = a-b
# this will give us degree of freedom for entire dataset
print(degree_of_freedom)

# First we have to separate dependent and independent variables
X = dataset.iloc[:, :-1].values  # independent variable
y = dataset.iloc[:, 1].values
# dependent variable
y_mean = np.mean(y)  # this will calculate mean of dependent variable
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=0)
reg = LinearRegression()
reg.fit(X_train, y_train)
# before doing this we have to train,test and split our
y_predict = reg.predict(X_test)
SSR = np.sum((y_predict-y_mean)**2)
print(SSR)

# SSR
# sum of squer regresso ( SSR )
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

# SSE
y = y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

# SST
# here df.to_numpy()will convert pandas Dataframe to Nump
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

# R2 Square

r_square = 1 - (SSR/SST)
r_square

train_mse = mean_squared_error(y_train, regressor.predict(X_train))
test_mse = mean_squared_error(y_test, y_pred)
print(train_mse)
print(test_mse)

print(f"Training Score (R^2): {bias:.2f}")
print(f"Testing Score (R^2): {variance:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Test MSE: {test_mse:.2f}")


# Save the trained model to disk
filename = 'linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as linear_regression_model.pkl")

print(os.getcwd())
