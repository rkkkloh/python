import tkinter as tk
from PIL import Image, ImageTk

def display():
    if x.get() == 1:
        print("You have progressed yourself!")
    else:
        print("You have no progress today :(")

window = tk.Tk()

x=tk.IntVar()
photo = ImageTk.PhotoImage(Image.open('photo/supermario.png'))

check_button = tk.Checkbutton(window,
                              text="to-do-list",
                              variable=x,
                              onvalue=1,
                              offvalue=0,
                              command=display,
                              font=('Arial',20),
                              fg='#00FF00',
                              bg='black',
                              padx=25,
                              pady=10,
                              image=photo,
                              compound='left')
check_button.pack()

window.mainloop()