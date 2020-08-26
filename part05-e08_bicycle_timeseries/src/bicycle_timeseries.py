#!/usr/bin/env python3

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def mapMonth(a):
    kuukausi = ["tammi","helmi","maalis","huhti","touko","kesä","heinä","elo","syys","loka","marras","joulu"]
    return kuukausi.index(a)+1

def cyclists_per_day():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")
    df[["Weekday","Day","Month","Year","Hour"]] = df["Päivämäärä"].str.split(expand=True)
    df["Month"]=df["Month"].apply(lambda x: int(mapMonth(x)))
    df["Day"]=df["Day"].map(int)
    df["Year"]=df["Year"].map(int)
    df["Hour"]=df["Hour"].apply(lambda x: int(x.split(":")[0]))
    df["Date"]=pd.to_datetime(df[["Year", "Month", "Day","Hour"]])
    df = df.drop(columns=["Päivämäärä","Weekday","Day","Month","Year","Hour"])
    df = df.set_index("Date")
    print(df)
    return df

def bicycle_timeseries():
    return cyclists_per_day()


def main():
    bicycle_timeseries()

if __name__ == "__main__":
    main()
