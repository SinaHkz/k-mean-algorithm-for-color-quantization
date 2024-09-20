from PIL import Image
import random
from Pixel import Pixel
from functions import *

imageName = input("Enter image name: ")

try:
    img = Image.open(imageName)
except:
    print("something went wrong!")
    exit()

countOfCentroid = int(input("Number of color: "))

centroids = []
for i in range(countOfCentroid):
    pixel = Pixel(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    centroids.append(pixel)

newImg = []
for i in range(img.width):
    newRow = []
    for j in range(img.height):
        pixelRGB = img.getpixel((i, j))
        newPixel = Pixel(pixelRGB[0], pixelRGB[1], pixelRGB[2])
        newRow.append(newPixel)
    newImg.append(newRow)

newImg = setImagePixelCentroids(centroids, newImg)
oldCentroids = centroids
centroids = evaluateNewCentroids(centroids, newImg)

count = 0

while (checkEndOfLoop(oldCentroids, centroids) and count < 20):
    oldCentroids = centroids
    newImg = setImagePixelCentroids(centroids, newImg)
    centroids = evaluateNewCentroids(centroids, newImg)
    count = count + 1

newImg = createNewImagePixel(newImg)

for i in range(img.width):
    for j in range(img.height):
        pixel = newImg[i][j]
        img.putpixel((i, j), (int(pixel.R), int(pixel.G), int(pixel.B)))
img.save("output.jpg")
