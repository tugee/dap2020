#!/usr/bin/env python3

import numpy as np

def first_half_second_half(a):
    m=int(a.shape[1]/2)

    returni = a[np.sum(a[:,0:m],axis=1)>np.sum(a[:,m:(2*m)],axis=1),:]
    return np.array(returni)

def main():
    pass

if __name__ == "__main__":
    main()
