#!/usr/bin/env python3
import gzip
from sklearn.model_selection import cross_val_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import model_selection
from sklearn import metrics
import numpy as np
from math import floor

def spam_detection(random_state=0, fraction=0.1):
    with gzip.open('src/ham.txt.gz', 'r') as f:
        ham = np.array(list(f))

    ham = ham[0:(int(len(ham)*fraction))]

    with gzip.open('src/spam.txt.gz', 'r') as f:
        spam = np.array(list(f))

    spam = spam[0:(int(len(spam)*fraction))]
    X = np.concatenate([ham,spam])
    y = np.hstack([np.zeros(len(ham)),np.ones(len(spam))])
    cv = CountVectorizer()
    Xfeats = cv.fit_transform(X)
    model = MultinomialNB()
    X_train, X_test, y_train, y_test = train_test_split(Xfeats,y,train_size=0.75,random_state=random_state)
    
    model.fit(X_train,y_train)
    y_fitted = model.predict(X_test)
    
    accuracy = metrics.accuracy_score(y_fitted,y_test)
    denominator = len(y_test)

    return accuracy,denominator, int((1-accuracy)*denominator)

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
