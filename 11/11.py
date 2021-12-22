import numpy as np
import itertools
import time

with open("testinput.txt","r") as f:
    inp = f.read().split("\n")[:-1]

for i,line in enumerate(inp):
    inp[i] = [char for char in line]

class Octopus():
    def __init__(self,pos,elvl):
        self.pos = pos
        self.neighbours = get_neighbours(self.pos)
        self.elvl = elvl
        self.active = True
    
    def check_ray(self):
        if self.elvl > 9 and self.active:
            self.elvl = 0
            self.active = False
            return True
        else:
            return False

    def activate(self):
        self.active = True
    

def get_neighbours(idx):
    x = idx[0]
    y = idx[1]
    nx = [x-1,x,x+1]
    ny = [y-1,y,y+1]
    res = [val for val in  itertools.product(nx,ny) if all([nr<len(inp[0]) and nr >=0 for nr in val])]
    try:
        res.remove(idx)
    except:
        pass
    return res

def get_indices(inp):
    it = np.nditer(inp,flags = ['multi_index'])
    ret = []
    while not it.finished:
        ret.append(it.multi_index)
        it.iternext()
    return ret

inp = np.array(inp,dtype=int)
octopi = []
for i in get_indices(inp):
    i = list(i)
    print(i)
    spot = i
    elvl = inp[i]
    octopi[i[0],i[1]] = Octopus(spot,elvl)

for i in range(steps):
    print(step)
    time.sleep(1)


