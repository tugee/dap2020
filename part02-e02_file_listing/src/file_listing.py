#!/usr/bin/env python3
import re

def file_listing(filename="src/listing.txt"):
    L = []
    with open(filename, "r") as f:
        for line in f:
            if(line ==""):
                break
            name = re.findall(r"\S+?$",line)
            month = re.findall(r"\s([A-z]{3,3})\s",line)
            numbers = re.findall(r"(\w?[0-9]+)",line)
            print(numbers)
            numbers1 = re.findall(r"(?<=:)[0-9]+",line)
            L.append((int(numbers[1]),month[0],int(numbers[2]),int(numbers[3]),int(numbers1[0]),name[0]))
    return L

def main():
    print(file_listing())

if __name__ == "__main__":
    main()
