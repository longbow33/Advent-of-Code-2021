with open("input.txt","r") as f:
    inp = f.read().split("\n")

temp = 9999
counter = 0
for i,line in enumerate(inp[:-1]):
    if (int(line) > temp):
        counter+=1
    temp = int(line)

for i in range(len(inp[:-1])):
        inp[i] = int(inp[i])
count = 0
for i in range(len(inp[:-4])):
    A = sum(inp[i:i+3])
    B = sum(inp[i+1:i+4])
    if A<B:
        count+=1


print(count)
