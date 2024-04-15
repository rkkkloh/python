#  raddio button = similar to checkbox, but you can only select one froma group
import tkinter as tk
from PIL import Image, ImageTk

def order():
    if x.get() == 0:
        print("You ordered hamburger")
    elif x.get() == 1:
        print("You ordered pizza")
    elif x.get() == 2:
        print("You ordered hotdog")
    else:
        print("huh?")

window = tk.Tk()

food = ["hamburger","pizza","hotdog"]
x = tk.IntVar()
hamburgerImage = ImageTk.PhotoImage(Image.open('photo/hamburger.png'))
pizzaImage = ImageTk.PhotoImage(Image.open('photo/pizza.png'))
hotdogImage = ImageTk.PhotoImage(Image.open('photo/hotdog.png'))
foodImages = [hamburgerImage,pizzaImage,hotdogImage]

for index in range(len(food)):
    radiobutton = tk.Radiobutton(text=food[index], #add text to radiobuttons
                                 variable = x, #groups radiobuttons together if they share the 
                                 value = index, #assigns each radiobuttons a different value 
                                 padx=25, #adds padding on x-axis
                                 font=("Impact", 50),
                                 image=foodImages[index], #adds image to radiobutton
                                 compound='left', #adds image & text (left-side)
                                 indicatoron=0, #eliminate circle indicators
                                 width=600, #sets width of radiobuttons
                                 command=order #set command of radiobutton to function
                                )
    radiobutton.pack(anchor=tk.W)

window.mainloop()