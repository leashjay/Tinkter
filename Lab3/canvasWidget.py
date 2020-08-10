from tkinter import *
from tkinter.ttk import *

master = Tk()
c = Canvas(master, width=200, height=200)
c.pack()

lineA = c.create_line(0, 0, 200, 200, tag='cool')
lineB = c.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
getRect = c.create_rectangle(50, 25, 150, 75, fill="blue")

c.itemconfigure('cool', fill='purple')
c.itemconfigure(getRect, fill='red')
c.coords(getRect, 100,100,200,200)

def action(loc):
    print("get Wrect")

c.tag_bind(getRect, "<ButtonPress-1>", action)




master.mainloop()