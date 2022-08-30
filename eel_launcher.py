# -*- coding: UTF-8 -*-
__author__ = "Jhong,Dong-You"
"""
Ref: Proladon
Ref: https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa0xTRDVTRXIzZ1dYOGtzSW1ONXAyRE52WGRoQXxBQ3Jtc0trYUJjVloxeC00Mk9mU3ZkZElyVmxPR21wcEFTNTUxRDFkVWw2Y2FHendtWXZaQk1uM2lSQjBkdGl3Qi1ES0lwZk13bkJVc1JlWnl0MWRDSHE3QmtJaE1IV0FLWkJZUTgtNVlVZ1VYQ3hMVEhHMkRnNA&q=https%3A%2F%2Fgist.github.com%2FProladon%2F6b485c43828882f56d8fe7e5f802d590&v=FNPW2ZFksCQ
"""
from tkinter import *
from tkinter import font
import tkinter as tk
from tkinter import colorchooser
import os

win = Tk()
win.minsize(200, 40)
win.maxsize(200, 40)
win.attributes('-topmost', 1)

font = font.Font(size=30)


def tkinter_color_select():
    color_tuple = tk.colorchooser.askcolor()
    print("color=", color_tuple)
    print("type=", type(color_tuple))
    color_hex = str(color_tuple[1])
    print("color hex=", color_hex)
    return color_hex


color = tkinter_color_select()


def start_py():
    os.system("python3 app.py")
    return


btn = Button(win, text='START', command=start_py)
# Note: The change of background color of button does not allow on macOS.
# For macOS, use highlight instead.
# Activebackground: Once clicked, change background color.
# Activeforeground:	Once clicked, change color text.
btn.config(width=100, font=font,
           relief=FLAT, activebackground='green',
           activeforeground=color, bg='blue',
           fg='red')
btn.pack()

win.mainloop()
