import Tkinter

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

    print 'north outflow: ', northOut
    print 'south outflow: ', southOut
    print 'east outflow: ', eastOut
    print 'west outflow: ', westOut

from Tkinter import *
root = Tkinter.Tk()

model = IntVar() 
Tkinter.Radiobutton(root, text='Model 1', variable=model, value=1).grid(row=0)
Tkinter.Radiobutton(root, text='Model 2', variable=model, value=2).grid(row=1)
Tkinter.Radiobutton(root, text='Model 3', variable=model, value=3).grid(row=2) 
Tkinter.Radiobutton(root, text='Model 4', variable=model, value=4).grid(row=3)

Tkinter.Label(root, text = 'Inflow from North').grid(row=4)
Tkinter.Label(root, text = 'Inflow from South').grid(row=5)
Tkinter.Label(root, text = 'Inflow from East').grid(row=6)
Tkinter.Label(root, text = 'Inflow from West').grid(row=7)

northIn = Tkinter.Entry(root)
northIn.grid(row=4, column=1)
southIn = Tkinter.Entry(root)
southIn.grid(row=5, column=1)
eastIn = Tkinter.Entry(root)
eastIn.grid(row=6, column=1)
westIn = Tkinter.Entry(root)
westIn.grid(row=7, column=1)

Tkinter.Button(root, text = 'Calculate', command = calculate).grid(row=8, column=1)

root.mainloop()