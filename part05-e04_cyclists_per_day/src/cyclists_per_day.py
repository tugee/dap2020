#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def mapDate(a):
    paivat = ["ma","ti","ke","to","pe","la","su"]
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    return days[paivat.index(a)]

def mapMonth(a):
    kuukausi = ["tammi","helmi","maalis","huhti","touko","kesä","heinä","elo","syys","loka","marras","joulu"]
    return kuukausi.index(a)+1

def cyclists_per_day():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")

    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")
    df1=df.loc[:,"Auroransilta":]
    df[["Weekday","Day","Month","Year","Hour"]] = df["Päivämäärä"].str.split(expand=True)
    df["Month"]=df["Month"].apply(lambda x: int(mapMonth(x)))
    df["Weekday"]=df["Weekday"].apply(lambda x: mapDate(x))
    df["Hour"]=df["Hour"].apply(lambda x: int(x.split(":")[0]))
    df["Day"]=df["Day"].map(int)
    df["Year"]=df["Year"].map(int)
    df2 = pd.concat([df[["Day","Month","Year"]],df1],axis=1)
    df2 = df2.groupby(by=["Year","Month","Day"]).sum()
    return df2

def main():
    df=cyclists_per_day()
    df.loc[(2017,8)].plot()
    plt.show()
    print("dtypes:", df.dtypes)
    print(df)
if __name__ == "__main__":
    main()