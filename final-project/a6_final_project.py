import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

data = pd.read_csv("final-project/cta_data.csv")
x = data[["Bus Rides", "Train Rides"]].values

x_std = StandardScaler().fit_transform(x)

k = 2

km = KMeans(n_clusters=k).fit(x_std)

centroids = km.cluster_centers_
labels = km.labels_

plt.figure(figsize=(5,4))

for i in range(k):
    cluster = x_std[labels == i]
    plt.scatter(cluster[:, 0], cluster[:, 1])

plt.scatter(centroids[:, 0], centroids[:, 1], marker = 'X', s = 100, c = 'r', label = "centroid")

plt.xlabel("Bus Rides")
plt.ylabel("Train Rides")
plt.show()