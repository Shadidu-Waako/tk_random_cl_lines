from tkinter import *
from random import choice


def random_color_code():
    hex_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    color_code = '#'
    for i in range(0, 6):
        color_code = color_code + choice(hex_char)
    return color_code


my_window = Tk()
my_canvas = Canvas(my_window, width=400, height=400, background='white')
my_canvas.grid(row=0, column=0)
my_canvas.create_line(0, 0, 400, 400, fill=random_color_code(), width=10)
my_window.mainloop()
