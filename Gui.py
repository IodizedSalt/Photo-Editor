from tkinter import *
import os
from PIL import Image
import ctypes
from PIL import ImageTk
from PIL import ImageOps
from tkinter import filedialog
from tkinter import messagebox
import imghdr
from Functions import *
from MenuFunctions import *
from ToolBoxFunctions import *
from ColourBoxFunctions import *
from PIL import ImageDraw
from collections import *
import Filters as Filter

# create the root and the canvas
root = Tk()
root.title("Image Editor")
root.state("zoomed")
canvasWidth = 800
canvasHeight = 900
canvas = Canvas(root, width=canvasWidth, height=canvasHeight, \
                background="gray")
toolKitFrame = Frame(root)
photoKitFrame = Frame(root)

toolKitFrame.pack(side=LEFT)
photoKitFrame.pack(side=RIGHT)


# Set up canvas data and call init
class Struct: pass


canvas.data = Struct()
canvas.data.width = canvasWidth
canvas.data.height = canvasHeight
canvas.data.mainWindow = root
canvas.data.undoQueue = deque([], 25)
canvas.data.redoQueue = deque([], 25)

backgroundColour = "white"
buttonWidth = 14
buttonHeight = 2


# slider = StringVar()
# slider.set(("0% Opacity"))


def initMenuBar():
    menubar = Menu(root)
    fileButton = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="File", menu=fileButton)
    fileButton.menu = Menu(fileButton, tearoff=0)
    fileButton.add_command(label="New               Ctrl + n", command=lambda: newImage(canvas))
    fileButton.add_command(label="Save               Ctrl + s", command=lambda: saveImage(canvas))
    fileButton.add_command(label="Restore          Ctrl + r", command=lambda: restoreImage(canvas))
    fileButton.add_command(label="Undo             Ctrl + z", command=lambda: undo(canvas))
    fileButton.add_command(label="Redo              Ctrl + x", command=lambda: redo(canvas))
    menubar.add_command(label="Help", command=lambda: displayHelp())
    root.config(menu=menubar)


def initLeftKit():
    toolBoxLabel = Label(toolKitFrame, text="Toolbox")
    rotateButton90 = Button(toolKitFrame, text="Rotate", background=backgroundColour,
                          width=buttonWidth, height=buttonHeight, command=lambda: rotateImage(canvas))

    mirrorButton = Button(toolKitFrame, text="Mirror", background=backgroundColour,
                          width=buttonWidth, height=buttonHeight, command=lambda: mirrorImage(canvas))

    toolBoxLabel.grid(row=2, column=1, padx=80, pady=10, sticky=NE)
    rotateButton90.grid(row=4, column=1, padx=50, pady=10, sticky=E)
    mirrorButton.grid(row=5, column=1, padx=50, pady=10, sticky=E)


def initRightKit():
    colourBoxLabel = Label(photoKitFrame, text="Colourbox")
    exposureButton = Button(photoKitFrame, text="Exposure", background=backgroundColour, width=buttonWidth,
                            height=buttonHeight, command=lambda: changeBrightness(canvas))
    saturationButton = Button(photoKitFrame, text="Saturation", background=backgroundColour,
                              width=buttonWidth, height=buttonHeight, command=lambda: changeSaturation(canvas))

    filterBox = ttk.Combobox(photoKitFrame, state="readonly")
    applyFilter = Button(photoKitFrame, text="Apply Filter", background=backgroundColour, width=buttonWidth,
                         height=buttonHeight, command=lambda: setPhotoFilter(canvas))
    filterBox.set("Filters")

    list = ["None", "Greyscale", "Sepia", "Inverted", "Posterize"]

    filterBox['values'] = list
    def setPhotoFilter(canvas):
        filter = filterBox.get()

        if filter == "None":
            print(filter)
            pass
        elif filter == "Greyscale" or "Sepia" or "Inverted" or "Posterize":
            print(filter)
            warning = messagebox.askquestion("WARNING", "Applying " + filter + " on top of another filter will make\n "
                                                       "it impossible to restore the original image. Continue?", icon="warning")

        if filter == "None":
            Filter.none(canvas)

        elif filter == "Greyscale":
                if warning == "yes":
                    Filter.greyscale(canvas)
                elif warning == "no":
                    pass

        elif filter == "Sepia":
            if warning == "yes":
                Filter.sepia(canvas)
            elif warning == "no":
                pass

        elif filter == "Inverted":
                if warning == "yes":
                    Filter.invert(canvas)
                elif warning == "no":
                    pass

        elif filter == "Posterize":
                if warning == "yes":
                    Filter.posterize(canvas)
                elif warning == "no":
                    pass

    colourBoxLabel.grid(row=2, column=1, padx=70, pady=10, sticky=NW)
    exposureButton.grid(row=3, column=1, padx=50, pady=10, sticky=W)
    saturationButton.grid(row=4, column=1, padx=50, pady=10, sticky=W)

    filterBox.grid(row=7, column=1, padx=50, pady=10, sticky=W)
    applyFilter.grid(row=8, column=1, padx=50, pady=10, sticky=W)

    canvas.data.image = None
    canvas.data.brightnessWindowClose = False
    canvas.data.brightnessLevel = None
    canvas.data.undoQueue = deque([], 10)
    canvas.data.redoQueue = deque([], 10)
    canvas.pack()

    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits)


def run():
    root.bind("<Key>", lambda event: keyPressed(canvas, event))
    root.bind("<Control-z>", lambda event: undo(canvas))
    root.bind("<Control-x>", lambda event: redo(canvas))
    root.bind("<Control-r>", lambda event: restoreImage(canvas))
    root.bind("<Control-n>", lambda event: newImage(canvas))
    root.bind("<Control-s>", lambda event: saveImage(canvas))

    initMenuBar()
    initLeftKit()
    initRightKit()


run()
