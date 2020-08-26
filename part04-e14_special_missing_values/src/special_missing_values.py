#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv",sep="\t")
    mask = (df["LW"]=="New") | (df["LW"]=="Re")
    print(mask)
    df["LW"][mask]=41
    print(df)
    #pd.to_numeric(df["LW"])
    mask2 = df["LW"].map(int)<df["Pos"]
    print(df[mask2])
    return df[mask2]

def main():
    special_missing_values()
    return

if __name__ == "__main__":
    main()
