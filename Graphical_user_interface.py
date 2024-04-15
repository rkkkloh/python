# GUI
# from tkinter import *
# widgets = GUI elements: buttons,textboxes,labels,images
# windows = serves as a container to hold or contain these widgets

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk() #instatiate an instance of window

window.geometry("500x500")
window.title("First GUI Program")
icon = ImageTk.PhotoImage(Image.open('photo/supermario.png'))
window.iconphoto(True,icon)
window.config(background="black")

window.mainloop() #place window on computer screen, listen for events