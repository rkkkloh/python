# entry widget = textbox that accepts a single line of user input
import tkinter as tk
from tkmacosx import Button

def submit():
    print(entry.get())
    entry.config(state=tk.DISABLED)

def passkey():
    print(entry.get())
    print(password.get())
    entry.config(state=tk.DISABLED)
    password.config(state=tk.DISABLED)

def delete():
    entry.delete(0,tk.END)

def backspace():
    entry.delete(len(entry.get())-1,tk.END)

window = tk.Tk()

entry = tk.Entry(window,
                 font=('Arial',40,'bold'),
                 fg='lightgreen',
                 bg='black')
#entry.insert(0,"Spongebob") # set default input string 
entry.pack(side=tk.LEFT)

password = tk.Entry(window,
                 font=('Arial',40,'bold'),
                 fg='lightgreen',
                 bg='black',
                 show='*')
#password.config(state=DiSABLED)
password.pack(side=tk.LEFT)

submit_button = Button(window,
                text='submit',
                command=passkey)
submit_button.pack(side=tk.RIGHT)

delete_button = Button(window,
                text='delete',
                command=delete)
delete_button.pack(side=tk.RIGHT)

backspace_button = Button(window,
                text='backspace',
                command=backspace)
backspace_button.pack(side=tk.RIGHT)


window.mainloop()