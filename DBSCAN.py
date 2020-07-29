import scipy
import numpy


class DBSCAN:
    def __init__(self, arr = None, dist = 0, minp = 0):
        return

    def fit(self, arr, dist, minp):
        self.arr = arr
        self.dist = dist
        self.minp = minp

        start_none = [None] * len(self.arr)
        clusters = dict(zip(self.arr, start_none))

        print(clusters)


        cluster_count = 0
        for i in self.arr:
            if clusters[i] == None:
                print(i)
                return

        print(clusters)



d = DBSCAN()
arr1 = [(1,2),(2,3),(3,4),(4,5)]

d.fit(arr1, 1, 1)
print(arr1)