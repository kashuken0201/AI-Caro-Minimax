from tkinter import *
from Rectangle import *
from Board import *
from AI_Caro import *

row = 20
col = 20
ai = AI_Caro(row,col)
def click(event):
    if(board.clickXO(cas, event.x, event.y)):
        print("Dang xu ly")
        move=ai.calcNextMove(board.arrMatrix, 3)
        print(move)
        board.drawXO(cas, move[0], move[1])
        print(str(board))

if __name__ == "__main__":
    size = 30
    offset = 50
    tk = Tk()
    tk.title("Game Caro Tam Hề")
    cas = Canvas(tk, height = offset*2 + col*size, width = offset*2 + row*size)
    cas.pack()
    board = Board(row, col, size, offset)
    board.drawBoard(cas)
    cas.bind_all('<Button-1>', click)
    tk.mainloop()
    