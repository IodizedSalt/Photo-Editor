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


#----------------------------------ROTATE IMAGE FUNCTION------------------------------------------------------#
def rotateImage(canvas):
    rotateWindow = Toplevel(canvas.data.mainWindow)
    rotateWindow.wm_attributes("-topmost", 1)
    rotateWindow.title("Rotation")
    rotateWindow.geometry("225x50+200+500")
    rotateCounter = Button(rotateWindow, command=lambda: rotate90CounterClockwise(canvas), text="90°↺", width=100,
                          background="white")
    rotateClock = Button(rotateWindow, command=lambda: rotate90Clockwise(canvas), text="90°↻", width=100,
                            background="white")
    rotateCounter.pack()
    rotateClock.pack()

def rotate90Clockwise(canvas):
    im = canvas.data.image
    copyim = im.rotate(-90, expand=True)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())
def rotate90CounterClockwise(canvas):
    im = canvas.data.image
    copyim = im.rotate(90, expand=True)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())
# ----------------------------------ROTATE IMAGE FUNCTION------------------------------------------------------#

#----------------------------------MIRROR IMAGE FUNCTION------------------------------------------------------#

def mirrorImage(canvas):
    mirrorWindow = Toplevel(canvas.data.mainWindow)
    mirrorWindow.wm_attributes("-topmost", 1)
    mirrorWindow.title("Mirror")
    mirrorWindow.geometry("225x50+200+600")
    mirrorX = Button(mirrorWindow, command=lambda: mirrorXAxis(canvas), text="Flip X-Axis",
                          width=100,
                          background="white")
    mirrorY = Button(mirrorWindow, command=lambda: mirrorYAxis(canvas), text="Flip Y-Axis", width=100,
                            background="white")
    mirrorX.pack()
    mirrorY.pack()


def mirrorXAxis(canvas):
    canvas.data.colourPopToHappen=False
    canvas.data.cropPopToHappen=False
    canvas.data.drawOn=False
    if canvas.data.image!=None:
        canvas.data.image=ImageOps.flip(canvas.data.image)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk=makeImageForTk(canvas)
        drawImage(canvas)
def mirrorYAxis(canvas):
    canvas.data.colourPopToHappen=False
    canvas.data.cropPopToHappen=False
    canvas.data.drawOn=False
    if canvas.data.image!=None:
        canvas.data.image=ImageOps.mirror(canvas.data.image)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk=makeImageForTk(canvas)
        drawImage(canvas)
#----------------------------------MIRROR IMAGE FUNCTION------------------------------------------------------#
