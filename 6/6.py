with open("input.txt","r") as f:
    inp = f.readline().strip("\n").split(",")

class Lanternfish():
    def __init__(self,timer = 9):
        self.timer = timer
    def tick(self):
        if self.timer == 0:
            self.timer = 6
            return (self.reproduce())
        self.timer -=1
    def reproduce(self):
        return Lanternfish()

fishes = []
for time in inp:
    fishes.append(Lanternfish(int(time)))

t =256
for i in range(t):
    for fish in fishes:
        ret = fish.tick()
        if ret is not None:
            fishes.append(ret)
            #print("appended")
    #print([fish.timer for fish in fishes])
    if i%20 == 0:
        print(i)
print(len(fishes))
