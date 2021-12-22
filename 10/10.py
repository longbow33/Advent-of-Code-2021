import time
import statistics 

with open("input.txt" ,"r") as f:
    inp = f.read().split("\n")[:-1]

openers = ['{','[','<','(']
closers = ['}',']','>',')']
res = 0
falsechars = []
goodLines = []
for index,line in enumerate(inp):
    print(index,line)
    #time.sleep(1)
    toClose = []
    lineCorrect = True
    for char in line:
        if char in openers:
            toClose.append(char)
        if char in closers:
            aqOpener = openers[closers.index(char)]
            #print(char,aqOpener,"HIER IST DAS PAAR")
            if aqOpener == toClose[-1]:
                #print(toClose[-1],"removed")
                del toClose[-1]
            else:
                lineCorrect = False
                print(char,"found",toClose[-1],"expected")
                print("breaking")
                falsechars.append(char)
                if char == ')':
                    res+=3
                if char == ']':
                    res+=57
                if char == '}':
                    res+=1197
                if char == '>':
                    res+=25137
                break
    if lineCorrect:
        goodLines.append([line,toClose])


print(res)
print(falsechars)

print("-------------------")
points = []
for line in goodLines:
    print(line[1])
    res2=0
    line[1].reverse()
    for char in line[1]:
        res2*=5
        if char == '(':
            res2+=1
        if char == '[':
            res2+=2
        if char == '{':
            res2+=3
        if char == '<':
            res2+=4
    points.append(res2)
print(statistics.median(points))

