#!/usr/bin/python3
# hello_tkinter.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text = 'click Me')
button.pack()
Label(root, text="Hello, Tkinter!").pack()
root.mainloop()
