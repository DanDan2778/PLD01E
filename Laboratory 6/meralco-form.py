import tkinter as tk
from tkinter import *

import gui_design as gui

window = tk.Tk()
window.title("Meralco Form")
window.geometry('700x900')

lbl = Label(window, bg='white', width=1540, height=900)
lbl.place(x=1, y= 1)

gui = gui.GuiDesign(window)
image = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\profile.jpg'

# Frame and image design
gui.frames(15, 15, 670, 850, 'white')
gui.image_design(image, 40, 70, 200, 200)
gui.title_design(39, 40, 'Employee Basic Info')

# First Name label
gui.label_design(400, 80, 'First Name: ')

# First Name Entry widget in DISABLED state
first_name = Entry(window, width=20, fg='black', bg='white', font=('Arial', 10))
first_name.insert(0, "Juan")  # Default value

first_name.place(x=530, y=80)

window.mainloop()
