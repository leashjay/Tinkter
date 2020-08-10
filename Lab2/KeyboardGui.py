from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

g_n = 6
g_name = "Alyssa"
g_condition = "dynamic"
g_alphabet = "abcdefghijklmnopqrstuvwxyz"


class KeyboardGui:
    def __init__(self, start_window):

        self.start_window = start_window
        self.targetValue = StringVar()
        self.targetLetters = StringVar()
        self.n = g_n
        self.i = 0

        def set_targets():
            copy_alpha = list(g_alphabet)
            random.shuffle(copy_alpha)
            self.targetLetters = copy_alpha[0:6]

        set_targets()

        def shuffled_board():
            shuffled_keys = list(g_alphabet)
            random.shuffle(shuffled_keys)
            board = [shuffled_keys[0:10], shuffled_keys[10:19], shuffled_keys[19:]]
            return board

        def get_board():
            if g_condition == "qwerty":
                board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
            else:
                board = shuffled_board()
            return board

        def set_target_blocks():
            if self.n >= 0:
                print("BLOCK N = ", self.n)
                blocks = self.targetLetters
                random.shuffle(blocks)
                self.n -= 1
            else:
                self.n == 0
                self.targetValue.set("YOU DONE")
            return blocks

        def set_board():
            self.targetValue.set("Press Y to continue")
            self.targetLetters = set_target_blocks()
            #Label widget that is a child of the root window
            label = Label(self.start_window, textvariable=self.targetValue)
            label.grid(row=0, column=0)

            keyboard_frame = Frame(start_window)
            keyboard_frame.config(relief=RAISED)

            for row in get_board():
                row_frame = Frame(keyboard_frame)

                for key in row:
                    key_frame = Frame(row_frame, height=32, width=32)
                    key_frame.pack_propagate(0)
                    key_frame.pack()
                    key_button = Button(key_frame, text=key, command=lambda x=key: show_next(x))
                    key_button.pack(fill=BOTH, expand=1)
                    key_frame.pack(side='left', expand='yes', fill='both', padx=1, pady=1, ipadx=0, ipady=1)
                    key_frame.config(relief=SUNKEN)

                row_frame.pack(side='top')

            keyboard_frame.grid(row=3, column=0, columnspan=2)

            s = Style()
            s.configure('TButton', font='helvetica 14', foreground='navy')
            s.configure('TLabel', font='helvetica 14', foreground='dark green')

        def clear_data(data):
            data.set("")

        def write_to_file(letter, time):
            with open('logging.csv', 'a', newline='') as myFile:
                writer = csv.writer(myFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([g_name, "Static", letter, time])
            myFile.close

        def show_next(x):
            letter_showing = self.targetLetters[self.i]
            start = time.time()
            if x == "y":
                self.targetValue.set(letter_showing)
            elif x == letter_showing:
                total_time = (time.time() - start) * 1000
                write_to_file(letter_showing, total_time)
                print(total_time)
                self.i += 1
                if g_condition == "dynamic":
                    set_board()
                start = time.time()
                if self.i != len(self.targetLetters):
                    self.targetValue.set(self.targetLetters[self.i])
                else:
                    if self.n == 0:
                        self.targetValue.set("YOU DONE")

                    else:
                        self.i = 0
                        self.targetLetters = set_target_blocks()
                        self.targetValue.set(self.targetLetters[self.i])

        set_board()

        #infinite loop that continually awaits user input on the GUI
        self.start_window.mainloop()


start_window = Tk()
keyboard = KeyboardGui(start_window)
start_window.mainloop()
