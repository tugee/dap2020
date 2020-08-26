#!/usr/bin/env python3

import math


def main():
    while(1):
        inp=input("Choose a shape (triangle, rectangle, circle):" )
        if(inp == ""):
            break
        if inp=="triangle":
            base=int(input("Give base of the triangle:" ))
            height=int(input("Give height of the triangle:" ))
            print("The area is "+'{:07.6f}'.format(base*height/2))
            continue
        if inp=="rectangle":
            base=int(input("Give width of the rectangle:" ))
            height=int(input("Give height of the rectangle:" ))
            print("The area is "+'{:07.6f}'.format(base*height))
            continue
        if inp=="circle":
            radius=int(input("Give radius of the circle:" ))
            print("The area is "+'{:07.6f}'.format(radius**2*math.pi))
            continue
        else:
            print("Unknown shape!")
            continue
    # enter you solution here

if __name__ == "__main__":
    main()
