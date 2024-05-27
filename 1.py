import tkinter as tk 
from tkinter import *
from tkinter import ttk 
window = tk.Tk()
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
lable2 = tk.Label(window, text="x")
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
button4 = tk.Button(window,text="=")
entry5 = tk.Entry(window,text="Entry widgets can be typed in", width=20)
entry1.pack(side=LEFT)
lable2.pack(side=LEFT)
entry3.pack(side=LEFT)
button4.pack(side=LEFT)
entry5 .pack(side=LEFT)
window.mainloop()