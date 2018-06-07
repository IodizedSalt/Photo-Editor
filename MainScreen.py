from tkinter import *
import tkinter as tk
from tkinter import ttk  # Extra components from tkinter (Nicer than the default)
from PIL import Image, ImageTk

root = Tk()  # Initialize tkinter root widget.

root.title("Photo Editor")
root.state('zoomed')  # Makes Fullscreen

#Dividing sections into frames and adding to MainApplication Frame
class Frames:
    ToolBar = Frame(root)
    ToolBox = Frame(root)
    Canvas = Frame(root)
    PhotoBox = Frame(root)

#Formatting Row 1 to distribute space between rows
root.grid_rowconfigure(1, weight=1)

#Formatting all section Frames into the main Frame
Frames.ToolBar.grid(row=0,column=0, sticky=W, columnspan=5)
Frames.ToolBox.grid(row=1,column=0, sticky=E, padx=100)
Frames.Canvas.grid(row=1,column= 1, sticky=N, padx=100)
Frames.PhotoBox.grid(row=1,column=2, sticky=E, padx=100)

#File/Help Toolbar in top left
class ToolBar:
    fileButton = ttk.Button(Frames.ToolBar, text="File")
    helpButton = ttk.Button(Frames.ToolBar, text="Help")

    fileButton.grid(row=0, column=0)
    helpButton.grid(row=0, column=1)

#ToolBox section for physical alterations to images
class ToolBox:
    toolBoxLabel = ttk.Label(Frames.ToolBox, text="Toolbox")
    cropButton = ttk.Button(Frames.ToolBox, text="Crop")
    rotateButton = ttk.Button(Frames.ToolBox, text="Rotate")

    toolBoxLabel.grid(row=2, column=1, pady=10)
    cropButton.grid(row=3, column=1, pady=10)
    rotateButton.grid(row=4, column=1, pady=10)

#Canvas section for the image
class Canvas:
    openImage = Image.open("assets/Transparent.jpg")
    img = ImageTk.PhotoImage(openImage)

    transparentBackground = Label(Frames.Canvas, image=img)
    transparentBackground.grid(row=1, column=2)

    Frames.Canvas.grid_rowconfigure(0, weight=1)
    Frames.Canvas.grid_columnconfigure(1, weight=1)

#PhotoBox opacity slider
slider = tk.StringVar()
slider.set(("0% Opacity"))

#PhotoBox section for digital alterations to images
class PhotoBox:


    colourBoxLabel = ttk.Label(Frames.PhotoBox, text="Colourbox")
    exposureButton = ttk.Button(Frames.PhotoBox, text="Exposure")
    saturationButton = ttk.Button(Frames.PhotoBox, text="Saturation")
    opacityLabel = ttk.Label(Frames.PhotoBox, textvariable=slider)
    opacityScale = ttk.Scale(Frames.PhotoBox, from_=0, to=100,
        command=lambda s:slider.set('%0.0f' % float(s) + "% Opacity"))
    filterBox = ttk.Combobox(Frames.PhotoBox)

    colourBoxLabel.grid(row=2, column=1, pady=10)
    exposureButton.grid(row=3, column=1, pady=10)
    saturationButton.grid(row=4, column=1, pady=10)
    opacityLabel.grid(row=5, column=2)
    opacityScale.grid(row=5, column=1, pady=10)
    filterBox.grid(row=6, column=1, pady=10)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

root.mainloop()
