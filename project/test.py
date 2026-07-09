from tkinter import *
from tkinter import ttk

win = Tk()
win.title("Advanced Treeview Styling")
win.geometry("600x400")

# Create style object
style = ttk.Style()
style.theme_use('clam')

# Configure multiple heading properties
style.configure('Treeview.Heading',
                background='#2E86C1',    # Blue background
                foreground='white',      # White text
                font=('Helvetica', 11, 'bold'),  # Bold font
                relief='raised',         # Raised border effect
                borderwidth=2)           # Border width

# Create Treeview
tree = ttk.Treeview(win, columns=('Name', 'Age', 'City'), show='headings')

# Set column properties
tree.heading('Name', text='Full Name')
tree.heading('Age', text='Age')
tree.heading('City', text='City')

tree.column('Name', width=150, anchor='w')
tree.column('Age', width=80, anchor='center')
tree.column('City', width=120, anchor='w')

# Add sample data
data = [
    ('Alice Johnson', '28', 'New York'),
    ('Bob Smith', '34', 'London'),
    ('Carol Davis', '25', 'Paris'),
    ('David Wilson', '41', 'Tokyo')
]

for row in data:
    tree.insert('', 'end', values=row)

tree.pack(pady=20, padx=20)

win.mainloop()