#!/usr/bin/env python3

def word_frequencies(filename):
    wordCount={}
    with open(filename, "r") as f:
        for line in f:
            words = line.split(" ")
            for word in words:
                word1 = word.strip("""!"#$%&'()*,-./:;?@[]_\n""")
                if not(word1 in wordCount):
                    wordCount[word1]=1
                else:
                    wordCount[word1]+=1
    return wordCount

def main():
    words = word_frequencies("alice.txt")
    print(words)


if __name__ == "__main__":
    main()
