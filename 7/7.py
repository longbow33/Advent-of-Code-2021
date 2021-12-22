import numpy as np
with open("input.txt","r") as f:
    inp = f.read().strip("\n").split(",")

pos = np.array(inp,dtype= int)

def gaussSum(dist):
    return(((dist**2)+dist)//2)

print(pos)

## i = 0, pos = 5 -> 5+4+3+2+1
costs = np.zeros(((2,max(pos)+1)),dtype= int)
for i in range(max(pos+1)):
    costs[0][i] = i
    costs[1][i] = sum(gaussSum(abs(pos-i)))

print(costs[np.where(costs == min(costs[1]))])
