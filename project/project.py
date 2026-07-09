import re

entries = {}

def main():
    while True:
        print(f"enter 1 to add an entry\nenter 2 to delete an entry\nenter 3 to change an entry\n4 to exit the program")
        response = int(input())
        if response == 4:
            print("thank you for using the accountancy program!")
            break
        menu(response)

def menu(response):
    if response == 1:
        entries = add()
    elif response == 2:
        entries = delete()
    elif response == 3:
        entries = edit()


def add():
    entry = input("enter the name of the entry, if it's an expense or an earning and its amount separated by commas:\n").split(", ")
    entry[2] = int(entry[2])
    entries[entry[0]] = [entry[1], entry[2]]
    print(entries)
    return entries

def delete():
    d = input("1, delete a named item\n2, delte the last entry\n3, clear the list\n")
    if d == 1:
        del entries[input("enter the name of the entry to be deleted:\n")]
    if d == 2:
        entries.popitem()
    if d == 3:
        entries.clear()

def edit():
    h, t, e = input("enter the name of the entry to be edited, the value to the edited, and the new value separated by commas\n1. name\n2. expense or cost\n3. amount\n")
    if t == 1:
        entries[e] = entries.pop[h]
    elif t == 2:
        entries[h][0] = e
    elif t == 3:
        entries[h][1] = e
    return entries

if __name__ == "__main__":
    main()
