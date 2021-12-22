import numpy as np

with open("bsp.txt","r") as f:
    inp = f.read().split("\n")
    inp = inp[:-1]
for i in range(len(inp)):
    inp[i] = inp[i].split(" ")
    inp[i].remove("|")

def add_possible(pattern,elem,pos):
    for char in elem:
        for place in pos:
            if char not in pattern[place]:
                pattern[place] += char
    return pattern

for line in inp:
    pospatt = np.zeros(7,dtype="<U10")
    for word in line:
        dig = len(word)
        print(word)
        if dig in [1,2,3,6]:
            print("entered")
            if dig == 2:
                pos = [2,5]
                pospatt = add_possible(pospatt,word,pos)
            if dig == 3:
                pos = [0,2,5]
                pospatt = add_possible(pospatt,word,pos)
            if dig == 4:
                pos = [1,2,3,5]
                pospatt = add_possible(pospatt,word,pos)
            if dig == 7:
                pos = range(7)
                pospatt = add_possible(pospatt,word,pos)

    print(pospatt)
    exit()

