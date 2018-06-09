from tkinter import *
import tkinter as tk
from tkinter import ttk,filedialog  # Extra components from tkinter (Nicer than the default)
from PIL import Image, ImageTk
from Functions import *


def none(canvas):
    canvas.data.image = canvas.data.originalImage
    canvas.data.undoQueue.append(canvas.data.image.copy())
    canvas.data.imageForTk = makeImageForTk(canvas)
    drawImage(canvas)


def greyscale(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    #### The existing method to convert to a grayscale image converts the ####
    ####         image mode, so I used my own function to convert         ####
    # value of each channel of a pixel is set to the average of the original
    # values of the channels
    if canvas.data.image != None:
        data = []
        for col in range(canvas.data.image.size[1]):
            for row in range(canvas.data.image.size[0]):
                r, g, b = canvas.data.image.getpixel((row, col))
                avg = int(round((r + g + b) / 3.0))
                R, G, B = avg, avg, avg
                data.append((R, G, B))
        canvas.data.originalImage = canvas.data.image.copy()
        canvas.data.image.putdata(data)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)


def sepia(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    # this method first converts the image to B&W and then adds the
    # same amount of red and green to every pixel
    if canvas.data.image != None:
        sepiaData = []
        for col in range(canvas.data.image.size[1]):
            for row in range(canvas.data.image.size[0]):
                r, g, b = canvas.data.image.getpixel((row, col))
                avg = int(round((r + g + b) / 3.0))
                R, G, B = avg + 100, avg + 50, avg
                sepiaData.append((R, G, B))
        canvas.data.originalImage = canvas.data.image.copy()
        canvas.data.image.putdata(sepiaData)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)


def invert(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    if canvas.data.image != None:
        canvas.data.image = ImageOps.invert(canvas.data.image)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)

def posterize(canvas):
    canvas.data.colourPopToHappen = False
    canvas.data.cropPopToHappen = False
    canvas.data.drawOn = False
    # we basically reduce the range of colurs from 256 to 5 bits
    # and so, assign a single new value to each colour value
    # in each succesive range
    posterData = []
    if canvas.data.image != None:
        for col in range(canvas.data.imageSize[1]):
            for row in range(canvas.data.imageSize[0]):
                r, g, b = canvas.data.image.getpixel((row, col))
                if r in range(32):
                    R = 0
                elif r in range(32, 96):
                    R = 64
                elif r in range(96, 160):
                    R = 128
                elif r in range(160, 224):
                    R = 192
                elif r in range(224, 256):
                    R = 255
                if g in range(32):
                    G = 0
                elif g in range(32, 96):
                    G = 64
                elif g in range(96, 160):
                    G = 128
                elif r in range(160, 224):
                    g = 192
                elif r in range(224, 256):
                    G = 255
                if b in range(32):
                    B = 0
                elif b in range(32, 96):
                    B = 64
                elif b in range(96, 160):
                    B = 128
                elif b in range(160, 224):
                    B = 192
                elif b in range(224, 256):
                    B = 255
                posterData.append((R, G, B))
        canvas.data.originalImage = canvas.data.image.copy()
        canvas.data.image.putdata(posterData)
        canvas.data.undoQueue.append(canvas.data.image.copy())
        canvas.data.imageForTk = makeImageForTk(canvas)
        drawImage(canvas)