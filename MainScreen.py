from tkinter import *
from tkinter import ttk    #Extra components from tkinter (Nicer than the default)
from PIL import Image, ImageTk
root = Tk()  #Initialize tkinter root widget.

root.title("Photo Editor")
root.state('zoomed') #Makes Fullscreen
frame = Frame(root)
# frame.pack()
frame.grid()
frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

class ToolBar:
    ttk.Button(root, text="File").grid(row=0, column=0)
    ttk.Button(root, text="Help").grid(row=0, column=1)
    #-----------------------------------------------------------------------------
class ToolBox:
    ttk.Label(root, text="Toolbox").grid(row=2, column = 1, pady=10)
    ttk.Button(root, text="Crop").grid(row=3, column=1,pady=10)
    ttk.Button(root, text="Rotate").grid(row=4, column=1,pady=10)
    #-----------------------------------------------------------------------------
# class Canvas:
#     openImage = Image.open("assets/Transparent.jpg")
#     img = ImageTk.PhotoImage(openImage)
#     transparentBackground = Label(image = img)
#     transparentBackground.grid(row=1, column=2, padx=400)
    #-----------------------------------------------------------------------------
class PhotoBox:
    ttk.Label(root, text="Colourbox").grid(row=2, column = 3, pady=10)
    ttk.Button(root, text="Exposure").grid(row=3, column=3,pady=10)
    ttk.Button(root, text="Saturation").grid(row=4, column=3,pady=10)
    ttk.Scale(root, from_=0, to=42).grid(row=5, column=3,pady=10)
    ttk.Combobox(root).grid(row=6, column=3,pady=10)






# #MainFrame containters
# class Frames:
#     toolBar = Frame(root).pack(side=TOP, anchor=NW)
#     toolBox = Frame(root).pack(side=LEFT, anchor=W)
#     canvas = Frame(root).pack(side=TOP, anchor=CENTER)
#     photobox = Frame(root).pack(side=RIGHT, anchor=CENTER)
#
#
# root.grid_rowconfigure(1, weight=1)
# root.grid_columnconfigure(0, weight=1)
#
# Frames.toolBar.grid(row=0)
# Frames.toolBox.grid(row=1)
# Frames.canvas.grid(row=3)
# Frames.photobox.grid(row=4)
#
# #Topleft Toolbar
# class ToolBar:
#     # toolBar = Frame(root).pack(side=TOP, anchor=NW)
#     file = ttk.Button(root, text="File").pack(side=LEFT, anchor=NW, expand=1)
#     help = ttk.Button(root, text="Help").pack(side=LEFT, anchor=NW, expand=1)
#     #-----------------------------------------------------------------------------
#
# ToolBar.file.grid(row=0, columnspan=3)
# ToolBar.help.grid(row=1, column=0)
#
# #ToolBox W
# class ToolBox:
#     # toolBox = Frame(root).pack(side=LEFT, anchor=E)
#     ttk.Label(root, text="Toolbox").pack(side=LEFT, anchor=CENTER)
#     ttk.Button(root, text="Crop").pack(side=LEFT, anchor=CENTER)
#     ttk.Button(root, text="Rotate").pack(side=LEFT, anchor=CENTER)
#     #-----------------------------------------------------------------------------
# #Canvas
# class Canvas:
#     # canvas = Frame(root).pack(side=TOP, anchor=CENTER)
#     openImage = Image.open("assets/Transparent.jpg")
#     img = ImageTk.PhotoImage(openImage)
#     transparentBackground = Label(image = img)
#     transparentBackground.pack(side=TOP, anchor=CENTER, expand=1)
#     #-----------------------------------------------------------------------------
# class PhotoBox:
#     # photobox = Frame(root).pack(side=RIGHT, anchor=W)
#     ttk.Label(root, text="Colourbox").pack(side=RIGHT, anchor=W)
#     ttk.Button(root, text="Exposure").pack(side=RIGHT, anchor=W)
#     ttk.Button(root, text="Saturation").pack(side=RIGHT, anchor=W)
#     ttk.Scale(root, from_=0, to=42).pack(side=RIGHT, anchor=W)
#     ttk.Combobox(root).pack(side=RIGHT, anchor=W)



root.mainloop()