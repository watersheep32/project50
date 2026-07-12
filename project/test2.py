from tkinter import *
from functions import *

def add_entry(window):
    label = Label(window, text="enter something")
    entry = Reentry(window)
    label.pack()
    entry.pack()
    entry.focus_set()
    window.bind('<KeyPress-Tab>', lambda e: print(1+1))

window = Tk()
window.geometry("400x400")
window.bind('<Return>', lambda event: add_entry(window))

lavel = Label(window, text="press enter to add an entry")
lavel.pack()

window.mainloop()