#!/usr/bin/env python3

def distinct_characters(L):
    d = {}
    for i in L:
        s=set(i)
        d[i]=len(s)
    return d

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
