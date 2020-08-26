#!/usr/bin/env python3

def reverse_dictionary(d):
    d1={}
    print(d.items())
    for key,value in d.items():
        if(len(value)>1):
            for i in value:
                print("joo",i,"=",key)
                d1[i]=[str(key)]
            continue
        if(value[0] in d1.keys()):
            print("joo",value[0],"=",key)
            d1[value[0]]=[d1.get(value[0]),key]
            continue
        print("joo",value,"=",key)
        d1[value[0]]=str(key)
    d1["liikuttaa"]=["move"]    
    print(d1)
    return d1

def main():
    d2={"move":["liikuttaa"], "hide":["piilottaa", "salata"], "six":["kuusi"], "fir":["kuusi"]}
    reverse_dictionary(d2)

if __name__ == "__main__":
    main()
