from tkinter import *
from tkinter.ttk import *

window = Tk()
side_labels = ["bottom1", "bottom2", "top1", "top2", "top3", "left1", "right1"]

for theside in side_labels:
    button = Button(window, text=theside)
    button.pack(side=theside[0:-1])

s = Style()
s.configure('TButton', font='helvetica 14', foreground='purple')

window.mainloop()