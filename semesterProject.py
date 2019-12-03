import tkinter
<<<<<<< HEAD
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
    
=======
from tkinter import *

>>>>>>> 6019120253bb6f6cd75f6690ec1e858db50dde1b

def calculate():
    forward_multiplier = .7
    right_turn_multiplier = .2
    left_turn_multiplier = .1
    north_out = 0.0
    south_out = 0.0
    east_out = 0.0
    west_out = 0.0

    if model.get() == 1:
        north_out = float(south_in.get()) * forward_multiplier
        south_out = float(north_in.get()) * forward_multiplier
        east_out = float(south_in.get()) * right_turn_multiplier
        west_out = float(north_in.get()) * right_turn_multiplier
    elif model.get() == 2:
        north_out = (float(west_in.get()) * left_turn_multiplier) + (float(east_in.get()) * right_turn_multiplier)
        south_out = (float(east_in.get()) * left_turn_multiplier) + (float(west_in.get()) * right_turn_multiplier)
        east_out = float(south_in.get()) * right_turn_multiplier
        west_out = float(north_in.get()) * right_turn_multiplier
    elif model.get() == 3:
        north_out = float(west_in.get()) * right_turn_multiplier
        south_out = float(east_in.get()) * right_turn_multiplier
        east_out = (float(south_in.get()) * left_turn_multiplier) + (float(north_in.get()) * right_turn_multiplier)
        west_out = (float(north_in.get()) * left_turn_multiplier) + (float(south_in.get()) * right_turn_multiplier)
    elif model.get() == 4:
        north_out = float(east_in.get()) * right_turn_multiplier
        south_out = float(west_in.get()) * right_turn_multiplier
        east_out = float(west_in.get()) * forward_multiplier
        west_out = float(east_in.get()) * forward_multiplier

    north_out_display.configure(text=str(north_out))
    south_out_display.configure(text=str(south_out))
    east_out_display.configure(text=str(east_out))
    west_out_display.configure(text=str(west_out))


<<<<<<< HEAD
from tkinter import *
import tkinter as tk
from tkinter import ttk
=======
>>>>>>> 6019120253bb6f6cd75f6690ec1e858db50dde1b
root = tkinter.Tk()
root.geometry('1000x800')
DEFAULT = "model_images/model1.png"
MODEL2 = "model_images/model2.png"
MODEL3 = "model_images/model3.png"
MODEL4 = "model_images/model4.png"

model = IntVar()
#photo_filepath = tk.StringVar()

<<<<<<< HEAD
model1 = tkinter.Radiobutton(root, text='Model 1', variable=model, value=1, command=model1).grid(row=0)
model2 = tkinter.Radiobutton(root, text='Model 2', variable=model, value=2, command=model2).grid(row=1)
model3 = tkinter.Radiobutton(root, text='Model 3', variable=model, value=3, command=model3).grid(row=2)
model4 = tkinter.Radiobutton(root, text='Model 4', variable=model, value=4, command=model4).grid(row=3)
=======
north_in = tkinter.Entry(root)
south_in = tkinter.Entry(root)
east_in = tkinter.Entry(root)
west_in = tkinter.Entry(root)

north_out_display = tkinter.Label(root)
south_out_display = tkinter.Label(root)
east_out_display = tkinter.Label(root)
west_out_display = tkinter.Label(root)

model = IntVar()
tkinter.Radiobutton(root, text='Model 1', variable=model, value=1).grid(row=0)
tkinter.Radiobutton(root, text='Model 2', variable=model, value=2).grid(row=1)
tkinter.Radiobutton(root, text='Model 3', variable=model, value=3).grid(row=2)
tkinter.Radiobutton(root, text='Model 4', variable=model, value=4).grid(row=3)
>>>>>>> 6019120253bb6f6cd75f6690ec1e858db50dde1b

tkinter.Label(root, text='Inflow from North').grid(row=0, column=1, sticky=E)
tkinter.Label(root, text='Inflow from South').grid(row=1, column=1, sticky=E)
tkinter.Label(root, text='Inflow from East').grid(row=2, column=1, sticky=E)
tkinter.Label(root, text='Inflow from West').grid(row=3, column=1, sticky=E)

north_in.grid(row=0, column=2)
south_in.grid(row=1, column=2)
east_in.grid(row=2, column=2)
west_in.grid(row=3, column=2)

tkinter.Button(root, text='Calculate', command=calculate).grid(row=4, column=1, pady=4)

tkinter.Label(root, text='Northbound Output: ').grid(row=5, column=0, sticky=E)
north_out_display.grid(row=5, column=1)
tkinter.Label(root, text='Southbound Output: ').grid(row=6, column=0, sticky=E)
south_out_display.grid(row=6, column=1)
tkinter.Label(root, text='Eastbound Output: ').grid(row=7, column=0, sticky=E)
east_out_display.grid(row=7, column=1)
tkinter.Label(root, text='Westbound Output: ').grid(row=8, column=0, sticky=E)
<<<<<<< HEAD
westOutDisp = tkinter.Label(root)
westOutDisp.grid(row=8, column=1)
=======
west_out_display.grid(row=8, column=1)

>>>>>>> 6019120253bb6f6cd75f6690ec1e858db50dde1b
root.mainloop()
