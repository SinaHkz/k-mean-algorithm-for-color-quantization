# K-Means Clustering for Image Color Quantization

### Overview

This project implements a K-Means clustering algorithm to perform color quantization on images. Color quantization is the process of reducing the number of unique colors in an image while maintaining its visual integrity. By applying K-Means, we can represent the original image with a limited color palette, which can be useful for image compression, stylization, and other applications.

### Features

* K-Means Clustering: Clusters the pixels of an image based on their RGB values.
* Customizable Color Palette: Specify the number of colors (K) to quantize the image.
* Supports Multiple Image Formats: Works with common image formats like PNG, JPEG, BMP, etc.


To run this project, you'll need:

* Python 3.x
* PIL (Python Imaging Library) or Pillow for image processing


### Example
k = 5

| original image | quantized image| 
| ------------- |:-------------:| 
|![venice-greece-upsplash](https://github.com/user-attachments/assets/f1dbb70d-2737-45d8-82d3-b8d3ff803287)|![output](https://github.com/user-attachments/assets/39018050-f8a2-4b61-90a7-1cc24a5f5cd6)| 



### How It Works

1. Image Preprocessing: The image is loaded and its pixels are represented as RGB vectors.
2. K-Means Initialization: Randomly select K initial cluster centers from the image pixels.
3. K-Means Iteration:
   Assign each pixel to the nearest cluster center.
   Recompute the cluster centers based on the mean of the assigned pixels.
   Repeat until convergence (i.e., the cluster centers no longer change).
4. Image Reconstruction: Replace each pixel with the nearest cluster center’s RGB value to generate the quantized image.


### Performance Considerations

* Increasing K will improve image fidelity but will also increase computational time.
* The algorithm may take longer for high-resolution images due to the larger number of pixels to process.

## Contact me

For any questions or suggestions, feel free to open an issue or contact me at sina.hakimzadeh.1401@gmail.com.

