#!/usr/bin/env python3

import numpy as np

def column_comparison(a):
    return np.array(a[a[:,1]>a[:,np.shape(a)[1]-2],:])
    
def main():
    pass

if __name__ == "__main__":
    main()
