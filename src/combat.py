#Combat.py
#Main focus of this file is to allow for combat functionality

import time
from tkinter import *
import math

mapCons = 50
mapConsCen = mapCons//2
spacing = mapCons//10+2


class CombatMap:
    colorDict = {
        0: "snow",
        1: "black",
        2: "gray",
        3: "red",
        4: "yellow",
        5: "blue",
        6: "gray12"
    }
    mathList = [.707, .5]



    selLoc = [0, 0]
    #[0] : out of range flag [1]: select line object [2]: tripwire [3]: debug pathH
    impObs = [0, 0, 0, 1]
    size = [5, 5]
    pathHighlight = []
    pathHardpoints = []


    def draw_map(self, x, y):
        self.size[0] = x
        self.size[1] = y
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
            self.objects.append(self.canvas.create_line(i * mapCons, 0,
                                                        i * mapCons, mapCons * y,
                                                        fill=self.colorDict[1]))
        self.objects.append(self.canvas.create_line(0, 2, mapCons * x, 2, fill=self.colorDict[1]))
        for i in range(y + 1):
            self.objects.append(self.canvas.create_line(0, i * mapCons,
                                                        mapCons * x, i * mapCons,
                                                        fill=self.colorDict[1]))

        self.impObs[1] = len(self.objects)

        self.objects.append(self.canvas.create_line(0, 0, 0, 0, width=3, fill=self.colorDict[2]))

        print("Number of essential objects: " + str(len(self.objects)))

    def select(self, event):
        print("X: " + str(event.x) + " Y: " + str(event.y))
        gridPos = [event.x//mapCons, event.y//mapCons]
        print("X: " + str(gridPos[1]) + " Y: " + str(gridPos[0]))

        square = self.map[gridPos[1]][gridPos[0]]

        if self.sel != 0 and square.type == 0 and self.impObs[0] == 0:
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
            # hide move line again
            self.canvas.coords(self.objects[self.impObs[1]], 0, 0, 0, 0)
            self.clean_path()
            print("moved")
        elif square.type != 0 and square.type != "X":
            self.sel = self.map[gridPos[1]][gridPos[0]]
            print("selected")
        else:
            print(square.type)

    def clean_path(self):
        for i in self.pathHighlight:
            self.canvas.delete(i)
        for i in self.pathHardpoints:
            self.canvas.delete(i)

    def find_path(self, x1, y1, x2, y2, w=.5):
        self.clean_path()

        path = set()
        high = {(x1, y1)}
        if x1 == x2:
            for i in range(y1, y2+1):
                path.add((x1, y1+i))
                self.pathHighlight.append(self.canvas.create_rectangle(x1 * mapCons, i * mapCons,
                                                                       (x1 * mapCons) + mapCons,
                                                                       (i * mapCons) + mapCons,
                                                                       fill=self.colorDict[3],
                                                                       stipple=self.colorDict[6]))
        elif y1 == y2:
            for i in range(x1, x2+1):
                path.add((x1+i, y1))
                self.pathHighlight.append(self.canvas.create_rectangle(i * mapCons, y1 * mapCons,
                                                                       (i * mapCons) + mapCons,
                                                                       (y1 * mapCons) + mapCons,
                                                                       fill=self.colorDict[3],
                                                                       stipple=self.colorDict[6]))
        else:
            """
            #Okay, I'm a bit proud of this next part
            resolution = .5
            dy = y2 - y1
            dx = x2 - x1
            m = dy/dx
            flip = 1
            if x2 < x1:
                flip = -1
            print("slope: " + str(m))
            xtrav = math.sqrt(1+m**2)/(1+m**2)
            ytrav = m*xtrav


            for i in range(0, int(math.sqrt(dx**2+dy**2)/resolution)):
                x1 += xtrav*resolution*flip
                y1 += ytrav*resolution*flip
                if self.impObs[3]:
                    
                    
                    version 1:
                    self.pathHardpoints.append(self.canvas.create_rectangle(x1*mapCons+mapConsCen-2,
                                                                            y1*mapCons+mapConsCen-2,
                                                                            x1*mapCons+2+mapConsCen,
                                                                            y1*mapCons+2+mapConsCen,
                                                                            fill=self.colorDict[4]))

                    pivot = math.atan(m)
                    self.pathHardpoints.append(self.canvas.create_line((x1+(math.cos(pivot+90))*self.mathList[1])*mapCons+mapConsCen,
                                                                       (y1+(math.sin(pivot+90))*self.mathList[1])*mapCons+mapConsCen,
                                                                       (x1+(math.cos(pivot-90))*self.mathList[1])*mapCons+mapConsCen,
                                                                       (y1+(math.sin(pivot-90))*self.mathList[1])*mapCons+mapConsCen, fill=self.colorDict[3]))
                cand = (round(x1), round(y1))
                if path[-1] != cand:
                    path.append(cand)
            """
            #version 2:
            dy = y2 - y1
            dx = x2 - x1
            m = dy/dx

            pivot = math.atan(m)+1.571
            xf = 1
            if dx < 0:
                xf = -1
            yf = 1
            if dy < 0:
                yf = -1
            for i in range(abs(dy)):
                path.add((((.5 + i) * yf) / m + x1, (.5 + i) * yf + y1))
            for i in range(abs(dx)):
                path.add(((.5 + i) * xf + x1, (.5 + i) * xf * m + y1))

            for i in path:
                self.pathHardpoints.append(self.canvas.create_rectangle(i[0] * mapCons + mapConsCen - 2,
                                                                        i[1] * mapCons + mapConsCen - 2,
                                                                        i[0] * mapCons + 2 + mapConsCen,
                                                                        i[1] * mapCons + 2 + mapConsCen,
                                                                        fill=self.colorDict[4]))

                self.pathHardpoints.append(
                    self.canvas.create_line((i[0] - math.cos(pivot)*w) * mapCons + mapConsCen,
                                            (i[1] - math.sin(pivot)*w) * mapCons + mapConsCen,
                                            (i[0] + math.cos(pivot)*w) * mapCons + mapConsCen,
                                            (i[1] + math.sin(pivot)*w) * mapCons + mapConsCen,
                                            fill=self.colorDict[3]))
                high.add((round(i[0] - math.cos(pivot) * w), round(i[1] - math.sin(pivot) * w)))
                high.add((round(i[0] + math.cos(pivot) * w), round(i[1] + math.sin(pivot) * w)))
                high.add((round(i[0] + (math.cos(math.atan(m)) * w)*xf), round(i[1] + (math.sin(math.atan(m)) * w)*xf)))

            for i in high:
                self.pathHighlight.append(self.canvas.create_rectangle(i[0] * mapCons,
                                                                       i[1] * mapCons,
                                                                       i[0] * mapCons + mapCons,
                                                                       i[1] * mapCons + mapCons,
                                                                       fill=self.colorDict[3],
                                                                       stipple=self.colorDict[6]))

        #print("current path: " + str(path))








    #def build_path(self, x1, y1, x2, y2):



    def add_char(self, x, y, t, s):
        """
        This function adds an empty character
        """
        self.map[y][x] = Character(len(self.objects), x, y, t, s)
        self.objects.append(self.canvas.create_rectangle(x*mapCons+spacing, y*mapCons+spacing,
                                                         (x*mapCons)+mapCons-spacing, (y*mapCons)+mapCons-spacing,
                                                         fill=self.colorDict[5]))
        print("character added")

    def add_wall(self, x1, y1, x2, y2):
        sto = len(self.objects)

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                self.map[y][x] = Wall(sto, x, y)
        self.objects.append(self.canvas.create_rectangle(x1*mapCons+spacing, y1*mapCons+spacing,
                                                         (x2*mapCons)+mapCons-spacing, (y2*mapCons)+mapCons-spacing,
                                                         fill=self.colorDict[1]))

    def motion(self, event):
        #should we worry about the mouse moving?
        if self.sel != 0:
            qx = event.x//mapCons
            qy = event.y//mapCons
            #if so, has it made a relevant movement?
            if (qx != self.selLoc[0] or qy != self.selLoc[1]) and qx < self.size[0] and qy < self.size[1]:
                self.selLoc[0] = qx
                self.selLoc[1] = qy
                self.find_path(self.sel.loc[0], self.sel.loc[1], qx, qy)

                if (qx-self.sel.loc[0])**2 + (qy-self.sel.loc[1])**2 > self.sel.speed**2 and self.sel.speed != 0:
                    self.canvas.itemconfig(self.objects[self.impObs[1]], fill=self.colorDict[3])
                    self.impObs[0] = 1
                else:
                    self.canvas.itemconfig(self.objects[self.impObs[1]], fill=self.colorDict[2])
                    self.impObs[0] = 0

                self.canvas.coords(self.objects[self.impObs[1]],
                                   self.sel.loc[0]*mapCons+mapConsCen, self.sel.loc[1]*mapCons+mapConsCen,
                                   qx*mapCons+mapConsCen, qy*mapCons+mapConsCen)

    def leave(self, event):
        self.impObs[2] = 1

    def printOut(self, event):
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
        self.canvas.bind("<Button-2>", self.leave)
        self.canvas.bind("<Button-3>", self.printOut)
        self.canvas.bind("<Motion>", self.motion)


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

class Wall(object):
    def __init__(self, ind, x, y):
        self.obInd = ind
        super().__init__(x, y, "X")


class Character(object):

    def __init__(self, ind, x, y, t=1, s=6):
        self.speed = s
        self.obInd = ind
        super().__init__(x, y, t)
        #self.printOut()


    def printOut(self):
        print("This character's speed is: " + str(self.speed))
        print("This Ob ind is: " + str(self.obInd))
        print("x: " + str(self.loc[0]) + " y: " + str(self.loc[1]))




def main():
    width = 10
    height = 15
    playarea = CombatMap(width, height)

    playarea.add_char(5, 5, 1, 6)
    playarea.add_wall(4, 3, 5, 3)
    print("total objects: " + str(len(playarea.objects)))
    start = time.time()
    fps = 0
    while True:
        playarea.master.update_idletasks()
        playarea.master.update()
        fps += 1
        """
        if time.time() - start > 1:
            start = time.time()
            print("Frames captures: " + str(fps))
            fps = 0
        """
        if playarea.impObs[2] == 1:
            break


    return 1


main()
"""
Timing tests:
this area isn't supposed to be in the end result and more to
focus on the timing of certain fuctions
"""
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

def timing():
    start = time.time()

    for _ in range(10000000):
        math.tan(.33)

    end = time.time()
    print(end - start)

