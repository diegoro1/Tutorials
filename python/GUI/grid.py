from tkinter import *

# assigns root
root = Tk()

my_label1 = Label(root, text="Hello, World!")
my_label2 = Label(root, text="My name is Bob")

# putting in a grid
my_label1.grid(row=0, column=0)
my_label2.grid(row=1, column=0) 

# makes root go in a loop until closed
root.mainloop()