with open("input.txt","r") as f:
    inp = f.read().split("\n")

state = [0,0,0] #hor,ver,aim

for i in inp[:-1]:
    try:
        i = i.split(" ")
        dr = i[0]
        vl = int(i[1])
    except:
        print(i,"failed")
        exit()


    if dr == "forward":
        state[0]+=vl
        state[1]+=(state[2]*vl)
    elif dr == "up":
        state[2]-=vl
    elif dr == "down":
        state[2]+=vl

print(state,state[0]*state[1])
