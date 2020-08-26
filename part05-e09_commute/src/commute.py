#!/usr/bin/env python3

import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def mapDate(a):
    paivat = ["ma","ti","ke","to","pe","la","su"]
    days = [1,2,3,4,5,6,7]
    return days[paivat.index(a)]

def mapMonth(a):
    kuukausi = ["tammi","helmi","maalis","huhti","touko","kesä","heinä","elo","syys","loka","marras","joulu"]
    return kuukausi.index(a)+1

def bicycle_timeseries():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")
    df[["Weekday","Day","Month","Year","Hour"]] = df["Päivämäärä"].str.split(expand=True)
    df["Month"]=df["Month"].apply(lambda x: int(mapMonth(x)))
    df["Weekday"]=df["Weekday"].apply(lambda x: mapDate(x))
    df["Day"]=df["Day"].map(int)
    df["Year"]=df["Year"].map(int)
    df["Hour"]=df["Hour"].apply(lambda x: int(x.split(":")[0]))
    mask = ((df["Year"]==2017))
    df = df.loc[mask,:]
    df["Date"]=pd.to_datetime(df[["Year", "Month", "Day","Hour"]])
    df = df.drop(columns=["Päivämäärä","Day","Month","Year","Hour"])
    print(df)
    return df

def commute():
    return bicycle_timeseries()
    
def main():
    df = commute()
    plt.plot(df)
    plt.show()


if __name__ == "__main__":
    main()
