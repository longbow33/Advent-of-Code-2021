import numpy as np

with open("input.txt","r") as f:
    inp = f.read().split("\n")
    inp = inp[:-1]

def split(word):
    return list(word)

def toBinary(arr):
    res = 0
    for i in range(len(arr)):
        potenz = len(arr)-i-1
        spot = i
        res+=arr[spot]*2**potenz
    return res

for i in range(len(inp)):
    inp[i] = split(inp[i])

inp = np.array(inp, dtype =np.int_)

gamma = []
eps = []
for i in range(len(inp[0])):
    temp = inp[:,i]
    counts = np.bincount(temp)
    if counts[0]<counts[1]:
        gamma.append(1)
        eps.append(0)
    else:
        gamma.append(0)
        eps.append(1)

epsdez = toBinary(eps)
gammadez = toBinary(gamma)

print(gammadez," G ", epsdez," E")
result = epsdez*gammadez
print("RESULT:",result)
print("-----------------------------")


import pandas as pd

def oxy(inp):
    df = pd.DataFrame(inp,columns = range(len(inp[0])))

    for i in range(len(inp[0])):
        most  = np.bincount(df[i])
        if len(most) == 1:
            return df
        if most[0]<=most[1]: #wenn 1 häufiger vorkommt
            df = df[df[i] == 1]
        else:
            df = df[df[i] == 0]
    return df

oxygen = oxy(inp)


def co2f(inp):
    df = pd.DataFrame(inp,columns = range(len(inp[0])))

    for i in range(len(inp[0])):
        most = np.bincount(df[i])
        if len(df) == 1:
            return df
        if most[0]<=most[1]:#wenn 0 öfter oder gleichoft
            df = df[df[i] == 0]
        else:
            df = df[df[i] == 1]

    return df
    
co2 = co2f(inp)

print(oxygen,"\n-----------------------\n",co2)

oxygen = oxygen.values.tolist()
co2 = co2.values.tolist()

oxygen = np.array(oxygen).flatten()
co2 = np.array(co2).flatten()

oxygen = toBinary(oxygen)
co2 = toBinary(co2)

print(oxygen*co2)

