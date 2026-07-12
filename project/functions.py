import re
from tkinter import *

transactions = []

class Reentry(Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Control-BackSpace>', self.entry_ctrl_bs)
    def entry_ctrl_bs(self, event):
        end_idx = self.index(INSERT)
        start_idx = self.get().rfind(" ", None, end_idx)
        self.selection_range(start_idx, end_idx)

def add(*entries): 
    name = entries[0].get()
    amount = entries[1].get()
    transactions.append((name, amount))

#def delete():
#    d = input("1, delete a named item\n2, delte the last entry\n3, clear the list\n")
#    if d == 1:
#        del entries[input("enter the name of the entry to be deleted:\n")]
#    if d == 2:
#        entries.popitem()
#    if d == 3:
#        entries.clear()

#def edit():
#    h, t, e = input("enter the name of the entry to be edited, the value to the edited, and the new value separated by commas\n1. name\n2. expense or cost\n3. amount\n")
#    if t == 1:
#        entries[e] = entries.pop[h]
#    elif t == 2:
#        entries[h][0] = e
#    elif t == 3:
#        entries[h][1] = e
#    return entries

if __name__ == "__main__":
    print("this is a module, not a script")