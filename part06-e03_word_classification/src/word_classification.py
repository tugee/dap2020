#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
 
    soon_to_be_array = []
    for x in a:
        lista = []
        for y in alphabet:
            lista.append(str(x).count(y))
        soon_to_be_array.append(lista)
 
    return np.array(soon_to_be_array)

def contains_valid_chars(s):
    for k in s:
        if k not in alphabet:
            return False
    return True

def get_features_and_labels():
    suomi = load_finnish()
    print(len(suomi))
    suomi = [s.lower() for s in suomi]
    suomi = [x for x in suomi if contains_valid_chars(x)]
    print(len(suomi))
    englanti = list(load_english())
    englanti = [x.lower() for x in englanti if (x[0].islower())]
    englanti = [x for x in englanti if contains_valid_chars(x)]
    print(len(englanti))
    englanti = get_features(englanti)
    suomi = get_features(suomi)
    X = np.vstack((suomi,englanti))
    a = np.zeros(len(suomi))
    b = np.ones(len(englanti))
    y = np.append(a,b,axis=0)
    return X, y


def word_classification():
    X, y = get_features_and_labels()
    a = model_selection.KFold(n_splits=5,shuffle=True,random_state=0)
    model = MultinomialNB()
    model.fit(X,y)
    L = cross_val_score(model,X,y,cv=a)
    return L


def main():
    a = np.array(["abc", "zaka"])
    f = get_features(a)
    get_features_and_labels()
    print(f)
    #print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
