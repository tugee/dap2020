#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model as lm
import numpy as np
def main():
    coefficients = coefficient_of_determination()
    # print the coefficients here
    L = ["X1","X2","X3","X4","X5"]
    print("R2-score with feature(s) X:",coefficients[0])
    for i, k in enumerate(L,1):
        print(f"R2-score with feature(s) {k}: {coefficients[i]}")

def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = lm.LinearRegression(fit_intercept=True)
    K = []
    m1 = model.fit(df[["X1","X2","X3","X4","X5"]],df["Y"])
    r1 = model.score(df[["X1","X2","X3","X4","X5"]],df["Y"])
    L = ["X1","X2","X3","X4","X5"]
    K.append(r1)
    for k in L:
        x = df[k].values.reshape((-1,1))
        model.fit(x,df["Y"])
        K.append(model.score(x,df["Y"]))
    return K
    

if __name__ == "__main__":
    main()
