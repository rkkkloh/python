from tkinter import *
from PIL import Image, ImageTk
from rembg import remove
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

background_photo = ImageTk.PhotoImage(Image.open('photo/space.png').resize((500,500)))
background = canvas.create_image(0,0,image=background_photo,anchor=NW)

photo_image = ImageTk.PhotoImage(remove(Image.open('photo/ufo.png').resize((150,100))))
my_image = canvas.create_image(0,0,image=photo_image,anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if(coordinates[0]>=(WIDTH-image_width) or coordinates[0]<0):
        xVelocity = -xVelocity
    if(coordinates[1]>=(HEIGHT-image_height) or coordinates[1]<0):
        yVelocity = -yVelocity
    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()