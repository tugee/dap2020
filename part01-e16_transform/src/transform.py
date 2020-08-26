#!/usr/bin/env python3

def transform(s1, s2):
    S=s1.split()
    S2=s2.split()
    S=map(int,S)
    S2=map(int,S2)
    multiplication = [a*b for a,b in zip(S,S2)]
    print(multiplication)
    return multiplication

def main():
    transform("1 5 3", "2 6 -1")

if __name__ == "__main__":
    main()
