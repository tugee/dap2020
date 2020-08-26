#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    indices = ["a","b","c"]
    as1 = []
    as2 = []
    i=0
    # (L1,indices) easier way to do it, do not try to loop everything
    for k in indices:
        as1.append(L1[i])
        as2.append(L2[i])
        i+=1
    s1 = pd.Series(as1,indices)
    s2 = pd.Series(as2,indices)
    return s1,s2

def modify_series(s1, s2):
    s1["d"] = s2["b"]
    del s2["b"]
    return s1,s2
def main():
    a,b = create_series([1,2,3],[2,2,3])
    a,b = modify_series(a,b)
    a+b
    
if __name__ == "__main__":
    main()
