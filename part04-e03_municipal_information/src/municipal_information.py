#!/usr/bin/env python3

import pandas as pd
import numpy as np
def main():
    df = pd.read_csv("src/municipal.tsv",sep="\t")
    print("Shape:",str(df.shape[0])+","+str(df.shape[1]))
    print("Columns:")
    print("\n".join(df.columns))
    
    return


if __name__ == "__main__":
    main()
