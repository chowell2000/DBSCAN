# DBSCAN

Python DBSCAN module with DBSCAN* and ST-DBSCAN
DBSCAN is well-known clustering algorithm. Given a minimum number of neighbors and a distance, DBSCAN finds points that have at least that many neighbors within the distance, marking them as clusters. Points that have fewer than the minimum neighbors but have 
Given a number N of minimum neighbors and a distance d, the algorithm proceeds as follows:

  If a point has < N neighbors within d, label the point as Noise (implemented as -1)

  If a point has at least N neighbors within d, label it and all its neighbors as a being in a cluster C. 
    Then check each neighbor point to see if it has N neighbors as well, if so, 
    label those neighbors as in cluster C and check their neighbors as well, and so on. 
      Note that the neighbors are labeled as in C even if they were previously 
      labeled Noise - these are border points.


This also includes an implementation of DBSCAN*, where border points are lalebed as Noise (-1).
To use this implementation, call the class with x=True:
dbscan = Dbscan.dbscan(x=True)
