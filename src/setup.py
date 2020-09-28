from combat import *
from tkinter import *

class menu:
    colorDict = {
        0: "snow",
        1: "black",
        2: "gray",
        3: "red",
        4: "yellow",
        5: "blue",
        6: "gray12"
    }
    fileName = None
    tripwire = 1
    reso = 3
    dropdown_toggle = False

    def dropdown(self):
        self.dropdown_toggle = not self.dropdown_toggle
        if self.dropdown_toggle:
            self.res1.place(relx=.5, rely=.475, anchor="n")
            self.res2.place(relx=.5, rely=.575, anchor="n")
            self.res3.place(relx=.5, rely=.675, anchor="n")
            self.res4.place(relx=.5, rely=.775, anchor="n")
            self.res5.place(relx=.5, rely=.875, anchor="n")
        else:
            self.res1.place_forget()
            self.res2.place_forget()
            self.res3.place_forget()
            self.res4.place_forget()
            self.res5.place_forget()



    def change_reso_1(self):
        print("changing mode")
        self.reso = 1
        self.selected.config(text="2560x1440")
        self.dropdown()

    def change_reso_2(self):
        print("changing mode")
        self.reso = 2
        self.selected.config(text="1920x1200")
        self.dropdown()

    def change_reso_3(self):
        print("changing mode")
        self.reso = 3
        self.selected.config(text="1920x1080")
        self.dropdown()

    def change_reso_4(self):
        print("changing mode")
        self.reso = 4
        self.selected.config(text="1280x800")
        self.dropdown()

    def change_reso_5(self):
        print("changing mode")
        self.reso = 5
        self.selected.config(text="1280x720")
        self.dropdown()


    def printout(self):
        str = self.file_inp.get()
        if str != "":
            self.fileName = str

        print("Fullscreen:", self.fs_bool.get(), " Filename:", self.fileName, " Reso mode:", self.reso)
        self.quit()

    def quit(self):
        self.tripwire = 0
        self.master.destroy()

    def __init__(self):
        self.master = Tk()
        self.master.title("A5eI Setup")
        self.master.resizable(width=False, height=False)
        self.master.geometry("300x400")
        frame1 = Frame(self.master, width=300, height=400, background="gray30")

        file_text = Label(self.master, width=4, height=1, bg="gray50", text="File", relief="flat")
        self.file_inp = Entry(self.master, width=26)
        fullscreen_text = Label(self.master, width=10, height=1, bg="gray50", text="Fullscreen", relief="flat")
        self.fs_bool = IntVar()
        fullscreen_button = Checkbutton(self.master, variable=self.fs_bool, bg="gray30", relief="flat")
        c = Button(self.master, text="Enter", width=10, height=2, command=self.printout)


        reso_text = Label(self.master, width=8, height=1, bg="gray50", text="Resolution", relief="flat")
        self.selected = Button(self.master, text="1920x1080", width=10, height=2, command=self.dropdown)
        self.res1 = Button(self.master, text="2560x1440", width=10, height=2, command=self.change_reso_1)
        self.res2 = Button(self.master, text="1920x1200", width=10, height=2, command=self.change_reso_2)
        self.res3 = Button(self.master, text="1920x1080", width=10, height=2, command=self.change_reso_3)
        self.res4 = Button(self.master, text="1280x800", width=10, height=2, command=self.change_reso_4)
        self.res5 = Button(self.master, text="1280x720", width=10, height=2, command=self.change_reso_5)


        file_text.place(relx=.1, rely=.125, anchor="nw")
        self.file_inp.place(relx=.25, rely=.125, anchor="nw")
        fullscreen_text.place(relx=.1, rely=.25, anchor="nw")
        fullscreen_button.place(relx=.5, rely=.25, anchor="n")
        c.place(relx=.5, rely=.8, anchor="c")
        reso_text.place(relx=.1, rely=.375, anchor="nw")
        self.selected.place(relx=.5, rely=.375, anchor="n")
        frame1.pack(fill=None, expand=False)






        """
        self.master = Tk()
        self.master.geometry("300x400")
        left = Frame(self.master, width=200, height=100, bg="blue")
        right = Frame(self.master, width=125, height=100, bg="red")
        left2 = Frame(self.master, width=125, height=100, bg="yellow")
        right2 = Frame(self.master, width=125, height=100, bg="green")
        bottom = Frame(self.master, bg="white")

        left.pack(fill=None, expand=False)
        right.pack(fill=None, expand=False)
        left2.pack(fill=None, expand=False)
        right2.pack(fill=None, expand=False)
        #bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


        # create the widgets for the top part of the GUI,
        # and lay them out
        b = Button(self.master, text="Enter", width=10, height=2, command=self.printout)
        c = Button(self.master, text="Clear", width=10, height=2, command=self.quit)
        b2 = Button(self.master, text="Enter", width=10, height=2, command=self.printout)
        c2 = Button(self.master, text="Clear", width=10, height=2, command=self.quit)
        d = Button(self.master, text="Clear", width=10, height=2, command=self.quit)

        b.pack(in_=left, fill=None, expand=False, padx=5, pady=5)
        c.pack(in_=right, padx=5, pady=5)
        b2.pack(in_=left2, padx=5, pady=5)
        c2.pack(in_=right2, padx=5, pady=5)
        d.pack(in_=bottom, side=TOP)
        """

def ma():
    welcome = menu()
    while welcome.tripwire:
        welcome.master.update_idletasks()
        welcome.master.update()
    fn = welcome.fileName
    fs = welcome.fs_bool.get()
    res = welcome.reso
    del welcome
    main_app(fn, fs, res)

ma()