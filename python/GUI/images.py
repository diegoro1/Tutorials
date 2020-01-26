from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images in Pyhton")
root.iconbitmap('/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/icon.icns')

# images
my_image = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/seniors.jpg"))
my_label = Label(image=my_image)
my_label.pack()

# buttons
button_quit = Button(root, text="Exit", command=root.quit)
button_quit.pack()



root.mainloop()