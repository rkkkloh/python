# button = you click it, then it does stuff
import tkinter as tk
from PIL import Image, ImageTk

def count():
    print("You clicked the button!")

window = tk.Tk()
photo = ImageTk.PhotoImage(Image.open('photo/supermario.png'))
button = tk.Button(window,
                   text="Click Me!",
                   command=count,
                   fg='lightgreen',
                   image=photo
                   )
#button.image = photo
button.pack()

window.mainloop()
