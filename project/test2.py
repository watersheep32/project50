from tkinter import *
from functions import *

def add_entry(window):
    label = Label(window, text="enter something")
    entry = Reentry(window)
    label.grid()
    entry.grid()
    window.bind('<Control-a>', lambda e: hide(entry, label))

def hide(entry, label):
    entry.grid_forget()
    label.grid_forget()

window = Tk()
window.geometry("400x400")
window.columnconfigure((0, 1, 2), weight=1)
window.bind('<Return>', lambda event: add_entry(window))

lavel = Label(window, text="press enter to add an entry")
lavel.grid()

window.mainloop()