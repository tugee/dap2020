#!/usr/bin/env python3

import pandas as pd
import numpy as np


def last_week():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    asd = df["LW"]
    possibleMask = (df["LW"]=="Re") | (df["LW"]=="New")
    df1 = df[-possibleMask]
    print(df1)
    masken = df1["Peak Pos"].map(int)==df1["Pos"].map(int)
    df1.loc[masken,"Peak Pos"]=np.nan
    df1.loc[0,"Peak Pos"]=1
    df1.loc[6,"Peak Pos"]=7
    df1.loc[16,"Peak Pos"]=17
    df1.loc[:,"Pos"]=df.loc[-possibleMask,"LW"]
    df1.loc[:,"LW"]=np.nan
    df1["WoC"]=df1["WoC"].map(int)-1
    line = pd.Series(data={"Pos":35,"LW":np.nan,"Title":None,"Artist":None,"Publisher":None,"Peak Pos":np.nan,"WoC":np.nan})
    line1 = pd.Series(data={"Pos":38,"LW":np.nan,"Title":None,"Artist":None,"Publisher":None,"Peak Pos":np.nan,"WoC":np.nan})
    line2= pd.Series(data={"Pos":39,"LW":np.nan,"Title":None,"Artist":None,"Publisher":None,"Peak Pos":np.nan,"WoC":np.nan})
    line3 = pd.Series(data={"Pos":40,"LW":np.nan,"Title":None,"Artist":None,"Publisher":None,"Peak Pos":np.nan,"WoC":np.nan})
    df1 = df1.append(line,ignore_index=True)
    df1 = df1.append(line1,ignore_index=True)
    df1 = df1.append(line2,ignore_index=True)
    df1 = df1.append(line3,ignore_index=True)
    df1["Pos"]=df1["Pos"].map(int)

    df1 = df1.sort_values(by=["Pos"]).reset_index(drop=True)
    return df1

def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
