#Combat.py
#Main focus of this file is to allow for combat functionality

import time
from tkinter import *
import math

mapCons = 50
spacing = mapCons//10+2



class combat_map:
    colorDict = {
        0 : "snow",
        1 : "black",
        2 : "blue",
        3 : "red",
        4 : "yellow",
        5 : "gray"
    }

    def draw_map(self, x, y):
        self.master = Tk()
        self.canvas = Canvas(self.master,
                             width=mapCons * x,
                             height=mapCons * y)
        self.canvas.pack()

        """
        draws lines onto canvas and stores them into the objects list for referencing
        """
        self.objects.append(self.canvas.create_line(2, 0, 2, mapCons * y, fill=self.colorDict[1]))
        for i in range(x + 1):
            self.objects.append(self.canvas.create_line(i * mapCons, 0, i * mapCons, mapCons * y, fill=self.colorDict[1]))
        self.objects.append(self.canvas.create_line(0, 2, mapCons * x, 2, fill=self.colorDict[1]))
        for i in range(y + 1):
            self.objects.append(self.canvas.create_line(0, i * mapCons, mapCons * x, i * mapCons, fill=self.colorDict[1]))

    def select(self, event):
        print("X: " + str(event.x) + " Y: " + str(event.y))
        gridPos = [event.x//mapCons, event.y//mapCons]
        print("X: " + str(gridPos[1]) + " Y: " + str(gridPos[0]))

        square = self.map[gridPos[1]][gridPos[0]]

        if self.sel != 0 and square.type == 0:
            # move class

            square.loc = [self.sel.loc[0], self.sel.loc[1]]
            self.map[self.sel.loc[1]][self.sel.loc[0]] = square

            # move object representation
            print("GP: " + str(gridPos[0]) + " loc: " + str(self.sel.loc[0]))

            self.canvas.move(self.objects[self.sel.obInd],
                             (gridPos[0] - self.sel.loc[0]) * mapCons,
                             (gridPos[1] - self.sel.loc[1]) * mapCons)

            # update class
            self.sel.loc = gridPos
            self.map[gridPos[1]][gridPos[0]] = self.sel
            self.sel = 0
            print("moved")
        elif square.type != 0:
            self.sel = self.map[gridPos[1]][gridPos[0]]
            print("selected")
        else:
            print(square.type)


    def addChar(self):

        """
        This function adds an empty character
        """
        self.map[0][0] = character_class(len(self.objects), 0, 0)
        self.objects.append(self.canvas.create_rectangle(spacing, spacing, mapCons - spacing, mapCons - spacing, fill=self.colorDict[2]))
        print("character added")

    #def update(self):




    def printOut(self,event):
        for x in self.map:
            for y in x:
                print(y.type, end=" ")
            print("")
        print("---------------")

    def __init__(self, x=5, y=5):
        self.sel = 0
        self.map = []
        self.objects = []
        for i in range(y):
            temp = []
            for j in range(x):
                temp.append(object(j, i))
            self.map.append(temp)
        self.draw_map(x, y)
        self.canvas.bind("<ButtonRelease-1>", self.select)
        self.canvas.bind("<Button-3>", self.printOut)
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


class object:
    def __init__(self, x, y, t=0):
        self.type = t
        self.loc = [x, y]

class character_class(object):

    def __init__(self,ind, x, y, t=1):
        self.obInd = ind
        super().__init__(x, y, t)
        self.printOut()


    def printOut(self):
        #print("This character's ID is: " + str(self.player_ID))
        print("This Ob ind is: " + str(self.obInd))
        print("x: " + str(self.loc[0]) + " y: " + str(self.loc[1]))






def main():
    width = 7
    height = 13
    playArea = combat_map(width, height)

    playArea.addChar()
    start = time.time()
    fps = 0
    while True:
        #for i in range(10):
        playArea.master.update_idletasks()
        playArea.master.update()
        fps += 1
    """
        if time.time() - start > 1:
            break
    print("Frames captures: " + str(fps))
    """
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
        canvas.create_oval(x1, y1, x2, y2, fill=python_green)


    #def scroll_bar(event):


    master = Tk()
    canvas = Canvas(master,
                 width = can_w,
                 height = can_h)


    canvas.pack(expand = YES, fill = BOTH)
    canvas.bind("<B1-Motion>", paint)

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