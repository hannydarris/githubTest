"""Project 9.2: Earthquake Data Mining
    Authors: Danny Harris and Thomas Michiels
    Description:

"""
import urllib.request
import math
import random
import turtle

def visualizeQuakes(k, r):
    """(int, int) -> None

    Calls: readeqf, createCentroids, createClusters

    Functions plots clusters, and centroids on a map,
    or turtle canvas, with given dimensions (k, r).
    Function returns None.

    >>> visualizeQuakes(5, 6)

    """
    datadict = readeqf()
    quakeCentroids = createCentroids(k, datadict)
    clusters = createClusters(k, quakeCentroids, datadict, r)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic("worldmap.gif")
    quakeWin.screensize(1800, 900)

    wFactor = (quakeWin.screensize()[0]/2)/180
    hFactor = (quakeWin.screensize()[1]/2)/90

    quakeT.hideturtle()
    quakeT.up()

    colorlist = ["red","green","blue","orange","cyan","yellow"]

    for clusterIndex in range(k):
        quakeT.color(colorlist[clusterIndex])
        for akey in clusters[clusterIndex]:
            lon = datadict[akey][0]
            lat = datadict[akey][1]
            quakeT.goto(lon*wFactor, lat*hFactor)
            quakeT.dot()
    quakeWin.exitonclick()
    
def readeqf():
   '''() -> dictionary of equake longitudes, latitudes

   Use USGS API to get data about earthquake
   events of magnitude >= 5 for past month;
   store earthquake longitude and latitudes
   in a list, which is returned.

   Called by: visualizeQuakes (and clusterAnalysis)

   For example,
   >>> readeqf()
   {1: [-122.75, 45.68], 2: [-121.73, 43.53]} 
   '''
   with urllib.request.urlopen(
   'http://earthquake.usgs.gov/fdsnws/event/1/\
query?format=csv\
&starttime=2016-02-01\
&minmagnitude=5'
) as eqf:
      
      eqdict = {}
      key = 0
      eqf.readline() # move past header
      for line in eqf:
         line = line.decode()
         line = line.strip().split(',')
         latitude = round(float(line[1]), 2)
         longitude = round(float(line[2]), 2)
         key += 1
         eqdict[key] = [longitude, latitude]

   return eqdict

def euclidD(point1, point2):
    """(int, int) -> num

    Function uses Euclidian Distance formula to calculate
    the distance between each coordinate point and the
    centroid points.
    Function returns total distance of points in cluster
    to the centroid.

    """
    total = 0
    for i in range(len(point1)):
        difference = (point1[i]-point2[i])**2
        total += difference

    euclidDistance = math.sqrt(total)
    return euclidDistance

def createCentroids(k, datadict):
    """(int, dict) -> list

    Function c

    """
    centroids = []
    centroidCount = 0
    centroidKeys = []

    while centroidCount < k:
        rkey= random.randint(1,len(datadict))
        if rkey not in centroidKeys:
            centroids.append(datadict[rkey])
            centroidKeys.append(rkey)
            centroidCount = centroidCount + 1
    return centroids

def createClusters(k, centroids, datadict, repeats):
    """(int, list, dict, int) -> list
    
    Function creates a list of lists of floating point numbers,
    and associates them with the list variable clusters.
    Each list within clusters represents a coordinate point.

    Function returns clusters.

    >>> createClusters(5, createCentroids(5, readeqf()), readeqf(), 6)
    [[6, 7, 12, 13, 18, 20, 21, 22, 23, 25, 26, 28, 33, 34, 35, 42, 45, 46, 51, 62, 64, 65, 70, 78, 81, 83, 88, 115, 118, 119, 120, 128, 129, 131, 132],
    [2, 4, 15, 16, 36, 40, 41, 47, 56, 61, 73, 75, 80, 86, 87, 91, 100, 103, 108, 109, 110, 112, 113, 114, 116, 124],
    [1, 3, 8, 9, 17, 27, 29, 31, 38, 39, 44, 49, 54, 55, 57, 60, 63, 66, 67, 69, 74, 84, 85, 89, 93, 94, 96, 98, 99, 101, 102, 104, 105, 107, 130],
    [19, 24, 43, 48, 50, 52, 53, 68, 76, 82, 97, 117, 121, 122], [5, 10, 11, 14, 30, 32, 37, 58, 59, 71, 72, 77, 79, 90, 92, 95, 106, 111, 123, 125, 126, 127, 133]]
    """
    for apass in range(repeats):
        print("****PASS",apass,"****")
        clusters=[]
        for i in range(k):
            clusters.append([])

        for akey in datadict:
            distances = []
            for clusterIndex in range(k):
                dist = euclidD(datadict[akey],centroids[clusterIndex])
                distances.append(dist)

            mindist = min(distances)
            index = distances.index(mindist)

            clusters[index].append(akey)

        dimensions = len(datadict[1])
        for clusterIndex in range(k):
            sums = [0]*dimensions
            for akey in clusters[clusterIndex]:
                datapoints = datadict[akey]
                for ind in range(len(datapoints)):
                    sums[ind] = sums[ind] + datapoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind]/clusterLen

            centroids[clusterIndex] = sums
        for c in clusters:
            print("CLUSTER")
            for key in c:
                print(datadict[key], end=" ")
                print()
        return clusters

def clusterAnalysis():
    """() -> None
    Calls: createCentroids, readeqf, createClusters

    Function creates clusters and centroids and a dictionary
    from function readeqf.
    Returns None.

    >>> clusterAnalysis()
    
    """
    examDict = readeqf()
    examCentroids = createCentroids(5, examDict)
    examClusters = createClusters(5, examCentroids, examDict, 3)

