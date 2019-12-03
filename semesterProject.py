import tkinter
def change_pic(labelname, picture):
    photo1 = ImageTk.PhotoImage(Image.open("model1.png"))
    labelname.configure(image=photo1)
    labelname.photo = photo1

    
    
def model1():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'model_images/model1.png')
                                #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1
    
def model2():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'model_images/model2.png')
                            #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1
    
def model3():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'model_images/model3.png')
                            #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1
    
def model4():
    novi = Toplevel()
    canvas = Canvas(novi, width = 300, height = 200)
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = 'model_images/model4.png')
                            #image not visual
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    #assigned the gif1 to the canvas object
    canvas.gif1 = gif1
    

def calculate():
    forwardMultiplier = .7
    rightTurnMultiplier = .2
    leftTurnMultiplier = .1
    northOut = 0.0
    southOut = 0.0
    eastOut = 0.0
    westOut = 0.0

    if model.get() == 1:
        northOut = float(southIn.get()) * forwardMultiplier
        southOut = float(northIn.get()) * forwardMultiplier
        eastOut = float(southIn.get()) * rightTurnMultiplier
        westOut = float(northIn.get()) * rightTurnMultiplier
    elif model.get() == 2:
        northOut = (float(westIn.get()) * leftTurnMultiplier) + (float(eastIn.get()) * rightTurnMultiplier)
        southOut = (float(eastIn.get()) * leftTurnMultiplier) + (float(westIn.get()) * rightTurnMultiplier)
        eastOut = float(southIn.get()) * rightTurnMultiplier
        westOut = float(northIn.get()) * rightTurnMultiplier
    elif model.get() == 3:
        northOut = float(westIn.get()) * rightTurnMultiplier
        southOut = float(eastIn.get()) * rightTurnMultiplier
        eastOut = (float(southIn.get()) * leftTurnMultiplier) + (float(northIn.get()) * rightTurnMultiplier)
        westOut = (float(northIn.get()) * leftTurnMultiplier) + (float(southIn.get()) * rightTurnMultiplier)
    elif model.get() == 4:
        northOut = float(eastIn.get()) * rightTurnMultiplier
        southOut = float(westIn.get()) * rightTurnMultiplier
        eastOut = float(westIn.get()) * forwardMultiplier
        westOut = float(eastIn.get()) * forwardMultiplier

    northOutDisp.configure(text = str(northOut))
    southOutDisp.configure(text = str(southOut))
    eastOutDisp.configure(text = str(eastOut))
    westOutDisp.configure(text = str(westOut))

from tkinter import *
import tkinter as tk
from tkinter import ttk
root = tkinter.Tk()
root.geometry('1000x800')
DEFAULT = "model_images/model1.png"
MODEL2 = "model_images/model2.png"
MODEL3 = "model_images/model3.png"
MODEL4 = "model_images/model4.png"

model = IntVar()
#photo_filepath = tk.StringVar()

model1 = tkinter.Radiobutton(root, text='Model 1', variable=model, value=1, command=model1).grid(row=0)
model2 = tkinter.Radiobutton(root, text='Model 2', variable=model, value=2, command=model2).grid(row=1)
model3 = tkinter.Radiobutton(root, text='Model 3', variable=model, value=3, command=model3).grid(row=2)
model4 = tkinter.Radiobutton(root, text='Model 4', variable=model, value=4, command=model4).grid(row=3)

tkinter.Label(root, text = 'Inflow from North').grid(row=0, column=1, sticky=E)
tkinter.Label(root, text = 'Inflow from South').grid(row=1, column=1, sticky=E)
tkinter.Label(root, text = 'Inflow from East').grid(row=2, column=1, sticky=E)
tkinter.Label(root, text = 'Inflow from West').grid(row=3, column=1, sticky=E)

northIn = tkinter.Entry(root)
northIn.grid(row=0, column=2)
southIn = tkinter.Entry(root)
southIn.grid(row=1, column=2)
eastIn = tkinter.Entry(root)
eastIn.grid(row=2, column=2)
westIn = tkinter.Entry(root)
westIn.grid(row=3, column=2)

tkinter.Button(root, text = 'Calculate', command = calculate).grid(row=4, column=1, pady=4)

tkinter.Label(root, text='Northbound Output: ').grid(row=5, column=0, sticky=E)
northOutDisp = tkinter.Label(root)
northOutDisp.grid(row=5, column=1)
tkinter.Label(root, text='Southbound Output: ').grid(row=6, column=0, sticky=E)
southOutDisp = tkinter.Label(root)
southOutDisp.grid(row=6, column=1)
tkinter.Label(root, text='Eastbound Output: ').grid(row=7, column=0, sticky=E)
eastOutDisp = tkinter.Label(root)
eastOutDisp.grid(row=7, column=1)
tkinter.Label(root, text='Westbound Output: ').grid(row=8, column=0, sticky=E)
westOutDisp = tkinter.Label(root)
westOutDisp.grid(row=8, column=1)
root.mainloop()
