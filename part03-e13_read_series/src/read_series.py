#!/usr/bin/env python3
import pandas as pd    # This is the standard way of importing the Pandas library
import numpy as np


def read_series():
    tussu = pd.Series()
    while True:
        try:  
            kakka = input("Syötä: ")
            paska = kakka.split()
            if kakka == "":
                break
            if len(paska)!=2:
                raise ValueError("ohno")
            tussu.set_value(str(paska[0]),str(paska[1]))
        except ValueError as exp:
            print ("Error", exp)
        print(tussu)
    return tussu

def main():
    read_series()

if __name__ == "__main__":
    main()
