#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    asd = np.sqrt(np.sum(a**2,axis=1))
    return asd

def main():
    a = vector_lengths(np.array([[0,1],[0,2]]))
    print(a)

if __name__ == "__main__":
    main()
