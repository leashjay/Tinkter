from tkinter import *
from tkinter.ttk import *

#creates a root window and initialises Tk's capabilities.
window = Tk()

#special Tk class supporting mutable strings
data = StringVar()
data.set("Data to display")

#Label widget that is a child of the root window
label = Label(window, textvariable=data)

#grid for geometry management,
label.grid(row=0, column=0)

#Entry widget that can be used to enter text.
entry = Entry(window, textvariable=data)
entry.grid(row=1, column=0)

clear = Button(window, text="Clear", command=lambda: clear_data(data))
clear.grid(row=2, column=0)

quit = Button(window, text="Quit", command=window.destroy)
quit.grid(row=3, column=0)


def clear_data(data):
    data.set("")

s = Style()
s.configure('TButton', font='helvetica 14', foreground='purple')

#infinite loop that continually awaits user input on the GUI
window.mainloop()

##SEEALSO: http://www.tkdocs.com/tutorial/widgets.html