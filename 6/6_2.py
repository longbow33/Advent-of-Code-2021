import numpy as np
from collections import Counter
import pandas as pd
import time
with open("input.txt","r") as f:
    inp = f.read().strip("\n").split(",")
    inp = np.array(inp,dtype = int)

def shift(arr):
    for i in range(len(arr)):
        arr[i] -=1
        if arr[i] ==-1:
            arr[i] =8

    return arr


cnt = sorted(Counter(inp).items())

fishes = np.zeros(9)


for i in cnt:
    fishes[i[0]] = i[1]
#fishes[time to repr] = count of fishes
#for each timestep, shift the fishes one down, then put the count of fishes[0] to fishes[6] and fishes[8]
print(fishes)
t = 256
for step in range(t):
    #for every day do the following
    tempfish = np.zeros(9)
    for i in range(len(fishes)):#for every group of fishes 
        if i!=0:
            tempfish[i-1] += fishes[i]
        else:
            tempfish[6] += fishes[0]
            tempfish[8] += fishes[0]
    fishes = tempfish
    print(fishes)
    time.sleep(.01)
print(sum(fishes))
