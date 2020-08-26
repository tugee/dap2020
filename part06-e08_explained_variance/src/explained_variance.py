#!/usr/bin/env python3
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t",header=0)
    pca=PCA(10)
    pca.fit(df)
    return list(df.var()), pca.explained_variance_

def main():
    v, ev = explained_variance()
    print("The variances are:",*(f"{x:.3f}" for x in v))
    print(f"The explained variances after PCA are:",*(f"{x:.3f}" for x in ev))
    plt.plot(np.arange(1,11), np.cumsum(ev))
    plt.show()
    print(sum(v), sum(ev))

if __name__ == "__main__":
    main()
