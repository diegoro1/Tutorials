from tkinter import *

root = Tk()
root.title("Frames in TKinter")

my_frame = LabelFrame(root, text="this is my frame", padx=5, pady=5)
my_frame.pack(padx=10, pady=10)

my_button0 = Button(my_frame, text="Nothing will happen.")
my_button1 = Button(my_frame, text="Nothing will happen.")
my_button0.grid(row=0, column=0)
my_button1.grid(row=1, column=1)

root.mainloop()
