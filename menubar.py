import tkinter as tk
from PIL import Image , ImageTk
from rembg import remove

def openFile():
    print("File has been opened!")

def saveFile():
    print("File has been saved!")

def cut():
    print("You cut some text!")

def copy():
    print("You copied some text!")

def paste():
    print("You pasted some text!")

window = tk.Tk()

fileImage = ImageTk.PhotoImage(remove(Image.open("photo/file.png").resize((25,25))))
saveImage = ImageTk.PhotoImage(remove(Image.open("photo/save.png").resize((20,20))))
exitImage = ImageTk.PhotoImage(remove(Image.open("photo/exit.png").resize((25,20))))

menubar = tk.Menu(window)
window.config(menu=menubar)

fileMenu = tk.Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile,image=fileImage,compound='left')
fileMenu.add_command(label="Save",command=saveFile,image=saveImage,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit,image=exitImage,compound='left')

editMenu = tk.Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label="Edit",menu=editMenu)
editMenu.add_command(label="Cut",command=cut)
editMenu.add_command(label="Copy",command=copy)
editMenu.add_command(label="Paste",command=paste)


window.mainloop()
