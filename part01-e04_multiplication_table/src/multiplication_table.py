#!/usr/bin/env python3


def main():
    for i in range(10):
        for k in range(10):
            if(k == 9):
                print('{:4d}'.format((k+1)*(i+1)))
                continue
            print('{:4d}'.format((k+1)*(i+1)), " ", end="")
if __name__ == "__main__":
    main()