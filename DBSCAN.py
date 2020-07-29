import scipy
import numpy
from scipy.spatial import distance

class DBSCAN:
    def __init__(self, arr = None, dist = 0, minp = 0, item_len =0):
        return

    def fit(self, arr, dist, minp):
        self.arr = arr
        self.dist = dist
        self.minp = minp
        self.item_len = len(arr[0])

        start_none = [None] * len(self.arr)
        clusters = dict(zip(self.arr, start_none))

        print(clusters)


        cluster_count = 0
        for i in self.arr:
            if clusters[i] == None:
                print(i)
                # break
                neighbors = self.cluster_finder(i, self.arr, self.dist)
                print(neighbors)

                if len(neighbors) < minp:
                    clusters[i]  = -1
                else:
                    cluster_count += 1
                    for i in neighbors:
                        if clusters[i] == None:
                            clusters[i] = cluster_count


        # print(neighbors)
        print(clusters)


    def cluster_finder(self, point, arr, dist):
        cdist = distance.euclidean
        neighbors = []
        i = numpy.asarray(point)
        # print(i)
        # print(i.shape)
        for j in arr:
            jarray = numpy.asarray(j)
            # print(j)
            if cdist(i,jarray) <= dist:
                neighbors.append(j)
        return neighbors



d = DBSCAN()
arr1 = [(1,2),(2,3),(3,4),(4,5)]
arr2 = [(1,2),(2,2),(1,1), (2,1),(3,4),(4,5), (4,4)]

d.fit(arr2, 1.8, 2)
# print(arr1)