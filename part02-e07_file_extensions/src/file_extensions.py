#!/usr/bin/env python3

import re

def file_extensions(filename):
    L = []
    dictionary = {}
    with open(filename, "r") as f:
        for line in f:
            nimi = re.findall(r"(\w+)",line)
            line1 = line.strip("\n")
            if len(nimi)>2:
                if nimi[len(nimi)-1] in dictionary.keys():
                    dictionary.get(nimi[len(nimi)-1]).append(line1)
                else:
                    dictionary[nimi[len(nimi)-1]]=[line1]
            elif len(nimi)==1:
                L.append(line.strip("\n"))
            else:
                if nimi[1] in dictionary.keys():
                    dictionary.get(nimi[1]).append(line1)
                else:
                    dictionary[nimi[1]]=[line1]
                
    return (L, dictionary)

def main():
    L, d = file_extensions("src/filenames.txt")
    print(str(len(L))+" files with no extension")
    for key in d.keys():
        print(key+" "+str(len(d.get(key))))

if __name__ == "__main__":
    main()
