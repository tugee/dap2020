#!/usr/bin/env python3

import pandas as pd
import numpy as np
def inverse_series(s):
    arvot = []
    indeksit = []
    i = 0
    for value in s.values:
        if value in indeksit:
            arvot[i]=s.keys()[i]
            continue
        indeksit.append(value)
        arvot.append(s.keys()[i])
        i+=1    
    return pd.Series(indeksit,arvot)

def main():
    d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
    s4 = pd.Series(d, name="Presidents")
    inverse_series(s4)

if __name__ == "__main__":
    main()
