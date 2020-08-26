#!/usr/bin/env python3

import numpy as np

def get_rows(a):
    rowVector = []
    for i in range(np.shape(a)[0]):
        rowVector.append(a[i,:])
    return rowVector

def get_columns(a):
    rowVector = []
    for i in range(np.shape(a)[1]):
        rowVector.append(a[:,i])
    return rowVector

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Rows:", get_rows(a))
    print("Columns:", get_columns(a))

if __name__ == "__main__":
    main()
