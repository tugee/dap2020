#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv",sep=";")
    df1=df.dropna(axis=0,how="all")
    return df1.dropna(axis=1,how="all")


def main():
    cyclists()
    
if __name__ == "__main__":
    main()
