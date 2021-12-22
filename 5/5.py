import re
import numpy as np
import collections

with open("input.txt","r") as f:
    inp = f.read()

regex = r"(\d*,\d*) -> (\d*,\d*)"

matches = re.finditer(regex,inp,re.MULTILINE)
lines = []

def sign(x):
    return(x)//abs(x)

def linepoints(x1,y1,x2,y2):
    print((x1,y1),(x2,y2))
    temp = []
    if y1==y2:
        if x1>x2:
            x1,x2 = x2,x1
        for i in range1(x1,x2):
            lines.append((i,y1))
    
    elif x1==x2:
        if y1>y2:
            y1,y2 = y2,y1
        for i in range1(y1,y2):
            lines.append((x1,i))
    
    else:
        if x1>x2:
            x = range(x1,x2-1,-1)
        else:
            x = range(x1,x2+1)

        if y1>y2:
            y= range(y1,y2-1,-1)
        else:
            y = range(y1,y2+1)
        print(x,y)
        for i in range(len(y)):
            lines.append((x[i],y[i]))

    
def range1(start,end):
    return range(start,end+1,)

for matchnum, match in enumerate(matches):
    #print(match.group(1),match.group(2))
    v1 = match.group(1).split(",")
    v2 = match.group(2).split(",")
    x1 = int(v1[0])
    y1 = int(v1[1])
    x2 = int(v2[0])
    y2 = int(v2[1])

    lines.append(linepoints(x1,y1,x2,y2))
    print("one done")    
    


occurences = collections.Counter(lines)

finsum = 0
for key,value in occurences.items():
    #print(key,value)
    if value >=2 and key != None:
        print(key,value)
        finsum+=1

print("finished with result: ",finsum)
