#!/usr/bin/env python3

def sum_equation(L):
    if(L==[]):
        return "0 = 0"
    part1 = " + ".join([str(elem) for elem in L])
    sum = 0
    for integer in L:
        sum = sum + integer
    return part1 + " = "+str(sum)

def main():
    print(sum_equation([1,2,3]))

if __name__ == "__main__":
    main()
