#!/usr/bin/env python3

import pandas as pd
def swedish_and_foreigners():
    df = 
    df1 = df["Akaa":"Äänekoski"]
    mask = (df1["Share of Swedish-speakers of the population, %"] > 5) & (df1["Share of foreign citizens of the population, %"]>5)
    df2=df1[mask]
    return df2

def growing_municipalities(df):
    mask = df["Population change from the previous year, %"] > 0
    return ((df[mask].shape[0])/(df.shape[0]))

def main():
    number = growing_municipalities(swedish_and_foreigners())
    print("Proportion of growing municipalities: " + str(round(number*100,1))+"%")

if __name__ == "__main__":
    main()
