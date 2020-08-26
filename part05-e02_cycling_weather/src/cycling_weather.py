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

def cycling_weather():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", sep=";")
    df2 = pd.read_csv("src/kumpula-weather-2017.csv",sep=",")

    df = df.dropna(axis=0, how="all")
    df = df.dropna(axis=1, how="all")
    df1=df.loc[:,"Auroransilta":]

    df[["Weekday","Day","Month","Year","Hour"]] = df["Päivämäärä"].str.split(expand=True)
    df["Month"]=df["Month"].apply(lambda x: int(mapMonth(x)))
    df["Weekday"]=df["Weekday"].apply(lambda x: mapDate(x))
    df["Hour"]=df["Hour"].apply(lambda x: int(x.split(":")[0]))
    df["Day"]=df["Day"].map(int)
    df["Year"]=df["Year"].map(int)

    df = pd.concat([df[["Weekday","Day","Month","Year","Hour"]],df1],axis=1)

    df3 = pd.merge(df,df2,left_on=["Year","Month","Day"],right_on=["Year","m","d"])
    df3 = df3.drop(["m","d","Time zone","Time"],axis=1)

    print(df3)
    return df3


def main():
    df=cycling_weather()
    print("dtypes:", df.dtypes)
    print(df)

if __name__ == "__main__":
    main()