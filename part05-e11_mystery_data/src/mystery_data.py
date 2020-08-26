#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv",sep="\t")
    model = LinearRegression(fit_intercept=False)
    model.fit(df[["X1","X2","X3","X4","X5"]],df["Y"])
    return model.coef_

def main():
    coefficients = mystery_data()
    # print the coefficients here
    L = ["X1","X2","X3","X4","X5"]
    for i, k in enumerate(L):
        print("Coefficient for",k,"is",coefficients[i])
    
    
if __name__ == "__main__":
    main()
