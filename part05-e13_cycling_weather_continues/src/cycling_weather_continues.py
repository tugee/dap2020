#!/usr/bin/env python3


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

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

    df = pd.concat([df[["Day","Month","Year"]],df1],axis=1)
    df = df.groupby(by=["Year","Month","Day"]).sum()
    df = df.fillna(method='ffill')
    df3 = pd.merge(df,df2,left_on=["Year","Month","Day"],right_on=["Year","m","d"])
    df3 = df3.drop(["m","d","Time zone","Time"],axis=1)
    return df3.fillna(method="ffill")


def cycling_weather_continues(station):
    df = cycling_weather()
    df = df[[station,"Precipitation amount (mm)","Snow depth (cm)","Air temperature (degC)"]]
    model = LinearRegression(fit_intercept=True)
    model.fit(df[["Precipitation amount (mm)","Snow depth (cm)","Air temperature (degC)"]],df[station])
    score = model.score(df[["Precipitation amount (mm)","Snow depth (cm)","Air temperature (degC)"]],df[station])
    a, b, c = model.coef_
    return ((a, b, c), score)
    
def main():
    station = "Baana"
    tupl, score = cycling_weather_continues(station)
    print("Measuring station:", station)
    print(f"Regression coefficient for variable \'precipitation\': {tupl[0]:.1f}")
    print(f"Regression coefficient for variable \'snow depth\': {tupl[1]:.1f}")
    print(f"Regression coefficient for variable \'temperature\': {tupl[2]:.1f}")
    print(f"Score: {score:.2f}")

if __name__ == "__main__":
    main()
