# -*- coding: utf-8 -*-
"""Linear Regression ML Implementation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yrGc9MZfXz00EruS4YSUnIYYXNrvZpKb
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

"""## Boston House Pricing Dataset"""

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
boston_data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
boston_target = raw_df.values[1::2, 2]

print(boston_data)

print(boston_target)

boston_featurename = ['CRIM','ZN','INDUS','CHAS' ,'NOX'
,'RM'
,'AGE'
,'DIS'
,'RAD'
,'TAX'
,'PTRATIO'
,'B'
,'LSTAT'
]

"""## Preparing the dataset"""

dataset = pd.DataFrame(boston_data, columns=boston_featurename)

dataset.head()

dataset['Price']=boston_target

dataset.head()

dataset.info()

"""## Summarizing the stats of the data"""

dataset.describe()

"""## Check the missing the values"""

dataset.isnull().sum()

"""### Exploratory Data Analysis (EDA)"""

## Correlation
dataset.corr()

import seaborn as sns
sns.pairplot(dataset)

plt.scatter(dataset['CRIM'],dataset['Price'])
plt.xlabel('Crime Rate')
plt.ylabel('Price')

plt.scatter(dataset['RM'],dataset['Price'])
plt.xlabel('RM')
plt.ylabel('Price')

import seaborn as sns
sns.regplot(x='RM', y='Price', data=dataset)

sns.regplot(x='CRIM', y='Price', data=dataset)

sns.regplot(x='LSTAT', y='Price', data=dataset)

sns.regplot(x='CHAS', y='Price', data=dataset)

sns.regplot(x='PTRATIO', y='Price', data=dataset)

"""## Independent and Depandent Features"""

X=dataset.iloc[:,:-1]
y=dataset.iloc[:,-1]

X.head()

y

"""## Train Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

X_train

X_test

"""## Standardize the dataset"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

X_train

X_test

"""# **Model Training**"""

from sklearn.linear_model import LinearRegression

regression = LinearRegression()

regression.fit(X_train, y_train)

## print the coefficients and the intercept
print(regression.coef_)

print(regression.intercept_)

## on which parameters the model has been trained
regression.get_params()

## Prediction with test data
reg_pred = regression.predict(X_test)

reg_pred

"""## Assumptions"""

## Plot a catter plot for the prdiction
plt.scatter(y_test, reg_pred)

#residuals
residuals = y_test-reg_pred

residuals

## Plot the residuals
sns.displot(residuals, kind='kde')

## Scatter plot with respect to prediction and residuals
## uniform distribuaion
plt.scatter(reg_pred, residuals)

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

print(mean_absolute_error(y_test, reg_pred))
print(mean_squared_error(y_test, reg_pred))
print(np.sqrt(mean_squared_error(y_test, reg_pred)))

"""## **R square and adjusted R square**


Formula

R^2 = 1 - SSR/SST

R^2 = coefficient of determination SSR = sum of squares of residuals SST = total sum of squares

"""

from sklearn.metrics import r2_score
score=r2_score(y_test,reg_pred)
print(score)

"""

**Adjusted R2 = 1** – [(1-R2)*(n-1)/(n-k-1)]

where:

R2: The R2 of the model n: The number of observations k: The number of predictor variables
"""

#display adjusted R-squared
1 - (1-score)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)

"""## New Data Prediction"""

boston_data[0].reshape(1,-1)

scaler.transform(boston_data[0].reshape(1,-1))

regression.predict(scaler.transform(boston_data[0].reshape(1,-1)))

"""#3 Pickle the Model File for Deployment"""

import pickle

pickle.dump(regression, open('regmodel.pkl','wb'))

pickled_model=pickle.load(open('regmodel.pkl','rb'))

#3 prediction
pickled_model.predict(scaler.transform(boston_data[0].reshape(1,-1)))























