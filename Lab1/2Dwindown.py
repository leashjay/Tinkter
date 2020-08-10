from tkinter import *
from tkinter.ttk import *
window = Tk()

window.title("I am really not having enjoy")

# Horizontal (x) Scroll bar
x_scroll = Scrollbar(window, orient=HORIZONTAL)
x_scroll.pack(side=BOTTOM, fill=X)

# Vertical (y) Scroll Bar
y_scroll = Scrollbar(window)
y_scroll.pack(side=RIGHT, fill=Y)

# Text Widget
text = Text(window, wrap=NONE,
            xscrollcommand=x_scroll.set,
            yscrollcommand=y_scroll.set,
            height=10,
            width=24
            )
data = StringVar()
data.set("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tTHIS")
text.insert(1.0, data.get())
text.pack()

# Configure the scrollbars
x_scroll.config(command=text.xview)
y_scroll.config(command=text.yview)

window.mainloop()