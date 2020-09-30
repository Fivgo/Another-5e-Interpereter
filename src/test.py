

"""
def foo():
    print("Hello world!")

switch = {
    0 : "hello",
    1 : "world",
    2 : foo
}

sto = switch[2]
sto()
"""

sto = [0,1,2,3,4]
print(sto.pop(2))


#for i in range(len([1,2,3,4])-1, -1, -2):
#    print(i)


"""
from tkinter import *

def create_win():
    def close(): win1.destroy();win2.destroy()
    win1 = Toplevel()
    win1.geometry('%dx%d%+d+%d'%(sw,sh,-sw,0))
    Button(win1,text="Exit1",command=close).pack()
    win2 = Toplevel()
    win2.geometry('%dx%d%+d+%d'%(sw,sh,sw,0))
    Button(win2,text="Exit2",command=close).pack()

root=Tk()
sw,sh = root.winfo_screenwidth(),root.winfo_screenheight()
print("screen1:",sw,sh)
w,h = 800,600
a,b = (sw-w)/2,(sh-h)/2

Button(root,text="Exit",command=lambda r=root:r.destroy()).pack()
Button(root,text="Create win2",command=create_win).pack()

root.geometry('%sx%s'%(w,h))
root.mainloop()
"""


"""
from numba import jit, cuda
import numpy as np
# to measure exec time
from timeit import default_timer as timer


# normal function to run on cpu
def func(a):
    for i in range(10000000):
        a[i] += 1

    # function optimized to run on gpu


@jit(target="cuda")
def func2(a):
    for i in range(10000000):
        a[i] += 1


if __name__ == "__main__":
    n = 10000000
    a = np.ones(n, dtype=np.float64)
    b = np.ones(n, dtype=np.float32)

    start = timer()
    func(a)
    print("without GPU:", timer() - start)

    start = timer()
    func2(a)
    print("with GPU:", timer() - start)
"""