
import pandas as pd
import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt

df = pd.read_csv("zadanie4/iris.data", sep=",", names=[
                 "sepal length in cm", "sepal width in cm", "petal length in cm", "petal width in cm", "class"])



l= df[['sepal length in cm','sepal width in cm','class']]

x1 = l[l['class']=='Iris-setosa']['sepal length in cm']
x2 = l[l['class']=='Iris-versicolor']['sepal length in cm']
x3 = l[l['class']=='Iris-virginica']['sepal length in cm']

y = l[l['class']=='Iris-setosa']['sepal width in cm']

plt.scatter(x1,y, c='r')
plt.scatter(x2,y, c='b')
plt.scatter(x3,y, c='g')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()