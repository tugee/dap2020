#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def to_grayscale(image):
    painting2 = image
    gray = np.dot(painting2[...,:3], [0.2126, 0.7152, 0.0722])
    return gray 

def to_red(image):
    painting2 = image.copy() 
    painting2[:,:,1]=0
    painting2[:,:,2]=0
    return painting2

def to_green(image):
    painting2 = image.copy()
    painting2[:,:,0]=0
    painting2[:,:,2]=0
    return painting2
def to_blue(image):
    painting2 = image.copy()
    painting2[:,:,0]=0
    painting2[:,:,1]=0
    return painting2

def main():  
    image = "src/painting.png"
    painting=plt.imread(image)
    plt.subplot(3,1,1)
    plt.imshow(to_red(painting))
    plt.subplot(3,1,2)
    plt.imshow(to_green(painting))
    plt.subplot(3,1,3)
    plt.imshow(to_blue(painting))
    plt.imshow(to_grayscale(painting), cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()

if __name__ == "__main__":
    main()
