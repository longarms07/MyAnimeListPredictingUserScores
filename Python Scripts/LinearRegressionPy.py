# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 22:31:01 2018

@author: ecrid
"""

from sklearn.linear_model import LinearRegression,Ridge
from sklearn.decomposition import PCA
import pandas as pan
from matplotlib import pyplot as plt
import numpy as np

data = pan.read_csv("AnimeListTrainingData.csv")
data.fillna(0, inplace=True)
data.head()
#print(data.columns[2206])
dataY = data[data.columns[2206]].values
#print(data[data.columns[0]])
dataX = data[list(data.columns[:2206])].values#.reshape[:,np.newaxis]
lr = Ridge(normalize=True)
lr = lr.fit(dataX,dataY)
#print(lr)
pca = PCA(n_components=1)
pc = pca.fit_transform(dataX) #get a one dimensional set of points we can use
dataX2 = pan.DataFrame(data=pc, columns = ['principal component'])
#dataX = dataX.sort_values([list(data.columns)], ascending=False)
#dataX2 = dataX2.sort_values(['principal component'], ascending=False)
residuals = []
#print(lr.predict(dataX))
index = 0
while index < len(dataX2):
    for point in lr.predict(dataX):
        #print(dataX2.iloc[index])
        residuals.append(dataX2.iloc[index]-point)
        index=index+1
#print(residuals)
dataX3 = pan.DataFrame.from_records(residuals, columns = ['Residuals'])
print(dataX3)
#assert(0==1)
#plt.scatter(dataX2,dataY, color='r')
#plt.scatter(dataX2, lr.predict(dataX),color='b')
plt.scatter(residuals,dataY, color='m')
plt.ylabel("Scores: ")
plt.xlabel("Principal Component Analysis of Features: ")
#lineX = np.linspace(-10,500,100)
#lineY = np.linspace(7,6,100)
plt.title("Anime Scores Linear Regression: Reisduals")
#plt.plot(lineX,lineY,color='k',linewidth=5)
plt.show()