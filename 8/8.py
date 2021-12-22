import numpy as np

with open("testinput.txt","r") as f:
    inp = f.read().split("\n")
    inp = inp[:-1]

part2 = inp

for i in range(len(inp)):
    inp[i] =inp[i].split(" | ")

inp = np.array(inp)
part1 = inp[:,1]
res  = 0

def add_possible(pattern, elem, pos):
    for char in elem:
        for place in pos:
            pattern[place]+=char
    return(pattern)

for line in part1:
    word = line.split(" ")
    print(line,"line")
    pospatt = np.zeros(7,dtype="<U7")
    print(pospatt)
    for elem in word:
        print(elem)
        dig = len(elem)
        if dig == 7:#8
            res+=1
            print(elem)
        elif dig == 2:#1
            pos = [3,6]
            pospatt = add_possible(pospatt,elem,pos)
        elif dig == 4:#4
            pos = [2,3,4,6]
            pospatt = add_possible(pospatt,elem,pos)
        elif dig == 3:#7
            pos = [1,3,6]
            pospatt = add_possible(pospatt,elem,pos)
        else:
            pass
    print(pospatt)

print(res)
