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


#----------------------------------SATURATE IMAGE FUNCTION------------------------------------------------------#
def changeSaturation(canvas):
    saturationWindow= Toplevel(canvas.data.mainWindow)
    saturationWindow.wm_attributes("-topmost",1)
    saturationWindow.title("Saturation")
    saturationWindow.geometry("225x50+1450+500")
    saturationUp = Button(saturationWindow, command=lambda: changeSaturationUp(canvas), text="+", width=100, background="white")
    saturationDown = Button(saturationWindow, command=lambda: changeSaturationDown(canvas), text="-", width=100, background="white")
    saturationUp.pack()
    saturationDown.pack()
def changeSaturationUp(canvas):
    im = canvas.data.image
    enhancer = ImageEnhance.Color(im)
    copyim = enhancer.enhance(1.2)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())

def changeSaturationDown(canvas):
    im = canvas.data.image
    enhancer = ImageEnhance.Color(im)
    copyim = enhancer.enhance(0.8)
    canvas.data.image = copyim
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)
    canvas.data.undoQueue.append(canvas.data.image.copy())
#----------------------------------SATURATE IMAGE FUNCTION------------------------------------------------------#

#----------------------------------BRIGHTNESS IMAGE FUNCTION------------------------------------------------------#
def changeBrightness(canvas):
    brightnessWindow = Toplevel(canvas.data.mainWindow)
    brightnessWindow.wm_attributes("-topmost",1)
    brightnessWindow.title("Brightness")
    brightnessWindow.geometry("225x50+1450+400")
    brightnessUp = Button(brightnessWindow, command=lambda: changeBrightnessUp(canvas), text="+", width=100, background="white")
    brightnessDown = Button(brightnessWindow, command=lambda: changeBrightnessDown(canvas), text="-", width=100, background="white")
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

#----------------------------------BRIGHTNESS IMAGE FUNCTION------------------------------------------------------#