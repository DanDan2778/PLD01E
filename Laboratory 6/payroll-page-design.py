import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

import gui_design as gui

window = tk.Tk()
window.title("Payroll System")
window.geometry('700x900')
lbl = Label(window, bg='white', width=1540, height=900)
lbl.place(x=1, y= 1)

add_y = 10

gui = gui.GuiDesign(window)
image = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\profile.jpg'
gui.frames(15, 25, 670, 850, 'white')
#profile picture
gui.image_design(image, 40, 70, 200, 200)
gui.title_design(39,45, 'Employee Basic Info', 13)
gui.title_design(200, 10, 'LPU-C CHOICE PAYROLL', 20)

# Windows Right Side
# Basic Information
x_label = 380
x_textbox = 540
# First Name
gui.label_design(x_label, 80, 'First Name: ')
gui.textbox_design_disabled(x_textbox, 70+add_y, '')
# Last Name
gui.label_design(x_label, 110, 'Last Name: ')
gui.textbox_design_disabled(540, 110, '')
# Middle Name
gui.label_design(x_label, 140, 'Middle Name: ')
gui.textbox_design_disabled(540, 140,'')
# City Status
gui.label_design(x_label, 170, 'Civil Status: ')
gui.textbox_design_disabled(540, 170, '')
# Qualified Dependent Status
gui.label_design(x_label, 205, 'Qualified Dependent ')
gui.label_design(x_label, 235, 'Status: ')
gui.textbox_design1(540, 205)
# Paydate
gui.label_design(x_label, 260, 'Paydate: ')
gui.textbox_design1(540, 260)
# Employee Status
gui.label_design(x_label, 290, 'Employee Status: ')
gui.textbox_design_disabled(540, 290, '')
# Designation
gui.label_design(x_label, 320, 'Designation: ')
gui.textbox_design_disabled(540, 320, '')

# Regular Deductions
gui.title_design(350, 370, 'Regular Deductions', 13)
# SSS
gui.label_design(x_label, 410, 'SSS Contribution: ')
gui.textbox_design_disabled(540, 410,' ')
# PhilHealth
gui.label_design(x_label, 440, 'PhilHealth Contribution: ')
gui.textbox_design_disabled(540, 440, '')
# Pag-IBIG
gui.label_design(x_label, 470, 'Pag-IBIG Contribution: ')
gui.textbox_design_disabled(540, 470, '')
# Tax
gui.label_design(x_label, 500, 'Income Tax Contribution: ')
gui.textbox_design_disabled(540, 500, '')

# Other Deductions
gui.title_design(350, 530, 'Other Deductions', 13)
# SSS Loan
gui.label_design(x_label, 560, 'SSS Loan: ')
gui.textbox_design1(540, 560)
# Pag-IBIG Loan
gui.label_design(x_label, 590, 'Pag-IBIG Loan: ')
gui.textbox_design1(540, 590)
# Faculty Savings Deposit
gui.label_design(x_label, 620, 'Faculty Savings Deposit: ')
gui.textbox_design1(540, 620)
# Faculty Savings Loan
gui.label_design(x_label, 650, 'Faculty Savings Loan: ')
gui.textbox_design1(540, 650)
# Salary Loan
gui.label_design(x_label, 680, 'Salary Loan: ')
gui.textbox_design1(540, 680)
# Other Loans
gui.label_design(x_label, 710, 'Other Loans: ')
gui.textbox_design1(540, 710)

# DEDUCTION SUMMARY
gui.title_design(350, 740, 'DEDUCTION SUMMARY', 13)
# Total Deductions
gui.label_design(x_label, 780, 'Total Deductions: ')
gui.textbox_design_disabled(540, 780, '')
# Button for Gross Income, Net Income, Save, Update and New
width = 7
pady = 2
y = 800 + 12
gui.button_design(360, y, 'Gross Income', '#000FFF', 'white', 'blue', 2., 10, pady)
gui.button_design(445, y, 'Net Income', '#000FFF', 'white', 'blue', 2, 9, pady)
gui.button_design(523, y, 'Save', '#5499c7', 'white', 'blue', 2, 4, pady)
gui.button_design(567, y, 'Update', '#5499c7', 'white', 'blue', 2, 6, pady)
gui.button_design(625, y, 'New', '#f4d03f', 'white', 'blue', 1, 4, pady)


# Windows Left Side
x_textbox_left = 180
# Employee Number
gui.label_design(40, 280, 'Employee Number: ')
gui.textbox_design1(x_textbox_left, 280)
# Search Employee with button
gui.label_design(40, 310, 'Search Employee: ')
gui.button_design(x_textbox_left, 307, 'Search', 'red', 'white', 'blue', 2, 10, 2)
# Department
gui.label_design(40, 340, 'Department: ')
gui.textbox_design_disabled(x_textbox_left, 340, '')
# Basic Income
gui.title_design(20, 370, 'Basic Income', 13)
# rate per hour y = 490
gui.label_design(40, 410, 'Rate per Hour: ')
gui.textbox_design1(x_textbox_left, 410)
# no. of hours / cut off
gui.label_design(40, 440, 'No. of Hours / Cut Off: ')
gui.textbox_design1(x_textbox_left, 440)
# income / cut off
gui.label_design(40, 470, 'Income / Cut Off: ')
gui.textbox_design_disabled(x_textbox_left, 470, '')
# Honorarium Income
gui.title_design(20, 500, 'Honorarium Income', 13)
# Rate per hour
gui.label_design(40, 550, 'Rate per Hour: ')
gui.textbox_design1(x_textbox_left, 550)
# No. of hours / cut off
gui.label_design(40, 580, 'No. of Hours / Cut Off: ')
gui.textbox_design1(x_textbox_left, 580)
# Income / Cut Off
gui.label_design(40, 610, 'Income / Cut Off: ')
gui.textbox_design_disabled(x_textbox_left, 610, '')
"""Continue From Here"""
# Other Income
gui.title_design(20, 640, 'Other Income', 13)
# Rate per hour
gui.label_design(40, 680, 'Rate per Hour: ')
gui.textbox_design1(x_textbox_left, 680)
# Income / Cut Off
gui.label_design(40, 710, 'Income / Cut Off: ')
gui.textbox_design_disabled(x_textbox_left, 710, '')
# Summary Income
gui.title_design(20, 740, 'Summary Income', 13)
# Gross Income
gui.label_design(40, 780, 'Gross Income: ')
gui.textbox_design_disabled(x_textbox_left, 780, '')
# Net Income
gui.label_design(40, 810, 'Net Income: ')
gui.textbox_design_disabled(x_textbox_left, 810, '')

mainloop()