#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    x = (-1*b+math.sqrt((b**2)-4*a*c))/(2*a)
    y = (-1*b-math.sqrt((b**2)-4*a*c))/(2*a)
    return (x,y)

def main():
    print(solve_quadratic(1,-3,2))
    print(solve_quadratic(1,2,1))
    pass

if __name__ == "__main__":
    main()
