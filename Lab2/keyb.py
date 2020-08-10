from tkinter import *
from tkinter.ttk import *

#creates a root window and initialises Tk's capabilities.
window = Tk()

#special Tk class supporting mutable strings
data = StringVar()
data.set("...")

#Label widget that is a child of the root window
label = Label(window, textvariable=data)
label.grid(row=0, column=0)


clear = Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=0, column=2)


keyboard_frame = Frame(window)
keyboard_frame.config(relief=RAISED)


board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

for row in board:
    row_frame = Frame(keyboard_frame)

    for key in row:
        key_frame = Frame(row_frame, height=32, width=32)
        key_frame.pack_propagate(0)
        key_frame.pack()
        key_button = Button(key_frame, text=key, command=lambda x=key: append(x))
        key_button.pack(fill=BOTH, expand=1)
        key_frame.pack(side='left', expand='yes', fill='both', padx=1, pady=1, ipadx=0, ipady=1)
        key_frame.config(relief=SUNKEN)

    row_frame.pack(side='top')



def clear_data(data):
    data.set("")

def append(x):
    data.set(data.get() + x)


keyboard_frame.grid(row=3, column=0, columnspan=2)

s = Style()
s.configure('TButton', font='helvetica 14', foreground='navy')
s.configure('TLabel', font='helvetica 14', foreground='dark green')


#infinite loop that continually awaits user input on the GUI
window.mainloop()

##SEEALSO: http://www.tkdocs.com/tutorial/widgets.html