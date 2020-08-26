#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv",sep="\t",index_col="Region 2018")
    df1 = df["Akaa":"Äänekoski"]
    mask = (df1["Share of Swedish-speakers of the population, %"] > 5) & (df1["Share of foreign citizens of the population, %"]>5)
    df2=df1[mask]
    return df2[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]


def main():
    swedish_and_foreigners()
    return

if __name__ == "__main__":
    main()
