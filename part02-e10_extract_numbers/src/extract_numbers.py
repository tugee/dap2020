#!/usr/bin/env python3

def extract_numbers(s):
    L = []
    kakka = s.split()
    print(kakka)
    for sana in kakka:
        try:
            x = int(sana)
            L.append(x)
            continue
        except ValueError:
            try:
                x = float(sana)
                L.append(x)
                continue
            except ValueError:
                continue
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
