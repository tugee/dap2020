#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def center(a):
    return (a.shape[0]-1)/2,(a.shape[1]-1)/2
def radial_distance(a):
    c = np.array(center(a))
    yAxis = a.shape[0]
    xAxis = a.shape[1]
    asd = np.zeros((yAxis,xAxis))
    for i in range(yAxis):
        for j in range(xAxis):
            asd[i][j]=np.sqrt((i-c[0])**2+(j-c[1])**2)
    return asd

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    if a.max()==a.min():
        return a*0
    return (a-a.min())/(a.max()-a.min())

def radial_mask(a):
    mask = 1-scale(radial_distance(a))
    return mask

def radial_fade(a):
    mask = radial_mask(a).reshape(a.shape[0],a.shape[1],1)
    return a*mask

def main():
    image = "src/painting.png"
    painting=plt.imread(image)
    plt.subplot(3,1,1)
    plt.imshow(painting)
    plt.subplot(3,1,2)
    plt.imshow(radial_mask(painting))
    plt.subplot(3,1,3)
    plt.imshow(radial_fade(painting))
    plt.show()

if __name__ == "__main__":
    main()
