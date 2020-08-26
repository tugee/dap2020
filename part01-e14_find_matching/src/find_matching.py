#!/usr/bin/env python3

def find_matching(L, pattern):
    K = []
    for i,string in enumerate(L):
        if pattern in string:
            K.append(i)
    return K

def main():
    pass

if __name__ == "__main__":
    main()
