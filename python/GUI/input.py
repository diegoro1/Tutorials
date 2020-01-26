from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")

def rand_click():
    my_label = Label(root, text=e.get().upper())
    my_label.pack()

my_button = Button(root, width=25, height=2,text="Create", command=rand_click)
my_button.pack()

root.mainloop()