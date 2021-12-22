import numpy as np


def get_neighbours(idx,shape):
    x,y = idx
    xmax,ymax = shape
    neighbours = []
    if x+1 <= shape[0]-1:
        right = [x+1,y]
        neighbours.append(right)
    if x-1 >= 0:
        left = [x-1,y]
        neighbours.append(left)
    if y+1 <= shape[1]-1:
        down = [x,y+1]
        neighbours.append(down)
    if y-1 >= 0:
        up = [x,y-1]
        neighbours.append(up)
    
    return neighbours

def get_mins(arr):
    mins = []
    for idx,point in np.ndenumerate(arr):
        x,y = idx
        if point < min([arr[spot[0],spot[1]] for spot in get_neighbours(idx,arr.shape)]):
            mins.append(idx)
    return mins

def explore(arr,idx):
    #from idx look into every direction, and append values of neighbours, that are greater than the value of idx and not 9 to the basin array
    #if the new basin array is unchanged, return the basin array
    changed = True
    basin_spots = [idx]
    while (changed):
        new = []
        changed = False
        for spot in basin_spots:
            neigh = get_neighbours(spot,arr.shape)
            for n in neigh:
                if arr[n[0],n[1]] > arr[spot[0],spot[1]] and arr[n[0],n[1]] != 9:
                    new.append(tuple(n))
        if  new != basin_spots:
            changed = True
            print("changed")
    print("unchanged")
    res = len(basin_spots)
    return res

with open("testinput.txt","r") as f:
    inp = f.read().split("\n")[:-1]

for i in range(len(inp)):
    inp[i] = [x for x in inp[i]]

inp = np.array(inp, dtype = int)
inp = inp.reshape(-1,len(inp[0]))
minIdx = get_mins(inp)

for mini in minIdx:
    print(explore(inp,mini))
