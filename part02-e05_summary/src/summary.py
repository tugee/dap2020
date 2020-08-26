#!/usr/bin/env python3

import sys
import math

def summary(filename):
    L = []
    with open(filename, "r") as f:
        summa = 0
        i = 0
        for line in f:
            try:
                x=float(line)
                L.append(x)
                summa+=x
                i+=1
            except:
                print("error")
    if i == 0:
        average = 0
    else:
        average = summa/i
    variance = sum([((x - average) ** 2) for x in L]) / (len(L)-1)
    sd = variance ** 0.5
    return (float(summa),float(average),float(sd))

def main():
    for name in sys.argv[1:]:
        triple = summary(name)
        nimi = name
        print("File: "+name+" Sum: {:.6f} Average: {:.6f} Stddev: {:.6f}".format(triple[0],triple[1],triple[2]))

if __name__ == "__main__":
    main()
