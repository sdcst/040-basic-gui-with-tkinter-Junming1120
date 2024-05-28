import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
dogphoto = PhotoImage(file="dog.png")


label3 = tk.Label(window, image=dogphoto)
label1 = tk.Label(window,text="A cuddly little puppy! This is from the same\n creators who brought you Keropi and Kero Kero", bg="#00FFFF")
label2 = tk.Label(window,text="Ponchacco!")

label3.grid(row=1, column=3, rowspan=2, sticky=E)
label2.grid(row=1, column=4, sticky=SW)
label1.grid(row=3, column=1, columnspan=6)


window.mainloop()