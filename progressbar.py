import tkinter as tk
from tkinter.ttk import *
import time

def start():
    GB = 50
    download=0
    speed=1
    while download<GB:
        time.sleep(0.05)
        bar['value'] += (speed/GB)*100
        download+=speed
        percent.set(str(int((download/GB)*100)) + "%")
        text.set(str(download)+"/"+str(GB)+" GB completed")
        window.update()

window = tk.Tk()

bar = Progressbar(window,orient=tk.HORIZONTAL,length=300)
bar.pack(pady=10)

percent = tk.StringVar()
text = tk.StringVar()
label = tk.Label(window,textvariable=percent).pack()
taskLabel = tk.Label(window,textvariable=text).pack()

Button(window,text='Download',command=start).pack()

window.mainloop()
