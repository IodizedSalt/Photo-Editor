from tkinter import *
import os
from PIL import Image
import ctypes
from PIL import ImageTk
from PIL import ImageOps
from tkinter import filedialog
from tkinter import messagebox
# from tkFileDialog import *
# import tkMessageBox
import imghdr
from PIL import ImageDraw
from collections import *


def run():
    # create the root and the canvas
    root = Tk()
    root.title("Image Editor")
    canvasWidth = 800
    canvasHeight = 700
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

    # buttonsInit
    backgroundColour = "white"
    buttonWidth = 14
    buttonHeight = 2
    slider = StringVar()
    slider.set(("0% Opacity"))

    class ToolBar:
        menubar = Menu(root)
        fileButton = Menu(menubar, tearoff=0)

        menubar.add_cascade(label="File", menu=fileButton)
        fileButton.menu = Menu(fileButton, tearoff=0)
        fileButton.add_command(label="New", command=lambda: newImage(canvas))
        fileButton.add_command(label="Save")
        fileButton.add_command(label="Restore")
        fileButton.add_command(label="Undo")
        fileButton.add_command(label="Redo")
        menubar.add_command(label="Help")
        root.config(menu=menubar)


    class ToolKit:
        toolBoxLabel = Label(toolKitFrame, text="Toolbox")
        cropButton = Button(toolKitFrame, text="Crop", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight)
        rotateButton = Button(toolKitFrame, text="Rotate", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight)

        toolBoxLabel.grid(row=2, column=0)
        cropButton.grid(row=3, column=0)
        rotateButton.grid(row=4, column=0)

    class PhotoKit:
        # brightnessButton2 = Button(photoKitFrame, text="Brightness", \
        #                            background=backgroundColour, \
        #                            width=buttonWidth, height=buttonHeight)
        #
        # brightnessButton2.grid(row=2, column=0)

        colourBoxLabel = Label(photoKitFrame, text="Colourbox")
        exposureButton = Button(photoKitFrame, text="Exposure", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight)
        saturationButton = Button(photoKitFrame, text="Saturation", \
                              background=backgroundColour, \
                              width=buttonWidth, height=buttonHeight)

        colourBoxLabel.grid(row=2, column=1)
        exposureButton.grid(row=3, column=1)
        saturationButton.grid(row=4, column=1)


    canvas.data.image = None
    canvas.data.brightnessWindowClose = False
    canvas.data.brightnessLevel = None
    canvas.data.undoQueue = deque([], 10)
    canvas.data.redoQueue = deque([], 10)
    canvas.pack()

    # and launch the app
    root.mainloop()  # This call BLOCKS (so your program waits)

def newImage(canvas):
    imageName = filedialog.askopenfilename()
    filetype = ""
    # make sure it's an image file
    try:
        filetype = imghdr.what(imageName)
    except:
        messagebox.showinfo(title="Image File", \
                              message="Choose an Image File!", parent=canvas.data.mainWindow)
    # restrict filetypes to .jpg, .bmp, etc.
    if filetype in ['jpeg', 'bmp', 'png', 'tiff']:
        canvas.data.imageLocation = imageName
        im = Image.open(imageName)
        canvas.data.image = im
        canvas.data.originalImage = im.copy()
        canvas.data.undoQueue.append(im.copy())
        canvas.data.imageSize = im.size  # Original Image dimensions
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)
    else:
        messagebox.showinfo(title="Image File", \
                              message="Choose an Image File!", parent=canvas.data.mainWindow)
def drawImage(canvas):
    if canvas.data.image != None:
        # make the canvas center and the image center the same
        canvas.create_image(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0,
                            canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0,
                            anchor=NW, image=canvas.data.imageForTk)
        canvas.data.imageTopX = int(round(canvas.data.width / 2.0 - canvas.data.resizedIm.size[0] / 2.0))
        canvas.data.imageTopY = int(round(canvas.data.height / 2.0 - canvas.data.resizedIm.size[1] / 2.0))


def makeImageForTk(canvas):
    im = canvas.data.image
    if canvas.data.image != None:
        # Beacuse after cropping the now 'image' might have diffrent
        # dimensional ratios
        imageWidth = canvas.data.image.size[0]
        imageHeight = canvas.data.image.size[1]
        # To make biggest version of the image fit inside the canvas
        if imageWidth > imageHeight:
            resizedImage = im.resize((canvas.data.width, \
                                      int(round(float(imageHeight) * canvas.data.width / imageWidth))))
            # store the scale so as to use it later
            canvas.data.imageScale = float(imageWidth) / canvas.data.width
        else:
            resizedImage = im.resize((int(round(float(imageWidth) * canvas.data.height / imageHeight)), \
                                      canvas.data.height))
            canvas.data.imageScale = float(imageHeight) / canvas.data.height
        # we may need to refer to ther resized image atttributes again
        canvas.data.resizedIm = resizedImage
        return ImageTk.PhotoImage(resizedImage)


run()