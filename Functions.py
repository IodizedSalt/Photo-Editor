from tkinter import ttk, filedialog, messagebox  # Extra components from tkinter (Nicer than the default)
from tkinter import *
import os
from tkinter.filedialog import asksaveasfilename

from PIL import Image, ImageEnhance
import ctypes
from PIL import ImageTk
from PIL import ImageOps
from tkinter import filedialog
from tkinter import messagebox
# from tkFileDialog import *
# import tkMessageBox
import imghdr
from Functions import *
from PIL import ImageDraw
from collections import *

def restoreImage(canvas):
    canvas.data.image = canvas.data.originalImage
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())

def displayHelp():
    messagebox.showinfo("Help", "Made by some stupid Geniuses\n\n\n\n" +
                        "File- Gives some options\n\n\n" +
                        "ToolBox- Physical Alterations\n\n" +
                        "\tCrop- Remove portions from an image\n"
                        "\tRotate- Rotate an image 90°\n\n\n" +
                        "ColourBox- Digital Alterations\n\n" +
                        "\tExposure- Increase Exposure of the image\n"
                        "\tSaturate- Saturate the Image\n" +
                        "\tOpacity- Change how Opaque the image is\n" +
                        "\tFilters- Apply custom, default filters\n"
                        )


def saveImage(canvas):
    if canvas.data.image != None:
        filename = asksaveasfilename(defaultextension=".jpg")
        im = canvas.data.image
        im.save(filename)


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
        origImag = im
        canvas.data.originalImage = im.copy()
        canvas.data.undoQueue.append(im.copy())
        canvas.data.imageSize = im.size  # Original Image dimensions
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        return canvas.data.originalImage
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


def rotate(canvas):
    im = canvas.data.image
    copyim = im.rotate(90, expand=True)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())


def changeBrightness(canvas):
    brightnessWindow = Toplevel(canvas.data.mainWindow)
    brightnessWindow.title("Brightness")
    brightnessUp = Button(brightnessWindow, command=lambda: changeBrightnessUp(canvas), text="+")
    brightnessDown = Button(brightnessWindow, command=lambda: changeBrightnessDown(canvas), text="-")
    brightnessUp.pack()
    brightnessDown.pack()


def changeBrightnessUp(canvas):
    im = canvas.data.image
    enhancer = ImageEnhance.Brightness(im)
    copyim = enhancer.enhance(1.25)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())


def changeBrightnessDown(canvas):
    im = canvas.data.image
    enhancer = ImageEnhance.Brightness(im)
    copyim = enhancer.enhance(0.8)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())


def undo(canvas):
    if len(canvas.data.undoQueue) > 0:
        lastImage = canvas.data.undoQueue.pop()
        canvas.data.redoQueue.appendleft(lastImage)
    if len(canvas.data.undoQueue) > 0:
        canvas.data.image = canvas.data.undoQueue[-1]
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)


def redo(canvas):
    if len(canvas.data.redoQueue) > 0:
        canvas.data.image = canvas.data.redoQueue[0]
    if len(canvas.data.redoQueue) > 0:
        # we remove this version from the Redo Deque beacuase it
        # has become our current image
        lastImage = canvas.data.redoQueue.popleft()
        canvas.data.undoQueue.append(lastImage)
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)

#-------KEY BINDINGS-----------#

def keyPressed(canvas, event):
    if event.keysym=="Escape":
        sys.exit()
