#!/usr/bin/env python3

class Rational(object):
    def __init__(self,os,nim):
        self.os = os
        self.nim = nim
     
    def __str__(self):
        return (str(self.os)+"/"+str(self.nim))
    def __add__(self,b):
        return Rational((self.os*b.nim+self.nim*b.os),(self.nim*b.nim))
    def __sub__(self,b):
        return  Rational((self.os*b.nim-self.nim*b.os),(self.nim*b.nim))
    def __mul__(self,b):
        return Rational((self.os*b.os),(self.nim*b.nim))
    def __truediv__(self,b):
        return Rational((self.os*b.nim),(self.nim*b.os))
    def __eq__(self,b):
        if self.os/self.nim==b.os/b.nim:
            return True
        return False
    def __gt__(self,b):
        if self.os/self.nim>b.os/b.nim:
            return True
        return False
    def __lt__(self,b):
        if self.os/self.nim<b.os/b.nim:
            return True
        return False
    
    pass

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
