from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Files")

def open():
    root.filename = filedialog.askopenfilename(initialdir="/Users/diegorodrigues/Desktop/Tutorials/python/GUI", 
    title="Select a File", filetypes=(("jpg", "*jpg"),("png","*png")))
    Label(root, text=root.filename).pack()
    global my_img
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=my_img).pack()

Button(root, text="Open File", command=open).pack()

root.mainloop()
