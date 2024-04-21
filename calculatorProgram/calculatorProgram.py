import tkinter as tk

def buttonPress(num):
    global equationText
    equationText = equationText + str(num)
    equation.set(equationText)


def evaluate():
    global equationText
    try:
        total = str(eval(equationText))

        equation.set(total)

        equationText = total
    except SyntaxError:
        equation.set("SYNTAX ERROR")

        equationText = ""
    except ZeroDivisionError:
        equation.set("MATH ERROR")

        equationText = ""

def clear():
    global equationText
    equation.set("")
    equationText = ""

def createButton(frame,text,width,height,fontsize,command,row,column,columnspan):

    tk.Button(frame, text=text, width=width, height=height, font=fontsize, command=command).grid(column=column, row=row,columnspan=columnspan)

window = tk.Tk()

window.geometry("500x500")

equationText = ''

equation = tk.StringVar()

tk.Label(window, textvariable=equation, font=('consolas',20), bg="white", width=24, height=2).pack()

frame = tk.Frame(window)
frame.pack()

createButton(frame,1,5,4,35,lambda:buttonPress(1),0,0,1)
createButton(frame,2,5,4,35,lambda:buttonPress(2),0,1,1)
createButton(frame,3,5,4,35,lambda:buttonPress(3),0,2,1)
createButton(frame,4,5,4,35,lambda:buttonPress(4),1,0,1)
createButton(frame,5,5,4,35,lambda:buttonPress(5),1,1,1)
createButton(frame,6,5,4,35,lambda:buttonPress(6),1,2,1)
createButton(frame,7,5,4,35,lambda:buttonPress(7),2,0,1)
createButton(frame,8,5,4,35,lambda:buttonPress(8),2,1,1)
createButton(frame,9,5,4,35,lambda:buttonPress(9),2,2,1)
createButton(frame,0,5,4,35,lambda:buttonPress(0),3,0,1)
createButton(frame,'.',5,4,35,lambda:buttonPress('.'),3,1,1)
createButton(frame,'=',5,4,35,evaluate,3,2,1)
createButton(frame,'+',5,4,35,lambda:buttonPress('+'),0,3,1)
createButton(frame,'-',5,4,35,lambda:buttonPress('-'),1,3,1)
createButton(frame,'*',5,4,35,lambda:buttonPress('*'),2,3,1)
createButton(frame,'/',5,4,35,lambda:buttonPress('/'),3,3,1)
clear = createButton(frame,'clear',5,4,35,clear,4,0,4)

window.mainloop()