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
def displayHelp():
    messagebox.showinfo("Help", "Made by some stupid Geniuses\n\n\n\n" +
                        "File- Gives some options\n\n\n" +
                        "ToolBox- Physical Alterations\n\n" +
                        "\tRotate- Rotate an image 90°\n\n\n" +
                        "\tMirror- Flip an image on its axis\n"+
                        "ColourBox- Digital Alterations\n\n" +
                        "\tExposure- Increase Exposure of the image\n"
                        "\tSaturate- Saturate the Image\n" +
                        "\tOpacity- Change how Opaque the image is\n" +
                        "\tFilters- Apply custom, default filters\n"
                        )

def restoreImage(canvas):
    canvas.data.image = canvas.data.originalImage
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
        lastImage = canvas.data.redoQueue.popleft()
        canvas.data.undoQueue.append(lastImage)
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)



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

