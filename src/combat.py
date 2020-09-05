#Combat.py
#Main focus of this file is to allow for combat functionality

import time
from tkinter import *
import math

mapCons = 50
spacing = mapCons//10+1

class combat_map:
    colorDict = {
        0 : "snow",
        1 : "black",
        2 : "blue",
        3 : "red",
        4 : "yellow"
    }

    def build_map(self, x, y):
        self.master = Tk()
        self.tes = Canvas(self.master,
                          width=mapCons * x,
                          height=mapCons * y)
        self.tes.pack()

        self.objects.append(self.tes.create_line(2, 0, 2, mapCons * y, fill=self.colorDict[1]))
        for i in range(x + 1):
            self.objects.append(self.tes.create_line(i * mapCons, 0, i * mapCons, mapCons * y, fill=self.colorDict[1]))
        self.objects.append(self.tes.create_line(0, 2, mapCons * x, 2, fill=self.colorDict[1]))
        for i in range(y + 1):
            self.objects.append(self.tes.create_line(0, i * mapCons, mapCons * x, i * mapCons, fill=self.colorDict[1]))

    def select(self, event):
        print("X: " + str(event.x) + " Y: " + str(event.y))
        gridPos = [event.x//mapCons, event.y//mapCons]
        print("X: " + str(gridPos[1]) + " Y: " + str(gridPos[0]))
        if self.map[gridPos[1]][gridPos[0]] > 0:
            print("yes")


    def addChar(self, num):
        print("character added")
        self.players.append(character_class(num, len(self.objects)))
        self.objects.append(self.tes.create_rectangle(spacing, spacing, mapCons - spacing, mapCons - spacing, fill=self.colorDict[2]))
        self.map[0][0] = num

    def place_player(self, ID, x = 0, y = 0):
        self.playerLoc_X = x
        self.playerLoc_Y = y
        self.map[y][x] = ID

    #def update(self):




    def printOut(self,event):
        print(self.players)
        for x in self.map:
            print(x)
        print("---------------")

    def __init__(self, x = 0, y = 0):
        self.players = []
        self.map = []
        self.objects = []
        for i in range(y):
            self.map.append([0] * x)
        self.build_map(x, y)
        self.tes.bind("<ButtonRelease-1>", self.select)
        self.tes.bind("<Button-3>", self.printOut)
        #mainloop()

"""
    def moveNorth(self, ID):
        for i in self.players:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_Y -= 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveEast(self, ID):
        for i in self.players:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_X += 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveSouth(self, ID):
        for i in self.players:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_Y += 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID

    def moveWest(self, ID):
        for i in self.players:
            if i.player_ID == ID:
                self.map[i.playerLoc_Y][i.playerLoc_X] = 0
                i.playerLoc_X -= 1
                self.map[i.playerLoc_Y][i.playerLoc_X] = ID
                i.printOut()
"""





class character_class:

    def __init__(self, ID = 0, ind = 0):
        self.player_ID = ID
        self.obInd = ind
        self.playerLoc_X = 0
        self.playerLoc_Y = 0


    def printOut(self):
        print("This character's ID is: " + str(self.player_ID))
        print("This Ob ind is: " + str(self.obInd))
        print("x: " + str(self.playerLoc_X) + " y: " + str(self.playerLoc_Y))






def main():
    width = 7
    height = 13
    playArea = combat_map(width, height)

    playArea.addChar(2)

    while True:
        playArea.master.update_idletasks()
        playArea.master.update()
        #val = input("where would you like to go? ")
        #if val == "w":
        #    playArea.moveNorth(1)
        #elif val == "d":
        #    playArea.moveEast(1)
        #elif val == "s":
        #    playArea.moveSouth(1)
        #elif val == "a":
        #    playArea.moveWest(1)

        #if val == "b":
        #    break

    return 1

def canvas_test():
    can_w = 400
    can_h = 400

    def paint(event):
        python_green = "#476042"
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        tes.create_oval(x1, y1, x2, y2, fill=python_green)


    #def scroll_bar(event):


    master = Tk()
    tes = Canvas(master,
                 width = can_w,
                 height = can_h)


    tes.pack(expand = YES, fill = BOTH)
    tes.bind("<B1-Motion>", paint)

    message = Label(master, text="Press and Drag the mouse to draw")
    message.pack(side=LEFT)
    while True:
        master.update_idletasks()
        master.update()
    #mainloop()


#canvas_test()
main()
#Timing tests:
#this area isn't supposed to be in the end result and more to
#focus on the timing of certain fuctions

def timing():
    start = time.time()

    for _ in range(10000000):
        math.tan(.33)

    end = time.time()
    print(end - start)