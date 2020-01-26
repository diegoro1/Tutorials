from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Slidders")
root.geometry("400x400")

def slide(var):
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=50, to=200, orient=HORIZONTAL, command=slide)
horizontal.pack()
Label(root, text=horizontal.get()).pack()


Button(root, text="click me", command=slide).pack()

root.mainloop()