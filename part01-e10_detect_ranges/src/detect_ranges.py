#!/usr/bin/env python3

def detect_ranges(L):
    sortedL = sorted(L)
    sortedL.append(sortedL[-1]+2)
    potentialRange = []
    returnL = []
    j=0
    for i in sortedL:
        if(j>=len(sortedL)-1):
            break
        print("Onko"+ str(sortedL[j+1])+"=="+str(i+1))
        if i+1 == sortedL[j+1]:
            print("havaittu")
            potentialRange.append(i)
            j=j+1
            print(potentialRange)
            continue
        else:
            if(potentialRange == []):
                returnL.append(i)
                j=j+1
            else:
                print(str(j)+str(i) + "mitävittua")
                potentialRange.append(i)
                j=j+1
                returnL.append((potentialRange[0],potentialRange[-1]+1))
                potentialRange=[]
    print(potentialRange)
    return returnL
            

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10,11, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
