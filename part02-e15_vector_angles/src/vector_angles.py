#!/usr/bin/env python3

import numpy as np
from numpy.core.umath_tests import inner1d
import scipy.linalg

def vector_angles(X, Y):
    value=np.degrees(np.arccos(np.clip(inner1d(X,Y)/(np.sqrt(inner1d(X,X))*np.sqrt(inner1d(Y,Y))),a_min=-1,a_max=1)))
    return value

def main():
    print(vector_angles(np.array([[1,2,3], [4,5,6]]),np.array([[1,2,3], [4,5,6]])))

if __name__ == "__main__":
    main()
