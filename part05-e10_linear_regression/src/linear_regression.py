#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model = LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis],y)
    return float(model.coef_), model.intercept_
    
def main():
    x=np.linspace(0, 10, 20)
    y=2*x+np.random.randn(20)
    slope, intercept = fit_line(x,y)
    print("Slope:",slope)
    print("Intercept:",intercept)
    xfit = np.linspace(0,10,100)
    yfit = slope*xfit+intercept
    plt.scatter(x, y, color="black")
    plt.plot(xfit,yfit,color="red")
    plt.show()
    
if __name__ == "__main__":
    main()
