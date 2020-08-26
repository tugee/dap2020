#!/usr/bin/env python3

import pandas as pd

def top_bands():
    df = pd.read_csv("src/bands.tsv",sep="\t")
    df["Band"]=df["Band"].str.upper()
    print(df)
    df2 = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    df3 = pd.merge(df2,df,left_on=["Artist"],right_on="Band",how="right")
    print(df3)

    return df3
    
def main():
    top_bands()

if __name__ == "__main__":
    main()
