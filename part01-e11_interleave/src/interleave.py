#!/usr/bin/env python3

def interleave(*lists):
    lista = []
    for a in zip(*lists):
        print(zip(*lists))
        lista.extend([*a])
    return lista

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
