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
    #[0] : out of range flag [1]: select line object OBSO [2]: tripwire [3]: debug pathH
    impObs = [0, 0, 0, 1]
    size = [5, 5]
    sel = 0
    map = []
    objects = []
    wallList = []
    mapCorners = []
    pathLine = []
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

    def clean_path(self):
        for i in self.pathHighlight:
            self.canvas.delete(i)
        del self.pathHighlight[:]
        for i in self.pathHardpoints:
            self.canvas.delete(i)
        del self.pathHardpoints[:]
        for i in self.pathLine:
            self.canvas.delete(i)
        del self.pathLine[:]

    def find_path(self, x1, y1, x2, y2, dist=5, w=.5):
        path = set()
        high = {(x1, y1)}
        self.pathLine.append(self.canvas.create_line(x1 * mapCons + mapConsCen, y1 * mapCons + mapConsCen,
                                                     x2 * mapCons + mapConsCen, y2 * mapCons + mapConsCen,
                                                     width=3, fill=self.colorDict[2]))
        dy = y2 - y1
        dx = x2 - x1
        if dx ** 2 + dy ** 2 > dist ** 2 and dist != 0:
            self.canvas.itemconfig(self.pathLine[0], fill=self.colorDict[3])
        else:
            self.canvas.itemconfig(self.pathLine[0], fill=self.colorDict[2])

        if x1 == x2:
            for i in range(y1, y2+1):
                high.add((x1, i))
            for i in range(y2, y1+1):
                high.add((x1, i))
        elif y1 == y2:
            for i in range(x1, x2+1):
                high.add((i, y1))
            for i in range(x2, x1+1):
                high.add((i, y1))
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

            m = dy/dx
            pivot = math.atan(m)+1.571

            xf = 1
            yf = 1
            if dx < 0:
                xf = -1
            if dy < 0:
                yf = -1

            #This checks if there is enough space to check the full width of the object
            if .5 < abs(m) < 2:
                w *= 1.414
            for i in range(abs(dy)):
                path.add((((.5 + i) * yf) / m + x1, (.5 + i) * yf + y1))
            for i in range(abs(dx)):
                path.add(((.5 + i) * xf + x1, (.5 + i) * xf * m + y1))

            # print("current path: " + str(path))
            for i in path:
                if self.impObs[3]:
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
                high.add((round(i[0] + (math.cos(math.atan(m)) * w) * xf),
                          round(i[1] + (math.sin(math.atan(m)) * w) * xf)))

        self.highlight_path(high)
        self.get_conflicts(high)




    def get_conflicts(self, lis):
        sto = []
        for i in lis:
            if self.map[i[1]][i[0]].type == "X":
                #sto = self.get_corners(self.map[i[1]][i[0]])
                print("Blocked!")
                break


    def get_corners_lite(self):
        for i in self.wallList:
            sto = self.map[i[1]][i[0]]
            if self.map[sto.dimen[1]-1][sto.dimen[0]-1].type == 0:
                self.mapCorners.append((sto.dimen[0]-1, sto.dimen[1]-1))
            if self.map[sto.dimen[1]-1][sto.dimen[2]+1].type == 0:
                self.mapCorners.append((sto.dimen[2] + 1, sto.dimen[1] - 1))
            if self.map[sto.dimen[3]+1][sto.dimen[0]-1].type == 0:
                self.mapCorners.append((sto.dimen[0] - 1, sto.dimen[3] + 1))
            if self.map[sto.dimen[3]+1][sto.dimen[2]+1].type == 0:
                self.mapCorners.append((sto.dimen[2] + 1, sto.dimen[3] + 1))


    def highlight_path(self, lis):
        for i in lis:
            self.pathHighlight.append(self.canvas.create_rectangle(i[0] * mapCons,
                                                                   i[1] * mapCons,
                                                                   i[0] * mapCons + mapCons,
                                                                   i[1] * mapCons + mapCons,
                                                                   fill=self.colorDict[3],
                                                                   stipple=self.colorDict[6]))

    def add_char(self, x, y, t, s):
        """
        This function adds an empty character
        """
        self.map[y][x] = Character(len(self.objects), x, y, t, s)
        self.objects.append(self.canvas.create_rectangle(x*mapCons+spacing, y*mapCons+spacing,
                                                         (x*mapCons)+mapCons-spacing, (y*mapCons)+mapCons-spacing,
                                                         fill=self.colorDict[5]))
        print("character added")

    """
    There are a lot of edge cases for the add_wall function.
    For now we'll assume the user is a competent coder...yeah
    """
    def add_wall(self, x1, y1, x2, y2):
        self.wallList.append((x1, y1))
        sto = len(self.objects)
        for y in range(min(y1, y2), max(y1, y2)+1):
            for x in range(min(x1, x2), max(x1, x2)+1):
                self.map[y][x] = Wall(sto, x, y, min(x1, x2), min(y1,y2), max(x1,x2), max(y1,y2))
        self.objects.append(self.canvas.create_rectangle(x1*mapCons+spacing, y1*mapCons+spacing,
                                                         (x2*mapCons)+mapCons-spacing, (y2*mapCons)+mapCons-spacing,
                                                         fill=self.colorDict[1]))

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

    def motion(self, event):
        #should we worry about the mouse moving?
        if self.sel != 0:
            qx = event.x//mapCons
            qy = event.y//mapCons
            #if so, has it made a relevant movement?
            if (qx != self.selLoc[0] or qy != self.selLoc[1]) and qx < self.size[0] and qy < self.size[1]:
                self.selLoc[0] = qx
                self.selLoc[1] = qy
                self.clean_path()
                self.find_path(self.sel.loc[0], self.sel.loc[1], qx, qy, self.sel.speed)


    def leave(self, event):
        self.impObs[2] = 1

    def printOut(self, event):
        for x in self.map:
            for y in x:
                print(y.type, end=" ")
            print("")
        print("---------------")

    def __init__(self, x=5, y=5):
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
    def __init__(self, ind, x, y, x1, y1, x2, y2):
        self.obInd = ind
        self.dimen = [x1, y1, x2, y2]
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


"""
Wall tests:
    playarea.add_char(1, 4, 1, 6)
    playarea.add_wall(3, 4, 4, 4)
    playarea.add_wall(5, 3, 5, 5)
    playarea.add_wall(4, 6, 4, 6)
"""

def main():
    width = 10
    height = 15
    playarea = CombatMap(width, height)

    playarea.add_wall(3, 4, 4, 4)
    playarea.add_wall(5, 3, 5, 5)
    playarea.add_wall(4, 6, 4, 6)
    playarea.get_corners_lite()
    print(playarea.wallList)
    playarea.highlight_path(playarea.mapCorners)

    playarea.add_char(1, 4, 1, 6)
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

