import math
from XO import *

class Board:
    player = 1
    check = 0
    arrXO = []
    arrMatrix = []
    offset = 0
    size = 0
    row = 0
    col = 0
    
    def __init__(self, row, col, size, offset) -> None:
        self.row = row
        self.col = col
        self.size = size
        self.offset = offset
        self.check = 1
        self.player = 1
        for i in range(0, self.row):
            line = []
            self.arrMatrix.append([])
            for j in range(0, self.col):
                mx = self.offset + j*self.size
                my = self.offset + i*self.size
                line.append(XO(mx, my, mx + self.size, my + self.size))
                self.arrMatrix[i].append(0)
            self.arrXO.append(line)
        
    def drawBoard(self, cas):
        for i in range(0, self.row):
            for j in range(0, self.col):
                self.arrXO[i][j].draw(cas)
                        
    def drawXO(self, cas, x, y):
        if self.check == 1:
            self.arrXO[x][y].value = self.player
            self.arrMatrix[x][y] = self.player
            self.arrXO[x][y].draw(cas)
            if self.isWin(x, y) == 1:
                self.check = 0
                self.log(cas)
            else:
                self.player = self.player*(-1)
    
    def clickXO(self, cas, x, y):
        x=math.ceil((x-50)/30)-1
        y=math.ceil((y-50)/30)-1
        print(x,y)
        if x >= 0 and y >= 0 and x < self.row and y < self.col and self.arrMatrix[y][x] == 0:
            self.drawXO(cas , y ,x)
            return True
        else:
            return False
    
    def isWin(self, mi, mj):
        if self.checkVertical(mi, mj) == 1 or self.checkHorizontal(mi, mj) == 1 or self.checkLeftDiagonal(mi, mj) == 1 or self.checkRightDiagonal(mi, mj) == 1:
            return 1
        else: return 0

    def checkHorizontal(self, mi, mj):
        #  left
        i = mi
        j = mj - 1
        count = 0
        if j < 0: j = 0
        while j >= 0:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            j -= 1
        # right
        i = mi
        j = mj + 1
        if j > self.col: j = self.col
        while j < self.col:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else:
                break
            j += 1
        if count >= 4: return 1
        else: return 0

    def checkVertical(self, mi, mj):
        # up
        i = mi - 1
        j = mj
        count = 0
        if i < 0: i = 0
        while i >= 0:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i -= 1
        #  down
        i = mi + 1
        j = mj
        while i < self.row:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i += 1
        if count >= 4: return 1
        else: return 0
        
    def checkLeftDiagonal(self, mi, mj):
        #  up
        i = mi - 1
        j = mj - 1
        count = 0
        while i >= 0 and j >= 0:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i -= 1
            j -= 1
        # down
        i = mi + 1
        j = mj + 1
        while i < self.row and j < self.col:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i += 1
            j += 1
        if count >= 4: return 1
        else: return 0

    def checkRightDiagonal(self, mi, mj):
        #  up
        i = mi - 1
        j = mj + 1
        count = 0
        while i >= 0 and j < self.col:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i -= 1
            j += 1
        # down
        i = mi + 1
        j = mj - 1
        while i < self.row and j >= 0:
            if self.arrXO[i][j].value == self.player:
                count += 1
            else: break
            i += 1
            j -= 1
        if count >= 4: return 1
        else: return 0

    def __str__(self):
        st=""
        for i in range(0,self.row):
            for j in range(0,self.col):
                st+=str(self.arrMatrix[i][j])+" "
            st+="\n"
        return st

    def log(self, cas):
        st = "Player "
        if self.player == 1:
            st += "X is win"
        else:
            st += "O is win"
        cas.create_text(100, 10, fill="black", font="Times 15", text=st)