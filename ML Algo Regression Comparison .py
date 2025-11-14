import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"C:\Users\DELL\OneDrive\Desktop\DATA SCIENCE\S-oct 6th - poly\6th - poly\1.POLYNOMIAL REGRESSION\emp_sal.csv")

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# linear model  -- linear algor ( degree - 1)
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# polynomial model  ( bydefeaut degree - 2)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=5)
X_poly = poly_reg.fit_transform(X)

poly_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)


# linear regression visualizaton 
plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X), color = 'blue')
plt.title('Linear Regression graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# poly nomial visualization 

plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# predicton 

lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred

####### svr model
from sklearn.svm import SVR
svr_model = SVR(kernel ='poly' , degree = 4 , gamma = 'auto' , C = 10.0)
svr_model.fit(X, y)

svr_model_pred = svr_model.predict([[6.5]])
print(svr_model_pred)

# knn regressor 
from sklearn.neighbors import KNeighborsRegressor
knn_reg = KNeighborsRegressor(n_neighbors=5 , weights='uniform' , algorithm='brute' , p = 2)
knn_reg.fit(X,y)

# prediction 
knn_reg_pred = knn_reg.predict([[6.5]])
knn_reg_pred

#decission tree algorithm
from sklearn.tree import DecisionTreeRegressor
dt_reg = DecisionTreeRegressor()
dt_reg.fit(X,y)

dt_reg_pred = dt_reg.predict([[6.5]])
print(dt_reg_pred)


#random forest 
from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=23,random_state=0)
rf_reg.fit(X,y)

rf_reg_pred = rf_reg.predict([[6.5]])
rf_reg_pred


#xgboost regressor 
import xgboost as xg
xgb_r = xg.XGBRegressor(objective ='reg:linear',n_estimators = 4)
xgb_r.fit(X,y)

xgb_reg_pred = xgb_r.predict([[6.5]])
xgb_reg_pred





