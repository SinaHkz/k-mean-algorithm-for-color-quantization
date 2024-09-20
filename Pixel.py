from functions import evaluateDistance


class Pixel:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B
        self.centroid = None
        self.distanceToCentroid = None

    def __str__(self):
        return f"({self.R},{self.G},{self.B})"

    def setPixels(self, RGB):
        self.R = RGB[0]
        self.G = RGB[1]
        self.B = RGB[2]

    def getPixelSet(self):
        return (self.R, self.G, self.B)

    def setNewCentroid(self, centroids):
        firstCentroid = centroids[0]
        distanceToFirstCentroid = evaluateDistance(firstCentroid.getPixelSet(), self.getPixelSet())
        self.setCentroid(firstCentroid, distanceToFirstCentroid)

        for i in range(1, len(centroids)):
            distance = evaluateDistance(centroids[i].getPixelSet(), self.getPixelSet())
            if distance < self.distanceToCentroid:
                self.setCentroid(centroids[i], distance)

    def setCentroid(self, centroid, distance):
        self.centroid = centroid
        self.distanceToCentroid = distance
