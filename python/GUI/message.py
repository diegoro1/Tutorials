from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

def popup():
    response = messagebox.askyesnocancel("this is a nice popup", "dont be a cheese.")
    if response == 1:
        Label(root, text="YESSSS").pack()
    elif response == 0:
        Label(root, text="NOOOOOO").pack()
    else:
        Label(root, text="Please dont hit cancel next time.").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()