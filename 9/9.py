import numpy as np

with open("input.txt","r") as f:
    inp = f.read().split("\n")[:-1]
heightmap = []

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

for line in inp:
    temp  = [x for x in line]
    heightmap.append(temp)

heightmap = np.array(heightmap,dtype = int)
print(heightmap)
print("................")
res = 0
mins = []
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        indexes = get_neighbours([x,y],heightmap.shape)
        print("X: ",x,"Y: ",y)
        neighbours = []

        indexes.append([get_neigbours[spot[0],spot[1]] for spot in indexes if heightmap[x,y] !=9])
        for idx in indexes:
            neighbours.append(heightmap[idx[0],idx[1]])
        print(heightmap[x,y],"stelle")
        print(neighbours,"neigh")
        if heightmap[x,y] < min(neighbours):
            res+= heightmap[x,y]+1
            mins.append(x,y)
    
print(res)
print(mins)
