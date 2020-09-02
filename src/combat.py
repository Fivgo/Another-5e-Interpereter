#Combat.py
#Main focus of this file is to allow for combat functionality

import time
from tkinter import *

mapCons = 50

class combat_map:
    def __init__(self, x = 0, y = 0):
        self.playersID = []
        self.map = []
        for i in range(y):
            self.map.append([0] * x)
        self.master = Tk()
        self.tes = Canvas(self.master,
                     width= mapCons * x,
                     height= mapCons * y)
        self.tes.pack()
        self.tes.create_line(2, 0, 2, mapCons * y, fill="black")
        self.tes.create_line(0, 2, mapCons * x, 2, fill="black")
        for i in range(x+1):
            self.tes.create_line(i*mapCons, 0, i*mapCons, mapCons*y, fill="black")
        for i in range(y+1):
            self.tes.create_line(0, i * mapCons, mapCons*x, i * mapCons, fill="black")
        mainloop()

    def addChar(self, num):
        self.playersID.append(character_class(num))

    def place_player(self, x = 0, y = 0):
        self.map[0][0] = self.player_ID
        self.playerLoc_X = 0
        self.playerLoc_Y = 0

    def moveNorth(self, ID):
        for i in self.playersID:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_Y -= 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveEast(self, ID):
        for i in self.playersID:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_X += 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveSouth(self, ID):
        for i in self.playersID:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_Y += 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveWest(self, ID):
        for i in self.playersID:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_X -= 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID
                i.printOut()




class character_class:

    def __init__(self, ID = 0):
        self.player_ID = ID
        self.playerLoc_X = 0
        self.playerLoc_Y = 0


    def printOut(self):
        print("This character's ID is: " + str(self.player_ID))
        print("x: " + str(self.playerLoc_X) + " y: " + str(self.playerLoc_Y))






def main():
    width = 7
    height = 13
    playArea = combat_map(width,height)
    playArea.addChar(1)


    while True:
        for x in playArea.map:
            print(x)
        print("---------------")
        val = input("where would you like to go? ")
        if val == "w":
            playArea.moveNorth(1)
        elif val == "d":
            playArea.moveEast(1)
        elif val == "s":
            playArea.moveSouth(1)
        elif val == "a":
            playArea.moveWest(1)
        elif val == "b":
            break

    return 1

def canvas_test():
    can_w = 400
    can_h = 400

    def paint(event):
        python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        tes.create_oval(x1, y1, x2, y2, fill=python_green)

    master = Tk()
    tes = Canvas(master,
                 width = can_w,
                 height = can_h)


    tes.pack(expand = YES, fill = BOTH)
    tes.bind("<B3-Motion>", paint)

    message = Label(master, text="Press and Drag the mouse to draw")
    message.pack(side=LEFT)
    mainloop()


#canvas_test()
main()

