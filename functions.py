def evaluateDistance(set1, set2):
    return (((set1[0] - set2[0]) ** 2) + ((set1[1] - set2[1]) ** 2) + ((set1[2] - set2[2]) ** 2)) ** 0.5


def setImagePixelCentroids(centroids, img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            img[i][j].setNewCentroid(centroids)
    return img


def evaluateNewCentroids(centroids, img):
    for i in range(len(centroids)):
        centroid = centroids[i]
        pixelOfCentroid = []
        for i in range(len(img)):
            for j in range(len(img[i])):
                if img[i][j].centroid == centroid:
                    pixelOfCentroid.append(img[i][j])
        if len(pixelOfCentroid) != 0:
            rValues = [obj.R for obj in pixelOfCentroid]
            centroid.R = sum(rValues) / len(pixelOfCentroid)

            gValues = [obj.G for obj in pixelOfCentroid]
            centroid.G = sum(gValues) / len(pixelOfCentroid)

            bValues = [obj.B for obj in pixelOfCentroid]
            centroid.B = sum(bValues) / len(pixelOfCentroid)

    return centroids


def checkEndOfLoop(oldCentroids, newCentroids):
    for i in range(len(oldCentroids)):
        if abs(oldCentroids[i].R - newCentroids[i].R) > 0.01 or abs(
                oldCentroids[i].G - newCentroids[i].G) > 0.01 or abs(oldCentroids[i].B - newCentroids[i].B) > 0.01:
            return False
    return True


def createNewImagePixel(img):
    for i in range(len(img)):
        for j in range(len(img[i])):
            pixel = img[i][j]
            pixel.setPixels(pixel.centroid.getPixelSet())
    return img
