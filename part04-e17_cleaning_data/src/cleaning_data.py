#!/usr/bin/env python3

import pandas as pd
import numpy as np


def cleaning_data():
    asd = [["Donald Trump",2017,np.nan,1,"Mike Pence"],["Barack Obama",2009,2017,2,"Joe Biden"],["George Bush",2001,2009,2,"Dick Cheney"],["Bill Clinton",1993,2001,2,"Al Gore"]]
    d = pd.DataFrame(asd,columns=["President","Start","Last","Seasons","Vice-president"])
    return d

def main():
    cleaning_data()

if __name__ == "__main__":
    main()
