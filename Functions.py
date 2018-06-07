# TODO:
# Make 'File' options
# -New(Place photo)
# -Save
# -Restore
# -Undo
# -Red0

import tkinter as tk
from tkinter import ttk,filedialog,messagebox  # Extra components from tkinter (Nicer than the default)

def newFile():
    filedialog.askopenfile(mode='rb', title='Choose a file')

def saveFile():
    print("Save")
def restoreFile():
    print("Restore")
def undoFile():
    print("Undo")
def redoFile():
    print("Redo")

def displayHelp():
    messagebox.showinfo("Help", "Made by some stupid Geniuses\n\n\n\n" +
                                "File- Gives some options\n\n\n"+
                                "ToolBox- Physical Alterations\n\n"+
                                    "\tCrop- Remove portions from an image\n"
                                    "\tRotate- Rotate an image 90°\n\n\n"+
                                "ColourBox- Digital Alterations\n\n"+
                                    "\tExposure- Increase Exposure of the image\n"
                                    "\tSaturate- Saturate the Image\n" +
                                    "\tOpacity- Change how Opaque the image is\n" +
                                    "\tFilters- Apply custom, default filters\n"
                        )

