import scipy
import numpy
from scipy.spatial import distance

class Dbscan:
    def __init__(self, x= True, arr = None, dist = 0, minp = 0, item_len =0,
                 labels_ = None, clusters = None):
        self.arr = arr
        self.arr = arr
        self.dist = dist
        self.minp = minp
        self.x = x
        self.clusters = clusters
        self.labels_ = labels_
        self.core_sample_indices_ = []

    # # def labels_(self):
    #     labels = [clusters[i] for i in clusters.keys()]
    #     return labels

    def fit(self, arr, dist, minp):
        self.arr = arr
        self.dist = dist
        self.minp = minp
        self.item_len = len(arr[0])

        start_none = [None] * len(self.arr)
        if type(self.arr) == numpy.ndarray:
            self.arr = list(map(tuple, self.arr))
        clusters = dict(zip(self.arr, start_none))
        self.clusters = clusters

        # print(clusters)


        cluster_count = 0
        for i in self.arr:
            # print(i)
            if clusters[i] == None:
                # print(i)
                # break
                neighbors = self.cluster_finder(i, self.arr, self.dist)
                print(neighbors)

                if len(neighbors) < minp:
                    clusters[i]  = -1
                    print(clusters[i])
                else:
                    neighbors.remove(i)
                    for j in neighbors:
                        # print(j)
                        if ((clusters[j] == -1) & (self.x == False)):
                            clusters[j] = cluster_count
                        if clusters[j] == None:
                            clusters[j] = cluster_count
                            iterneighbors = self.cluster_finder(j, self.arr, self.dist)
                            if len(iterneighbors) >= minp:
                                new_neighbors = list(set(iterneighbors) - set(neighbors))
                                for item in new_neighbors:
                                    neighbors.append(item)
                                # print(iterneighbors)
                                # print(new_neighbors)
                    # print(neighbors)
                    # print(clusters[j])
                    clusters[i] = cluster_count
                    cluster_count += 1




        # print(neighbors)

        self.labels_ = numpy.asarray([self.clusters[i] for i in self.clusters.keys()])
        self.core_sample_indices_ = []

        print(self.clusters)


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


#
# d = DBSCAN()
# arr1 = [(1,2),(2,3),(3,4),(4,5)]
# arr2 = [(1,2),(2,2),(1,1), (2,1),(3,4),(4,5), (4,4)]
#
# d.fit(arr2, 3, 4)
# print(arr1)