# label = an area widget that holds text and/or an image within a window

#from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from rembg import remove

window = tk.Tk()
window.title("Python Label")
photo = ImageTk.PhotoImage(remove(Image.open('photo/supermario.png')))
#window.geometry("300x300")
label = tk.Label(window,
              text = "Hello World",
              font=("Arial",40,"bold"),
              fg='lightgreen',
              bg='black',
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom'
              )
label.pack()
#label.place(x=100,y=100)

window.mainloop()