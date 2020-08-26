#!/usr/bin/env python3

import numpy as np
import collections

def most_frequent_first(a, c):
    b = a[:,c]   # get column c
    _,s,t = np.unique(b, return_inverse=True, return_counts=True)
    print(b)
    print(t)
    print(s)
    print(t[s])
    idx = np.argsort(t[s])
    print(idx)
    return a[idx][::-1]

def main():
    a = np.array([[1, 3, 4, 2],
              [2, 2, 1, 2],[1, 3, 4, 1],[1, 3, 3, 7],[1, 3, 3, 8],[1, 3, 3, 2],[1, 3, 3, 1]])
    most_frequent_first(a,3)

if __name__ == "__main__":
    main()
