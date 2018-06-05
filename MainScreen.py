from tkinter import *
from tkinter import ttk    #Extra components from tkinter (Nicer than the default)
from PIL import Image, ImageTk

root = Tk()  #Initialize tkinter root widget.

root.title("Photo Editor")

ttk.Button(root, text="File").grid(row=0, column=0)
ttk.Button(root, text="Edit").grid(row=0, column=1)
ttk.Button(root, text="Help").grid(row=0, column=2)


image = Image.open("Transparent.jpg")
img = ImageTk.PhotoImage(image)
# root.configure(background="Transparent.jpg")
label = Label(image = img)
label.grid(row=1, column=4)



root.mainloop()