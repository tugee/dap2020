#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    mask = df["m"]==7
    df1 = df[mask]
    df2 = df1["Air temperature (degC)"]
    return df2.mean()
def main():
    print("Average temperature in July: "+str())
    return

if __name__ == "__main__":
    main()
