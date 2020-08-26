#!/usr/bin/env python3

import scipy.stats
import numpy as np

def load():
    import pandas as pd
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

def lengths():
    iris=load()
    print(iris)
    return scipy.stats.pearsonr(iris[:,0],iris[:,2])[0]


def correlations():
    iris = load()
    kakka = np.corrcoef(iris.T)
    return np.array(kakka)

def main():
    print(lengths())
    print(correlations())

if __name__ == "__main__":
    main()
