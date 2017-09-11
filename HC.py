# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 00:09:52 2017

@author: zaghlollight
"""

import matplotlib.pyplot as plt
import pandas as pd 
dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values

#using the dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()

# Fitting Hierarchical Clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
yhc = hc.fit_predict(x)

# Visualising the clusters
plt.scatter(x[yhc == 0, 0], x[yhc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[yhc == 1, 0], x[yhc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[yhc == 2, 0], x[yhc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[yhc == 3, 0], x[yhc == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(x[yhc == 4, 0], x[yhc == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()