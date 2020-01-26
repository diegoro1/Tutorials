from tkinter import *

root = Tk()

def my_click():
    label1 = Label(root, text="Hello Yo!")
    label1.pack()

# creating a disabled button
my_button = Button(root, text="Click Me!", state=DISABLED)
my_button.pack()

# this is a ugly button that will call my_click as the user wishes
my_button1 = Button(root, text="Click Here Instead", padx=50, pady=50, command=my_click, fg="white", bg="#000000")
my_button1.pack()

# loop
root.mainloop()