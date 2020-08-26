#!/usr/bin/env python3

def positive_list(L):
    kakka = list(filter(is_positive,L))
    return kakka
def is_positive(x):
    if(x<=0):
        return 0
    else: return 1

def main():
    L = [2,-2,0,1,-7]
    positive_list(L)

if __name__ == "__main__":
    main()
