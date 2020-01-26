from tkinter import *

root = Tk()
root.title("Radio")

# r = IntVar()

modes = [
    ("Cheese","Cheese"),
    ("Avocado","Avocado"),
    ("Ham","Ham"),
    ("Steak","Steak"),
]

pizza = StringVar()
pizza.set("cheese")

for text, mode in modes:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

#Radiobutton(root, text="Option1", variable=r, value=1).pack()
#Radiobutton(root, text="Option2", variable=r, value=2).pack()

# my_label = Label(root, text=r.get())
# my_label.pack()


root.mainloop()