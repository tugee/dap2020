#!/usr/bin/env python3
import numpy as np
from functools import reduce   # import the reduce function from the functools module



def matrix_power(a, n):
    if(n==0):
        return np.eye(np.size(a,1))
    if(n>0):
        generator = [a for i in range(n)]
    if(n<0):
        generator = [np.linalg.inv(a) for i in range(n,0)]
    print(generator)
    k=reduce(lambda x,y:np.matmul(x,y), generator)
    return k
def main():
    matrix_power([[2,0],[0,1]],-1)

if __name__ == "__main__":
    main()
