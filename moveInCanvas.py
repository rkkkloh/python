from tkinter import *
from PIL import Image,ImageTk
from rembg import remove

def move_up(event):
   canvas.move(myimage,0,-15)
def move_down(event):
   canvas.move(myimage,0,15)
def move_left(event):
   canvas.move(myimage,-15,0)
def move_right(event):
   canvas.move(myimage,15,0)

window = Tk()

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

canvas = Canvas(window,width=500,height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(remove(Image.open('photo/racecar.png').resize((70,50))))
myimage = canvas.create_image(0,0,image=photoimage,anchor=NW)

window.mainloop()