#!/usr/bin/env python3

import pandas as pd
import numpy as np
def powers_of_series(s, k):
    if(s.empty):
        return pd.DataFrame([],columns =range(1,k+1))
    df = pd.DataFrame(s.values,columns = [1],index = s.index)
    for exponential in range(2,k+1):
        col = s.values**exponential
        kolonna = pd.DataFrame(col,columns = [exponential],index=s.index)
        df[exponential]=kolonna
    return df
    
def main():
        ind=list("abcdefghijklmnopqrstuvwxyz")
        k=3
        for n in range(4):
            L=np.random.randint(-10, 10, n)
            s = pd.Series(L, index=ind[:n])
            print(s)
            print(n)
            print(powers_of_series(s,3))
    
if __name__ == "__main__":
    main()
