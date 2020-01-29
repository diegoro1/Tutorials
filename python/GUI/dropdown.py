from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Drop-Down")
root.geometry("600x400")

def show():
    Label(root,text=clicked.get()).pack()

clicked = StringVar()
clicked.set(option[0])

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday"
]

drop = OptionMenu(root, clicked, *options)
drop.pack()

Button(root, text="show selected", command=show).pack()

root.mainloop()