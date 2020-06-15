import math
import numpy as np

#Point class for an n-dimensional point
class Point :
    
    #initialize a point with coordinates in a list
    def __init__(self, coords) :
        self.coords = coords
        self.currCluster = None

    #dimensionality of point
    @property
    def dim(self) :
        return len(self.coords)
        
    #Returns the distance between this point and other
    #Remember how to calculate Euclidean distance!
    def distFrom(self, other) :
        #calculate distance from self to other
        if self.dim != other.dim :
            raise Exception("dimension mismatch: self has dim {} and other has dim {}".format(self.dim, other.dim))
        #fill in
        sqr_sum=0

        for i in range(self.dim):
            sqr_sum += (self.coords[i]-other.coords[i])**2

        dist = math.sqrt(sqr_sum)

        return dist
        
    #Reassign point from its current cluster to a new cluster
    #Returns True if the new cluster is different from the current cluster
    #Returns False otherwise
    #(Return value is useful for determining if you've converged)
    def moveToCluster(self, dest) :
        if (self.currCluster is dest) :
            return False
        else :
            if (self.currCluster) :
                self.currCluster.removePoint(self)                
            dest.addPoint(self)
            self.currCluster = dest
            return True
            
    #Return the object that is closest to the current point
    #Useful for finding the closest cluster to the current point
    def closest(self, listOfPoints) :
        minDist = self.distFrom(listOfPoints[0])
        minPt = listOfPoints[0]
        for p in listOfPoints :
            if (self.distFrom(p) < minDist) :
                minDist = self.distFrom(p)
                minPt = p
        return minPt
        
    def __getitem__(self, i) :
        return self.coords[i]
        
    def __str__(self) :
        return str(self.coords)
        
    def __repr__(self) :
        return "Point: " + self.__str__()
        
#create a list of points
#input: data, a p-by-k numpy array
#output: a list of p k-dimensional points, with each point's coordinates
#        coming from one row of data
def makePointList(data) :
    #fill in
    data_list=[]

    for i in range(len(data)):
        data_list.append(Point(data[i]))

    return data_list
    
if __name__ == '__main__' :
    data = np.array([[0.5, 2.5], [0.3, 4.5], [-0.5, 3], [0, 1.2], [10, -5], [11, -4.5], [8, -3]])
    
    points = makePointList(data)
    print(points)

    print(points[0].distFrom(points[1]))