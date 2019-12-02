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

    northOutDisp.configure(text = str(northOut))
    southOutDisp.configure(text = str(southOut))
    eastOutDisp.configure(text = str(eastOut))
    westOutDisp.configure(text = str(westOut))

from Tkinter import *
root = Tkinter.Tk()

model = IntVar() 
Tkinter.Radiobutton(root, text='Model 1', variable=model, value=1).grid(row=0)
Tkinter.Radiobutton(root, text='Model 2', variable=model, value=2).grid(row=1)
Tkinter.Radiobutton(root, text='Model 3', variable=model, value=3).grid(row=2) 
Tkinter.Radiobutton(root, text='Model 4', variable=model, value=4).grid(row=3)

Tkinter.Label(root, text = 'Inflow from North').grid(row=0, column=1, sticky=E)
Tkinter.Label(root, text = 'Inflow from South').grid(row=1, column=1, sticky=E)
Tkinter.Label(root, text = 'Inflow from East').grid(row=2, column=1, sticky=E)
Tkinter.Label(root, text = 'Inflow from West').grid(row=3, column=1, sticky=E)

northIn = Tkinter.Entry(root)
northIn.grid(row=0, column=2)
southIn = Tkinter.Entry(root)
southIn.grid(row=1, column=2)
eastIn = Tkinter.Entry(root)
eastIn.grid(row=2, column=2)
westIn = Tkinter.Entry(root)
westIn.grid(row=3, column=2)

Tkinter.Button(root, text = 'Calculate', command = calculate).grid(row=4, column=1, pady=4)

Tkinter.Label(root, text='Northbound Output: ').grid(row=5, column=0, sticky=E)
northOutDisp = Tkinter.Label(root)
northOutDisp.grid(row=5, column=1)
Tkinter.Label(root, text='Southbound Output: ').grid(row=6, column=0, sticky=E)
southOutDisp = Tkinter.Label(root)
southOutDisp.grid(row=6, column=1)
Tkinter.Label(root, text='Eastbound Output: ').grid(row=7, column=0, sticky=E)
eastOutDisp = Tkinter.Label(root)
eastOutDisp.grid(row=7, column=1)
Tkinter.Label(root, text='Westbound Output: ').grid(row=8, column=0, sticky=E)
westOutDisp = Tkinter.Label(root)
westOutDisp.grid(row=8, column=1)

root.mainloop()