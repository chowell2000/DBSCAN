import dbscan
from sklearn import cluster
import numpy as np
import random

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


# #############################################################################
# Generate sample data
# centers = [[2, 1], [-2, -1], [1, -2], ]
centers = [(random.randrange(-20,20), random.randrange(-20,20)) for i in range(15)]
X, labels_true = make_blobs(n_samples=2500, centers=centers, cluster_std=1,
                            random_state=0)

X = StandardScaler().fit_transform(X)

# print(X)
# #############################################################################
# Compute DBSCAN
d = dbscan.Dbscan(x = False)
d.fit(X, 0.05, 10)
db = DBSCAN(eps=0.05, min_samples=10).fit(X)
core_samples_mask = np.zeros_like(d.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = d.labels_


# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print('Estimated number of clusters: %d' % n_clusters_)
print('Estimated number of noise points: %d' % n_noise_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))
print(db.core_sample_indices_)
print(db.labels_ == d.labels_)
if (db.labels_ == d.labels_).all():
    print('lists the same')
else:
    print('lists differ')
print('self.x from Dbscan')
print(d.x)
# #############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    # xy = X[class_member_mask & core_samples_mask]
    xy = X[class_member_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=8)
    #
    # xy = X[class_member_mask & ~core_samples_mask]
    # plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
    #          markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()



#
# d = DBSCAN.DBSCAN()
# arr1 = [(1,2),(2,3),(3,4),(4,5)]
# arr2 = [(1,2),(2,2),(1,1), (2,1),(3,4),(4,5), (4,4)]
#
# d.fit(arr2, dist=3, minp=4)
#
# d_true = cluster.DBSCAN(eps=3, min_samples=4)
# dbtest = d_true.fit(arr2)
#
# print(d.labels_)
# print(dbtest.labels_)
# print(type(dbtest.labels_))