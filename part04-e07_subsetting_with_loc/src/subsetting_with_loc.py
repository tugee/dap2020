#!/usr/bin/env python3

import pandas as pd

def subsetting_with_loc():
    df = pd.read_csv("src/municipal.tsv",sep="\t",index_col="Region 2018")
    df2 = df.loc["Akaa":"Äänekoski",["Population", "Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]
    return df2

def main():
    subsetting_with_loc()

if __name__ == "__main__":
    main()
