import pandas as pd

data=pd.read_csv('Salary_Data.csv')

# for i in range(len(data.iloc[:,0])):
#     print(data.iloc[i,0])
print(data.head())

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

print(y)

#split  train and test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=1/3,random_state=0)

#model trainnig
from sklearn.linear_model import LinearRegression
lr= LinearRegression()
lr.fit(x_train,y_train)

predict = lr.predict(x_test)
print(predict)

import matplotlib.pyplot as pt

pt.scatter(x,y,color='red')
pt.plot(x_train,lr.predict(x_train),color='blue')


import matplotlib.pyplot as plt

