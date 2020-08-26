#!/usr/bin/env python3

import scipy
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    X,y = load_iris(return_X_y=True)
    print(y)
    model=KMeans(n_clusters = 3, random_state=0)
    model.fit(X,y)
    print(model.labels_)
    permutation3 = find_permutation(3, y, model.labels_)
    print(permutation3)
    acc = accuracy_score(y, [ permutation3[label] for label in model.labels_])
    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
