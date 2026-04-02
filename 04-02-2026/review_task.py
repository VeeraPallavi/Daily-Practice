# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, mean_absolute_error, mean_squared_error, r2_score,precision_score,recall_score,f1_score,roc_auc_score
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from google.colab import drive
drive.mount('/content/drive')

#Load the Dataset
df = pd.read_csv("/content/drive/MyDrive/aws_inventory_logistics_raw (1).csv")

print(df)

#Data Preprocessing

df.isnull().sum()

df = df.dropna()

df.info()
df.describe()

#Linear Regression

X = df.drop('transport_cost', axis = 1)
y = df['transport_cost']

X = pd.get_dummies(X, drop_first= True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Mean Absolute Error : ",mean_absolute_error(y_test,y_pred))
print("Mean Square Error : ",mean_squared_error(y_test,y_pred))
print("R2_score : ",r2_score(y_test,y_pred))

#DecisionTreeClassifier & DecisionTreeRegression

num_values = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
cat_values = df.select_dtypes(include=['object']).columns.tolist()

print(num_values)
print(cat_values)

df['stock_risk'] = (df['stock_level'] < df['reorder_level']).astype('int')

processsor = ColumnTransformer(
    transformers=[
    ('cat', OneHotEncoder(handle_unknown = 'ignore'), cat_values)
],remainder= 'passthrough'
)

X = df.drop(['transport_cost','stock_risk'], axis = 1)

y_reg = df['transport_cost']
y_class = (df['stock_risk']< df['reorder_level']).astype(int)

X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_reg, test_size = 0.2, random_state = 42)

X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X, y_class, test_size = 0.2, random_state = 42)

cif_pipeline = Pipeline([
    ('processsor', processsor),
    ('model', DecisionTreeClassifier(max_depth = 1000, random_state=42))
])

reg_pipeline = Pipeline([
    ('processsor', processsor),
    ('model', DecisionTreeRegressor(max_depth = 1000, random_state=42))
])

cif_pipeline.fit(X_train_class, y_train_class)
reg_pipeline.fit(X_train_reg, y_train_reg)

y_reg_pred = reg_pipeline.predict(X_test_reg)
y_class_pred = cif_pipeline.predict(X_test_class)

#Regression Metrics
print("Regression Metrics: ")
print("Mean Absolute Error : ",mean_absolute_error(y_test_reg, y_reg_pred))
print("Mean Square Error : ",mean_squared_error(y_test_reg,y_reg_pred))
print("R2_score : ",r2_score(y_test_reg,y_reg_pred))

#Classification Metrics
print("Classification metrics : ")
print("Accuracy : ",accuracy_score(y_test_class, y_class_pred))
print("Precision : ", precision_score(y_test_class, y_class_pred))
print("Recall : ", recall_score(y_test_class, y_class_pred))
print("F1 Score : ", f1_score(y_test_class, y_class_pred))

#Example Use Case

new_data = pd.DataFrame({
    'inventory_id' : ['INV-2065'],
    'warehouse' :['WH-B'],
    'product' :['Laptop'],
    'supplier' : ['Supplier-Z'],
    'stock_level' : [200],
    'reorder_level' : [150],
    'last_updated' : ['3/23/2026 9:22:56 PM']
})

transportation_cost = reg_pipeline.predict(new_data)
stock_risk = cif_pipeline.predict(new_data)

print("Predicted Transportation Cost :",transportation_cost[0])
print("Risk of shortage :", stock_risk[0])