#!/usr/bin/env python3

import sys

def file_count(filename):
    with open(filename, "r") as f:
        lines = 0
        chars = 0
        words = 0
        for line in f:
            print(line)
            lines+=1
            wordList = line.split()
            words += len(wordList)
            chars += sum(len(word) for word in wordList)
    return (lines, words, chars)

def main():
    for name in sys.argv[1:]:
        l, w, c = file_count(name)
        print(f"{l}\t{w}\t{c}\t{name}")

if __name__ == "__main__":
    main()
