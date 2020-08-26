#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []
    with open(filename, "r") as f:
        next(f)
        for line in f:
            if(line ==""):
                break
            regex = re.search(r"(\d+)\W+(\d+)\W+(\d+)\W+(.*)",line)
            red = regex.group(1)
            green = regex.group(2)
            blue = regex.group(3)
            name = regex.group(4)
            string = red+"\t"+green+"\t"+blue+"\t"+name
            L.append(string)
    return L


def main():
    pass

if __name__ == "__main__":
    main()
