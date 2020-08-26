#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def main():
    a = np.array([[2,4,6,7],[4,3,5,1]])
    b = np.array([[1,2,3,4],[4,2,3,1]])
    plt.title("title")  # Add a title to the figure
    plt.xlabel("x-axis")       # Give a label to the x-axis
    plt.ylabel("y-axis")       
    plt.plot(a[0],a[1])
    plt.plot(b[0],b[1])
    plt.show()


if __name__ == "__main__":
    main()
