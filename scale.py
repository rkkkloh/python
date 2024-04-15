import tkinter as tk
from PIL import Image,ImageTk
from rembg import remove

def submit():
    print("The temperature is" , scale.get() , "degree C")

window = tk.Tk()
#window.config(background="white")
hotImage = ImageTk.PhotoImage(remove(Image.open("photo/hot.png").resize((50,50))))
hotLabel = tk.Label(image=hotImage)
hotLabel.pack()

scale = tk.Scale(from_=600,
                to=0,
                length=600,
                orient=tk.VERTICAL, #orientation of scale
                font=('Consoles',20),
                tickinterval=10, #adds numeric indicators for value
                #showvalue=False, #hide current value can be a boolean or int value
                resolution = 5, #increment of slider
                troughcolor = '#69EAFF',
                fg = '#FF1C00',
                bg = '#111111'
                )
#scale.set((scale['from']+scale['to'])/2)
scale.set(((scale['from']-scale['to'])/2)+scale['to']) #set current value of slider
scale.pack()

coldImage = ImageTk.PhotoImage(remove(Image.open("photo/cold.png").resize((50,50))))
coldLabel = tk.Label(image=coldImage)
coldLabel.pack()

button = tk.Button(text='submit', command=submit)
button.pack()

window.mainloop()