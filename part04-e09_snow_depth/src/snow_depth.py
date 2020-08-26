#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    df = pd.read_csv("src/kumpula-weather-2017.csv")
    return max(df["Snow depth (cm)"])

def main():
    print("Max snow depth: "+str(round(snow_depth(),1)))
    return

if __name__ == "__main__":
    main()
