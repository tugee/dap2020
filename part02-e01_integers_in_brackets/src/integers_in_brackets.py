#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    s=re.findall(r'\[\s*([+-]?\d+)\s*\]' ,s)
    lista=list(map(int,s))
    return lista

def main():
    pass

if __name__ == "__main__":
    main()
