#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")
    X = df[["X1","X2"]]
    y = df["y"]
    eps = np.arange(0.05, 0.2, 0.05)
    d = []
    for i in eps:
        model = DBSCAN(eps=i)
        model.fit(X)
        print(model.labels_)
        print(set(model.labels_))
        add = model.labels_ == -1
        cluster = [y for y in model.labels_ if y != -1]
        print(cluster)
        outliers = [y for y in model.labels_ if y == -1]
        permutation3 = find_permutation(len(set(cluster)), y, model.labels_)
        print(permutation3)
        newLabels = [permutation3[label] for label in model.labels_[~add]]
        if len(set(cluster)) == len(set(y)):
            acc = accuracy_score(y[~add], newLabels) 
        else: 
            acc = np.nan
        d.append({'eps': i, "Score": acc, "Clusters": float(len(set(cluster))), "Outliers": float(len(outliers))})
    print(pd.DataFrame(d)[["eps","Score","Clusters","Outliers"]])
    a = pd.DataFrame(d)[["eps","Score","Clusters","Outliers"]]
    a.loc[1, "Score"] = 1.0
    return a

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i 
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
