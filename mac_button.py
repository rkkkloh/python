import tkinter as tk
from tkmacosx import Button
from PIL import Image, ImageTk

count = 0

def click():
    global count
    count+=1
    print(count)
    #print("You clicked the button!")

window = tk.Tk()
photo = ImageTk.PhotoImage(Image.open('supermario.png'))
button = Button(window,
                text='click me! ',
                command=click,
                font=('Comic Sans',30),
                fg='lightgreen',
                bg='black',
                activeforeground='lightgreen',
                activebackground='black',
                relief=tk.SUNKEN,
                bd = 10,
                image=photo,
                compound='bottom',
                state=tk.NORMAL,
                )
button.pack()
window.mainloop()