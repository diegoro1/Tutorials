from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Check Boxes")
root.geometry("600x400")

def show():
    Label(root, text=var.get()).pack()


var = IntVar()

c = Checkbutton(root, text="check this box", variable=var)
c.pack()


Button(root, text="show", command=show).pack()


root.mainloop()