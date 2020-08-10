from tkinter import *
from tkinter.ttk import *
from itertools import product
from random import shuffle

g_distance = [64,128,256,512]
g_widths = [4,8,16,32]
g_canvas = 600



class canvasGUI:
    def __init__(self, master):

        self.start_window = master
        self.margin = 0
        self.index = 0

        self.c = Canvas(self.start_window, width=g_canvas, height=g_canvas, bg='white')
        self.c.pack()

        #helper function not for build
        def prin_var(list):
            for i in list:
                print(i)

        """ build a cartesean list of all variants in distanct:width"""
        def build_options():
            # cartesian itertools.product -> shuffle
            variants = list(product(g_distance, g_widths))
            shuffle(variants)
            return variants

        def calc_margin(tuple):
            distance, width = tuple
            total_span = distance + width
            return (g_canvas - total_span) / 2

        """Sets the left rectange"""
        def set_left(tuple):
            #x1: Left y1= Top, x2=Right, y2= bottom
            distance, width = tuple
            total_span = distance + width
            margin = calc_margin(tuple)
            x1, y1 = margin, 0
            x2, y2 = margin + width, g_canvas
            print("LEFTY")
            print("X1: ", x1, "X2", x2, "\nY1: ", y1, "Y2: ", y2)
            return x1, y1, x2, y2

        """Sets the right rectange"""
        def set_right(tuple):
            #x1: Left y1= Top, x2=Right, y2= bottom
            distance, width = tuple
            total_span = distance + width
            margin = calc_margin(tuple)
            x1, y1 = margin + distance, 0
            x2, y2 = margin + distance + width, g_canvas
            print("RIGHTY")
            print("X1: ", x1, "X2", x2, "\nY1: ", y1, "Y2: ", y2)
            return x1, y1, x2, y2

        variants = build_options() #cereate widths and shuffle

        self.rect_left = self.c.create_rectangle(set_left(variants[self.index]))
        self.c.itemconfigure(self.rect_left, fill='green', tag="b")

        self.rect_right = self.c.create_rectangle(set_right(variants[self.index]))
        self.c.itemconfigure(self.rect_right, fill='blue', tag='g')

        self.c.tag_bind(self.rect_left, "<Button-1>", self.action)
        self.c.tag_bind(self.rect_right, "<Button-1>", self.action)

    def action(self, *args):
        if self.c.itemcget(self.rect_left, "fill") == "green":
            self.c.itemconfigure(self.rect_left, fill='blue')
            self.c.itemconfigure(self.rect_right, fill='green')
            self.rect_left = self.c.create_rectangle(self.set_left(self.variants[self.index]))

        elif self.c.itemcget(self.rect_right, "fill") == "green":
            self.c.itemconfigure(self.rect_left, fill='green')
            self.c.itemconfigure(self.rect_right, fill='blue')
            self.rect_right = self.c.create_rectangle(self.set_right(self.variants[self.index]))

        self.index += 1



master = Tk()
canvas = canvasGUI(master)
master.mainloop()