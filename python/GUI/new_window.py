from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Main Window")

def open():
    global my_img
    top = Toplevel()
    top.title("Second Window")
    my_img = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/hi.png"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    button_quit = Button(top, text="Quit", command=top.destroy)
    button_quit.pack()


button_window = Button(root, text="Open second window", command=open)
button_window.pack()


root.mainloop()