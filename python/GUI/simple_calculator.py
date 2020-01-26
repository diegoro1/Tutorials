# this is as simple as it gets, no runtime was thought about while making this, the goal ws to learn 
# tkinter not make something as funtional

from tkinter import *

root = Tk()
root.title("Simple Calculator")

entry = Entry(root, borderwidth=5, width=30)
entry.grid(row=0, column=0, columnspan=3, padx=0, pady=5)

# a different app without using the modulo to increment numbers
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))

# deletes what is in textbox
def button_delete():
    entry.delete(0, END)

# adds in a horrible way (should use a flag instead)
def button_addition():
    first_number = int(entry.get())
    global f_num
    f_num = first_number
    entry.delete(0,END)

# displays addition
def button_equals():
    second_number = int(entry.get())
    entry.delete(0, END)
    entry.insert(0, second_number + f_num)

# numerical buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# arith buttons
button_add = Button(root, text="+", padx=40, pady=20, command=lambda: button_addition())
button_equal= Button(root, text="=", padx=89, pady=20, command=button_equals)
button_clear= Button(root, text="Clear", padx=76, pady=20, command=lambda: button_delete())

# adding buttons to GUI
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

root.mainloop()