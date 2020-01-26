from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")

# index for the list of images
index = 0


# foward and back funtionallity
def foward():
    global index
    global image_label
    global button_foward
    if index <= 3:
        index = index + 1
        image_label.grid_forget()
        image_label = Label(image=image_list[index])
        image_label.grid(row=0, column=0, columnspan=3)
        button_foward = Button(root, text=">>", command=lambda: foward())
        button_foward.grid(row=1, column=2)
    else:
        button_foward = Button()
        button_foward = Button(root, text=">>", state=DISABLED)
        button_foward.grid(row=1, column=2)

    
def backwards():
    global index
    global image_label
    if index > 0:
        index = index - 1
        image_label.grid_forget()
        image_label = Label(image=image_list[index])
        image_label.grid(row=0, column=0, columnspan=3)
    

# setting images to variables
image0 = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/hi.png"))
image1 = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/seniors.jpg"))
image2 = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/shop.jpg"))
image3 = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/walkabout.jpg"))
image4 = ImageTk.PhotoImage(Image.open("/Users/diegorodrigues/Desktop/Tutorials/python/GUI/assets/washing_hands.jpg"))

# creating a list of images
image_list = [image0, image1, image2, image3, image4]


# label to place the image
image_label = Label(image=image0)
image_label.grid(row=0, column=0, columnspan=3)


# buttons
button_back = Button(root, text="<<", command=lambda: backwards())
button_foward = Button(root, text=">>", command=lambda: foward())
button_exit = Button(root, text="Exit", command=root.quit)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_foward.grid(row=1, column=2)


root.mainloop()