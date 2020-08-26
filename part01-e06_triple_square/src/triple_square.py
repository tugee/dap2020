#!/usr/bin/env python3


def main():
    for i in range(1,10):
        a=triple(i)
        b=square(i)
        if(a<b):
            break
        print("triple("+str(i)+")==",end="")
        print(a,end="")
        print(" square("+str(i)+")==",end="")
        print(b)

        
def triple(a):
    return a*3
def square(b):
    return b**2

if __name__ == "__main__":
    main()
