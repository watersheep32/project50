from tkinter import *
from tkinter import ttk
from functions import *

transactions = []
total = 0
currency = "£"

def add_entry(window):
    name.delete(0, END)
    amount.delete(0, END)
    name_label.grid(column=1, pady=10, columnspan=2)
    name.grid(column=1, columnspan=2)
    amount_label.grid(column=1, pady=10, columnspan=2)
    amount.grid(column=1, columnspan=2)
    return_label.grid(column=1, columnspan=2, pady=10)
    window.unbind('<Control-a>')
    window.bind('<Return>', read_text)
    name.focus_force()

def read_text():
    if amount.get() == "":
        amount.focus_force()
        return
    elif name.get() == "":
        name.focus_force()
        return
    elif amount.get().isdigit() == False:
        amount.focus_force()
        warning.grid(column=2, row=5)
        return
    transactions.append((name.get(), amount.get()))
    tree.insert('', 'end', values=transactions[-1])
    global total
    total += int(amount.get())
    running_total.configure(text=f"{currency}{total}")
    window.bind('<Control-a>', lambda event: add_entry(window))
    hide_widgets(name, amount, name_label, amount_label, return_label, warning)

def pop_tree():
    try:
        hide_widgets(forgor_label)
        a = tree.selection()[0]
        global total
        total -= tree.item(a)['values'][1]
        tree.delete(a)
        running_total.configure(text=f"{currency}{total}")
    except IndexError:
        forgor_label.grid(column=3, row=1, sticky="w")

def edit_tree():
    try:
        edit_forgor_label.grid_forget()
        a = tree.selection()[0]
        b = tree.item(a)['values']
        name.configure(textvariable=b[0])
        amount.configure(textvariable=b[1])
        name_label.grid(column=1, pady=10, columnspan=2)
        name.grid(column=1, columnspan=2)
        amount_label.grid(column=1, pady=10, columnspan=2)
        amount.grid(column=1, columnspan=2)
        return_label.grid(column=1, columnspan=2, pady=10)
        window.bind('<Return>', lambda event: read_tree(b))
    except:
        edit_forgor_label.grid(column=2, row=2, sticky="e")

def read_tree(b):
    if amount.get() == "":
        amount.focus_force()
        return
    elif name.get() == "":
        name.focus_force()
        return
    elif amount.get().isdigit() == False:
        amount.focus_force()
        warning.grid(column=2, row=5)
        return
    global total
    total -= b[1]
    running_total.configure(text=f"{currency}{total}")
    b[0] = name.get()
    b[1] = amount.get()
    print(amount.get())
    total += int(b[1])
    window.unbind('<Return>')
    hide_widgets(name, name_label, amount, amount_label, return_label)

def hide_widgets(*widgets):
    for widget in widgets:
        widget.grid_forget()

colours = ["#646669", "#d1d0c5", "#323437", "#e2b714"]
fonter = "Roboto Mono"

window = Tk()
window.title("this is so tedious")
height = window.winfo_screenheight()
width = window.winfo_screenwidth()
back= colours[2]
window.geometry(f"{int(width*3/5)}x{int(height*3/5)}")
window.config(bg=back)
window.columnconfigure((0, 1, 2, 3), weight=1)

w = window.winfo_reqwidth()
h = window.winfo_reqheight()
print(w, h)

stile = ttk.Style()
stile.theme_use('clam')
stile.configure('Treeview.Heading', background=colours[3], foreground=colours[2], font=(fonter, 12))
stile.configure('Treeview', background=colours[0], foreground=colours[1], font=(fonter, 12), fieldbackground=colours[0])


tree = ttk.Treeview(window, columns=('name', 'amount'), show='headings')
tree.heading("name", text="name")
tree.heading("amount", text="amount")

tree.column("#0", width=0, minwidth=0)
tree.column("name", anchor=CENTER, width=int(width/6))
tree.column("amount", anchor=CENTER, width=int(width/6))

tree.grid(column=1, columnspan=2, pady=25)

tree.insert('', "end", values=("Thrustmaster T300", "250"))

forgor_label = Label(window, text="please select a thing to delete", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
input_label = Label(window, text="press ctrl+A to add a new transaction", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
input_label.grid(column=1, columnspan=2, pady=10)
window.bind('<Control-a>', lambda event: add_entry(window))
running_total = Label(window, text=f"{currency}{total}", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
running_total.grid(column=1, columnspan=2, sticky="w", row=1, padx=10)
name = Reentry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
name_label = Label(window, text="enter name of transaction:", fg=colours[1], bg=colours[2], font=(fonter, 11))
amount = Reentry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
amount_label = Label(window, text="enter amount of transaction:\n(- for costs)", fg=colours[1], bg=colours[2], font=(fonter, 11))
return_label = Label(window, text="submit with the enter key", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
warning = Label(window, text="only numbers please", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
delete_tree = Button(window, text="delete selected item", fg=colours[1], bg=colours[2], font=(fonter, 13), command=pop_tree)
delete_tree.grid(column=2, row=1, padx=100, sticky="e")
edit_tree = Button(window, text="edit selected item", fg=colours[1], bg=colours[2], font=(fonter, 13), command=edit_tree)
edit_tree.grid(column=2, row=2, padx=105, sticky="e")
edit_forgor_label = Label(window, text="please select a thing to edit", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))

def main():
    window.mainloop()

if __name__ == "__main__":
    main()