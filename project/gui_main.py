from tkinter import *
from tkinter import font
from tkinter import ttk
import project

def add_entry(window):
    name = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    cost = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    amount = Entry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    name_label = Label(window, text="")
    name.grid(column=1, pady=10, columnspan=2)
    cost.grid(column=1, pady=10, columnspan=2)
    amount.grid(column=1, pady=10, columnspan=2)
    submitter = Button(window, text="submit", font=(fonter, 9), fg=colours[1], bg=colours[2], command=lambda: submit_entry(window, tree, submitter, name, cost, amount))
    submitter.grid(column=2, padx=20)

def submit_entry(window, tree, submitter, name, cost, amount):
    name_value = name.get()
    name.destroy()
    cost_value = cost.get()
    cost.destroy()
    amount_value = amount.get()
    amount.destroy()
    submitter.destroy()
    tree.insert('', 'end', values=(name_value, cost_value, amount_value))

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

add_button = Button(window, text="add table entry", font=(fonter, 13), fg=colours[1], bg=colours[2], command=lambda: add_entry(window)) #add the function later on
add_button.grid(column=1, columnspan=2)

window.title("h")

window.mainloop()
