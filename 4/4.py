import numpy as np
import re
import time

with open("input.txt","r") as f:
    inp = f.read().split("\n\n")

numbers = inp[0].split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

boards = inp[1:]
def clean_boards(boards):    
    regex  = r"(\d+)"
    new_boards = []
    for i in boards:
        temp = []
        matches = re.finditer(regex,i)
        for matchNum,match in enumerate(matches):
            temp.append(int(match.group()))
        temp = np.dstack((np.array(temp).reshape(5,5),np.zeros((5,5))))
        new_boards.append(temp)
    return np.array(new_boards)


boards = clean_boards(boards)

class Board():
    def __init__(self,board):
        self.board = board[:,:,0]
        self.hits = np.array(board[:,:,1],dtype = np.dtype(bool))

    def check_bingo(self):
        if np.any(np.all(self.hits==True,axis=0)):
            #print(self.board)
            ##print(self.hits)
            return True
        elif np.any(np.all(self.hits==True,axis=1)):
            #print(self.board)
            #print(self.hits)
            return True
        return False

    
    def make_board(self):
        return(np.dstack((self.board,self.hits)))

    def update_hits(self,number):
        indices = np.where(self.board == number)
        self.hits[indices] = True
        return self.hits
    
    def get_final_score(self):
        indices = np.where(self.hits == False)
        #print(indices)
        finsum = 0
        for i in range(len(indices[0])):
            finsum += self.board [indices[0][i],indices[1][i]]
        return finsum
    
boards = [Board(board) for board in boards]

for number in numbers:

    for boardie in boards:
        boardie.hits = boardie.update_hits(number)
    checker = [boardie.check_bingo() for boardie in boards]
    #print(checker)
    if np.any(checker) == True:
        boardnum = np.where(checker)[0]
        print(np.where(checker)[0],"CHECKER")
        print("--------------------",number)
        #print(boards[boardnum].board,"\n",boards[boardnum].hits)
        #final_score = boards[boardnum].get_final_score()
        #print(final_score*number)
        delboards = []
        for num in boardnum:
            delboards.append(boards[num])
            print(num,"is out",len(boards),"remaining")
            print(boards[num].hits)
        if len(boards)>=2:
            for board in delboards:
                print(boards.pop(boards.index(board)),"popped")
        else:
            winning_board = boards[0]
            print("winning board found",number)
            print(winning_board.board)
            print(winning_board.hits)
            print(winning_board.get_final_score()*number)
            exit()
    time.sleep(.1)


  
