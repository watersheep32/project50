from tkinter import *
from tkinter import font
from tkinter import ttk
from functions import *

transactions = []
total = 0
currency = "£"

def add_entry(window):
    name = Reentry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    name_label = Label(window, text="enter name of transaction:", fg=colours[1], bg=colours[2], font=(fonter, 11))
    amount = Reentry(window, justify= "center", font=(fonter, 9), fg=colours[2], bg=colours[3], relief="sunken")
    amount_label = Label(window, text="enter amount of transaction:\n(- for costs)", fg=colours[1], bg=colours[2], font=(fonter, 11))
    return_label = Label(window, text="submit with the enter key", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
    name_label.grid(column=1, pady=10, columnspan=2)
    name.grid(column=1, columnspan=2)
    amount_label.grid(column=1, pady=10, columnspan=2)
    amount.grid(column=1, columnspan=2)
    return_label.grid(column=1, columnspan=2, pady=10)
    window.unbind('<Control-a>')
    window.bind('<Return>', lambda event: read_text(window, name, amount, tree=tree, name_label=name_label, amount_label=amount_label, return_label=return_label))

def read_text(window, *entries, tree, name_label, amount_label, return_label):
    name = entries[0].get()
    amount = entries[1].get()
    destroy_widgets(name_label, amount_label, return_label, entries[0], entries[1])
    window.bind('<Control-a>', lambda event: add_entry(window))
    if name == "" or amount == "":
        add_entry(window)
        return
    
    transactions.append((name, amount))
    tree.insert('', 'end', values=transactions[-1])
    global total
    total += int(transactions[-1][1])

def destroy_widgets(*widgets):
    for widget in widgets:
        widget.destroy()

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

input_label = Label(window, text="press ctrl+A to add a new transaction", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
input_label.grid(column=1, columnspan=2, pady=10)
window.bind('<Control-a>', lambda event: add_entry(window))
running_total = Label(window, text=f"{currency}{total}", fg=colours[1], bg=colours[2], font=(fonter, 13, "bold"))
running_total.grid(column=0, columnspan=1, sticky="e", row=1)


def main():
    window.mainloop()

if __name__ == "__main__":
    main()