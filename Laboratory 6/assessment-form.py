import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

import gui_design as gui

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.title('LPU-C Assessment Form')
gui = gui.GuiDesign(window)
lbl = Label(window, bg='white', width=1540, height=900)
lbl.place(x=1, y= 1)

# Header design
gui.frames(0, 0, screen_width, 140, '#AE0404')
image_path = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\LPU-C-LOGO.png'
gui.image_design2(image_path, 325, 10, 115, 115, '#AE0404')
gui.label_design_center('Lyceum of the Philippines University', 30)
gui.label_design_center('First Semester A.Y. 2024-2025', 10)
gui.label_design_center('ENROLLMENT ASSESSMENT FORM', 25)

gui.frames(0, 140, screen_width, 850, 'red')
gui.frames(0, 140, screen_width, 100, '#D51C1C')

# Student Information
gui.label_textbox_bold(15, 160, 'STUDENT NUMBER: ', 150, 30)
gui.label_textbox_bold(15, 200, 'NAME: ', 150, 50)
# course
gui.label_textbox_bold(750, 160, 'COURSE: ', 90, 30)
# college
gui.label_textbox_bold(750, 200, 'COLLEGE: ', 90, 30)

# Class Schedule
gui.label_textbox_bold(15, 255, 'CLASS SCHEDULE', 150, 30)
gui.line(15, 290, 150, 290)



# Student Information
#gui.label_design3(15, 96, 'STUDENT NUMBER: ', 10, 'black')
#gui.textbox_design3(150, 96, 50, 2, 'black', 10)


window.mainloop()