import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt



#the purpose of dbscan is to identify outliers by making clusters i.grouping the data and the remaining points will then be outliers


#genrate random data points there will be the normal data points and ofc the outlier points
np.random.seed(46)
#0 is the meaan around which the data will be spread,1/5 indicates the measure of spread i.e. SD obviously outliers are more spread out and the last one 2000/500 the no of values
normal_data=np.random.normal(0,1,2000)
outlier_data=np.random.normal(0,5,500)
data=np.concatenate([normal_data,outlier_data])

#make a datframe
df=pd.DataFrame(data,columns=['value'])

#data preprocessing: standraize the data
#the aim is to have data mean as 0 and standard deviation of 1 so it is easier to compare and analyse
scaler = StandardScaler()
df['scaled_value'] = scaler.fit_transform(df[['value']])

#now we apply the dbscan clustring algorithm
#in dbscan we have:
#epsilon: the radius or distance which makes the point a neighbouring value, denoted as eps here
#min points: the minimum no of points required to form a cluster, denoted as min_sample here
#core points: the points which have at least the min no of points to make it in to a cluster
#noise points: points that do not belong in a cluster
db = DBSCAN(eps=0.5, min_samples=5).fit(df[['scaled_value']])
df['dbscan_labels'] = db.labels_
#The labels assigned by DBSCAN are stored in the db.labels_ attribute. Each point in the dataset is assigned a label:
#Points that are part of a cluster are assigned a positive integer label (representing the cluster number).
#Points classified as noise are assigned the label -1.

#detect the outliers they are vlaues whose label is -1
outliers_dbscan = df[df['dbscan_labels'] == -1]
print("Outliers detected using DBSCAN:")
print(outliers_dbscan)

#now to visualise the clusters we will plot
plt.figure(figsize=(10, 10))
#plotting the clusters
plt.scatter(df[df['dbscan_labels'] != -1]['scaled_value'],
            np.zeros(len(df[df['dbscan_labels'] != -1])),
            color='red', label='Clustered Points', alpha=0.5)

#plotting the outliers
plt.scatter(outliers_dbscan['scaled_value'],
            np.zeros(len(outliers_dbscan)),
            color='gold', label='DBSCAN Outliers')

plt.title('Outliers Detected by DBSCAN Method')
plt.xlabel('Scaled Value')
plt.legend()
plt.show()





