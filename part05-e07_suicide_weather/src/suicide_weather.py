#!/usr/bin/env python3

import pandas as pd
import numpy as np

def suicide_fractions():
    df = pd.read_csv("src/who_suicide_statistics.csv", sep =",",header=0)
    df["frac"]=df["suicides_no"]/df["population"]
    df1 = df.groupby("country")["frac"].mean()
    return df1
    
def suicide_weather():
    df = pd.read_html("src/List_of_countries_by_average_yearly_temperature.html",header=0)[0]
    print(df)    
    df1 = suicide_fractions()
    print(df1)
    df2=pd.merge(df,df1,left_on="Country",right_on="country")
    df2.set_index("Country",inplace = True)
    df2.iloc[:,0] = df2.iloc[:,0].map(lambda s: float(s.replace("\u2212", "-")))
    print(df2)
    asd = df2.corr(method="spearman").iloc[0,1]
    print(asd)
    return (df1.shape[0],df.shape[0] , df2.shape[0], asd)

def main():
    row1, row2, row3, corr = suicide_weather()
    print("Suicide DataFrame has",row1,"rows")
    print("Temperature DataFrame has",row2,"rows")
    print("Common DataFrame has",row3,"rows")
    print("Spearman correlation:",corr)

if __name__ == "__main__":
    main()
