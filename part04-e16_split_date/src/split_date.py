#!/usr/bin/env python3

import pandas as pd
import numpy as np

def mapDate(a):
    paivat = ["ma","ti","ke","to","pe","la","su"]
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    return days[paivat.index(a)]

def mapMonth(a):
    kuukausi = ["tammi","helmi","maalis","huhti","touko","kesä","heinä","elo","syys","loka","marras","joulu"]
    return kuukausi.index(a)+1

def split_date():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")
    df[["Weekday","Day","Month","Year","Hour"]] = df["Päivämäärä"].str.split(expand=True)
    df["Month"]=df["Month"].apply(lambda x: int(mapMonth(x)))
    df["Weekday"]=df["Weekday"].apply(lambda x: mapDate(x))
    df["Hour"]=df["Hour"].apply(lambda x: int(x.split(":")[0]))
    df["Day"]=df["Day"].map(int)
    df["Year"]=df["Year"].map(int)

    return df[["Weekday","Day","Month","Year","Hour"]]

def main():
    df=split_date()
    print(split_date())
    print("dtypes:", df.dtypes)
    print(df)
if __name__ == "__main__":
    main()
