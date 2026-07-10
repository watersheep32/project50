from tkinter import *
from tkinter import font
from tkinter import ttk
import project

def add_entry(window):
    name = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    cost = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    amount = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    name.grid(column=1, sticky="e", pady=20)
    submitter = Button(window, text="submit", font=(fonter, 9), fg=colours[1], bg=colours[2], command=lambda: submit_entry(window, tree, submitter, ))
    submitter.grid(column=2, sticky="e", padx=20)

def submit_entry(window, entry, tree, submitter):
    entry_value = entry.get()
    entry.destroy()
    submitter.destroy()
    tree.insert('', 'end', values=(entry_value, "expense", 0))

colours = ["#646669", "#d1d0c5", "#323437", "#e2b714"]
fonter = "Roboto Mono"

window = Tk()
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
back= colours[2]
window.geometry(f"{int(width*4/5)}x{int(height*4/5)}")
window.config(bg=back)
window.columnconfigure((0, 1, 2, 3), weight=1)

w = window.winfo_reqwidth()
h = window.winfo_reqheight()
print(w, h)

stile = ttk.Style()
stile.theme_use('clam')
stile.configure('Treeview.Heading', background=colours[3], foreground=colours[2], font=(fonter, 12))
stile.configure('Treeview', background=colours[0], foreground=colours[1], font=(fonter, 12), fieldbackground=colours[0])
tree = ttk.Treeview(window, columns=('name', 'expense or earning', 'amount'), show='headings')
tree.heading("name", text="name")
tree.heading("expense or earning", text="expense or earning")
tree.heading("amount", text="amount")

tree.column("#0", width=0, minwidth=0)
tree.column("name", anchor=CENTER, width=int(width/6))
tree.column("expense or earning", anchor=CENTER, width=int(width/6))
tree.column("amount", anchor=CENTER, width=int(width/6))

tree.grid(column=1, columnspan=2, pady=25)

addButton = Button(window, text="add table entry", font=(fonter, 13), fg=colours[1], bg=colours[2], command=lambda: add_entry(window)) #add the function later on
addButton.grid(column=1, sticky="e")

window.title("h")

window.mainloop()
