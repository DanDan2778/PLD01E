import tkinter as tk
from tkinter import *
from tkinter import ttk

from scipy.special.cython_special import fdtridfd

import gui_design as gui

window = tk.Tk()
window.title("Meralco Application Form")
window.geometry('700x900')
# Background
bg = Label(window, bg='white', width=1540, height=900)
bg.place(x=-1, y= -1)

class MeralcoApplicationForm:
    def __init__(self):
        self.window = window
        self.gui = gui.GuiDesign(window)
        self.screen_width = 1540
        self.screen_height = 960
        self.combo_field = ''
        self.header_color = '#0CA4B5'
        self.logo1_path = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\meralco_logo.png'
        self.logo2_path = r'C:\Users\danie\Desktop\repository\PLD01E\Laboratory 6\meralco_logo_2.png'

    def header(self):
        self.gui.frames(-1, -1, self.screen_width, 80, self.header_color)
        self.gui.label_design_center('', 5, self.header_color)
        self.gui.label_design_center('Meralco Application Form', 30, self.header_color)
        self.gui.image_design2(self.logo1_path, 610, 5, 70, 70, self.header_color)
        self.gui.image_design2(self.logo2_path, 15, 58, 164, 20, self.header_color)

    def customer_details(self):
        x_label_textbox = 30
        self.gui.title_design(15, 90, 'Customer Details', 11)
        #self.gui.label_design4(15, 90, 'Customer Details', 11, 'bold', 'black', 'white')
        self.gui.label_textbox(x_label_textbox, 120, 'First Name: ', 150, 15)
        self.gui.label_textbox(x_label_textbox, 150, 'Last Name', 150, 15)
        self.gui.label_textbox(350, 120, 'Middle Name: ', 150, 15)
        self.gui.label_textbox(x_label_textbox, 180, 'Date of Birth: ', 150, 15)
        self.gui.label_design3(x_label_textbox, 195, '(mm\\dd\\yyyy)', 10, 'black')
        self.gui.label_textbox(350, 180, 'Primary Number: ', 150, 15)
        self.gui.label_textbox(350, 215, 'Phone Number: ', 150, 15)
        self.gui.label_textbox(x_label_textbox, 215, 'Email Address: ', 150, 15)
    # Preffered Notification Channel
        self.gui.label_design_bg(x_label_textbox, 245, 'Preffered Notification Channel*', 'white', 10, 'black')
        n = tk.StringVar()
        self.combo_field = ttk.Combobox(self.window, width = 15, textvariable= n)
        self.combo_field['values'] = (' Both', ' SMS', ' Email')
        self.combo_field.place(x=x_label_textbox + 20, y=275)
        self.combo_field.current()
    def service_address(self):
        x = 30
        self.gui.title_design(15, 305, 'Service Address', 12)
        self.gui.label_textbox(x, 335, 'Province:', 75, 20)
        self.gui.label_textbox(x + 150 + 75, 335, 'City/Municipality', 120, 15)
        self.gui.label_textbox(500, 335, 'Barangay', 75, 15)
        self.gui.label_design3(x, 365, 'Landmark', 10, 'black')
        self.gui.textbox_design3(x, 395, 106, 5, 'black', 10)
        self.gui.button_design(500, 500, 'Submit Application', 'green', 'black', 'black', 1, 20, 2)
# Service Address
"""Province city/municipality Barangay
house/bldg. no., Street, subdivision
landmark+"""








form = MeralcoApplicationForm()
form.header()
form.customer_details()
form.service_address()
window.mainloop()