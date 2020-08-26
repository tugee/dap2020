#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    s1=pd.Series(["United Kingdom","Finland","USA","Sweden","Germany","Russia"])
    s2=pd.Series([np.nan, 1917, 1776,1532,np.nan,1992],index=s1)
    s3=pd.Series([None,"Niinistö","Trump",None,"Steinmeier","Putin"],index=s1)
    print(s3)
    asd = pd.DataFrame([],index=s1)
    asd["Year of independence"]=s2
    asd["President"]=s3
    print(asd)
    return asd
               
def main():
    missing_value_types()
    return

if __name__ == "__main__":
    main()
