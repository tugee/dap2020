#!/usr/bin/env python3

import numpy as np

def diamond(n):
    a=np.eye(n,dtype=int)
    transpose=np.flip(a,axis=1)[1:n,]
    big=np.concatenate((a,transpose),axis=0)
    bigFlip=np.flip(big,axis=1)[:,0:n-1]
    final=np.concatenate((bigFlip,big),axis=1)
    return final

def main():
    print(diamond(4))

if __name__ == "__main__":
    main()
