#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc
import scipy

def toint(x):
    L = ["A","C","G","T"]
    a = []
    for char in x:
        a.append(L.index(char))
    if(len(x)==1):
        return a[0]
    return a 

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep = '\t', header=0)
    X = df.X.values
    X = [toint(y) for y in X]
    y = df.y.values
    return (np.array(X), np.array(y))

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X,y = get_features_and_labels(filename)
    model = AgglomerativeClustering(affinity="euclidean",linkage="average")
    model.fit(X)
    permutation3 = find_permutation(2, y, model.labels_)
    newLabels = [permutation3[label] for label in model.labels_]
    acc = accuracy_score(y, newLabels) 
    return acc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def cluster_hamming(filename):
    X,y = get_features_and_labels(filename)
    X2 = pairwise_distances(X,metric="hamming")
    model = AgglomerativeClustering(affinity="precomputed",linkage="average")
    model.fit(X2)
    permutation3 = find_permutation(2, y, model.labels_)
    newLabels = [permutation3[label] for label in model.labels_]
    acc = accuracy_score(y, newLabels) 
    return acc


def main():
    get_features_and_labels("src/data.seq")
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
