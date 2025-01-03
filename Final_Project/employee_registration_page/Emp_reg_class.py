import tkinter as tk
from tkinter import *
from tkinter import ttk
import gui_design as gui


class EmpRegPage:
    def __init__(self, window):
        self.window = window
        self.g = gui.GuiDesign(window)



    def header(self):
        self.g.frames(0, 0, 700, 850, 'white')
        self.g.title_design(40, 15, 'SE-RI\'s Employee Personal Information', 25)

    def emp_pers_info(self):
        self.g.frames(15, 135 - 50, 670, 140, 'grey')
        image_loc = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\employee_registration_page\prof2_logo.png'
        self.g.image_design(image_loc, 57, 80 - 15, 100, 98)
        self.g.button_design(50, 240 - 50- 15, 'Choose File', 'light grey', 'black', 'black', 1, 10, 2)
        self.g.label_design_bg(140, 245 - 50- 15, 'No file chosen', 'grey', 10, 'black')
    # First Name
        self.g.label_design_bg(240, 160 - 50- 15, 'First Name:', 'grey', 10, 'black')
        self.g.textbox_design3(240, 180 - 50- 15, 15, 1, 'black', 10)
    # Middle Name
        self.g.label_design_bg(350, 160 - 50- 15, 'Middle Name:', 'grey', 10, 'black')
        self.g.textbox_design3(350, 180 - 50- 15, 15, 1, 'black', 10)
    # Last Name
        self.g.label_design_bg(460, 160 - 50- 15, 'Last Name:', 'grey', 10, 'black')
        self.g.textbox_design3(460, 180 - 50- 15, 15, 1,'black', 10)
    # Suffix
        self.g.label_design_bg(570, 160 - 50- 15, 'Suffix:', 'grey', 10, 'black')
        self.g.textbox_design3(570, 180 - 50- 15, 15, 1, 'black', 10)
    # Date of Birth
        self.g.label_design_bg(240, 210 - 50- 15, 'Date of Birth:', 'grey', 10, 'black')
        textbox = Text(self.window, width=12, height=1, fg='black', bg='white', font=('Calibre', 11))
        textbox.place(x=240, y=230 - 50- 15)
        textbox.insert(1.0, 'mm/dd/yyyy')
        self.g.button_design(260, 260 - 50- 15, 'Choose Date', 'light grey', 'black', 'black', 1, 10, 1)
    # Gender
        self.g.label_design_bg(350, 210 - 50- 15, 'Gender', 'grey', 10, 'black')
        n = tk.StringVar()
        combo_field = ttk.Combobox(self.window, width=12, textvariable=n)
        combo_field['values'] = (' Female', ' Male ', ' Unidentified')
        combo_field.place(x=350, y=230 - 50- 15)
        combo_field.current()
    # Nationality
        self.g.label_design_bg(460, 210 - 50- 15, 'Nationality:', 'grey', 10, 'black')
        combo_field = ttk.Combobox(self.window, width=12)
        combo_field['values'] = (' Filipino', ' American ', ' Japanese', ' Chinese', ' Korean')
        combo_field.place(x=460, y=230 - 50- 15)
        combo_field.current()
    # Civil Status
        self.g.label_design_bg(570, 210 - 50- 15, 'Civil Status:', 'grey', 10, 'black')
        combo_field = ttk.Combobox(self.window, width=12)
        combo_field['values'] = (' Single', ' Married ', ' Widowed', ' Separated', ' Divorced')
        combo_field.place(x=570, y=230 - 50 - 15)
        combo_field.current()

    def company_info(self):
        #self.gui.frame1(15, 150)
        self.g.frames(15, 300 - 65, 670, 140, 'grey')
    # Department
        self.g.label_design_bg(25, 310- 65, 'Department:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 330 - 65, 50, 1, 'black', 10)
    # Designation
        self.g.label_design_bg(340, 310 - 65, 'Designation:', 'grey', 10, 'black')
        self.g.textbox_design3(340, 330 - 65, 25, 1, 'black', 10)
    # Qualified Dept. Status
        n = tk.StringVar()
        self.g.label_design_bg(505, 310 - 65, 'Qualified Department Status:', 'grey', 9, 'black')
        combo_field = ttk.Combobox(self.window, width=25, textvariable=n)
        combo_field['values'] = (' Yes', ' No ')
        combo_field.place(x=505, y=330 - 65)
    # Employee Status
        self.g.label_design_bg(25, 360 - 65, 'Employee Status:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 380 - 65, 65 , 1, 'black', 10)
    # Paydate
        self.g.label_design_bg(430, 360 - 65, 'Paydate:', 'grey', 10, 'black')
        textbox = Text(self.window, width=10, height=1, fg='black', bg='white', font=('Calibre', 11))
        textbox.place(x=430, y=380 - 65)
        textbox.insert(1.0, 'mm/dd/yyyy')
        self.g.button_design(430, 410 - 65, 'Choose Date', 'light grey', 'black', 'black', 1, 10, 1)
    # Employee Number
        self.g.label_design_bg(525, 360 - 65, 'Employee Number:', 'grey', 10, 'black')
        self.g.textbox_design3(525, 380 - 65, 24, 1, 'black', 10)

    def contact_info(self):
        self.g.title_design(15, 450 - 65 - 10, 'Contact Information', 12)
        self.g.frames(15, 480 - 65 - 15, 670, 130, 'grey')
    # Contact Number
        self.g.label_design_bg(25, 490 - 65 - 15, 'Contact Number:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 510 - 65 - 15, 52, 1, 'black', 10)
    # Email Address
        self.g.label_design_bg(360, 490 - 65 - 15, 'Email Address:', 'grey', 10, 'black')
        self.g.textbox_design3(360, 510 - 65 - 15, 52, 1, 'black', 10)
    # Other Social Media Account
        n = tk.StringVar()
        self.g.label_design_bg(25, 540 - 65 - 15, 'Other Social Media Account:', 'grey', 10, 'black')
        combo_field = ttk.Combobox(self.window, width=49, textvariable=n)
        combo_field['values'] = (' Facebook', ' Twitter ', ' Instagram', ' LinkedIn', ' Tiktok')
        combo_field.place(x=25, y=570 - 65 - 15)
    # Social Media Account ID\No.
        self.g.label_design_bg(360, 540 - 65 - 15, 'Social Media Account ID/No.:', 'grey', 10, 'black')
        self.g.textbox_design3(360, 570 - 65 - 15, 52, 1, 'black', 10)

    def adress(self):
        self.g.title_design(15, 620 - 65 - 25, 'Address', 12)
        self.g.frames(15, 650 - 65 - 30, 670, 240, 'grey')
    # Address Line 1
        self.g.label_design_bg(25, 660 - 65 - 30, 'Address Line 1:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 680 - 65 - 30, 107, 1, 'black', 10)
    # Address Line 2
        self.g.label_design_bg(25, 610, 'Address Line 2:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 630, 100, 1, 'black', 10)
    # City or Municipality
        self.g.label_design_bg(25, 655, 'City or Municipality:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 675, 50, 1, 'black', 10)
    # State\Province
        self.g.label_design_bg(360, 655, 'State\\Province:', 'grey', 10, 'black')
        self.g.textbox_design3(360, 675, 50, 1, 'black', 10)
    # Country
        self.g.label_design_bg(25, 700, 'Country:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 720, 50, 1, 'black', 10)
    # Zip Code
        self.g.label_design_bg(360, 700, 'Zip Code:', 'grey', 10, 'black')
        self.g.textbox_design3(360, 720, 20, 1, 'black', 10)
    # Picture Path of Uploaded Image
        self.g.label_design_bg(25, 745, 'Picture Path of Uploaded Image:', 'grey', 10, 'black')
        self.g.textbox_design3(25, 765, 50, 1, 'black', 10)

    def save_cancel_button(self):
        self.g.button_design(25, 800, 'Save', 'light grey', 'black', 'black', 1, 10, 2)
        self.g.button_design(120, 800, 'Cancel', 'light grey', 'black', 'black', 1, 10, 2)
