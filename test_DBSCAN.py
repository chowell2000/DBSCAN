import dbscan
from sklearn import cluster

d = dbscan.Dbscan()
arr1 = [(1,2),(2,3),(3,4),(4,5)]
arr2 = [(1,2),(2,2),(1,1), (2,1),(3,4),(4,5), (4,4)]

d.fit(arr2, dist=3, minp=4)

d_true = cluster.DBSCAN(eps=3, min_samples=4)
dbtest = d_true.fit(arr2)

print(d.labels_)
print(dbtest.labels_)
print(type(dbtest.labels_))