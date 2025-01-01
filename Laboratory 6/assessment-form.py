import tkinter as tk
from tkinter import *

import gui_design as gui

window = tk.Tk()

# Check for screen width and height


class AssessmentForm:
    def __init__(self):
        self.window = window
        self.screen_width = window.winfo_screenwidth()
        self.screen_height = window.winfo_screenheight()
        self.window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.window.title('LPU-C Assessment Form')
        self.gui = gui.GuiDesign(window)
        self.lbl = Label(window, bg='white', width=1540, height=900)
        self.lbl.place(x=1, y=1)
        self.image_path = ''
        self.frame = ''
        print("Screen Width and Height")
        print(self.screen_width, self.screen_height)
        self.new_window = ''


    def header(self):
# Header design
        bg = '#AE0404'
        self.gui.frames(0, 0, self.screen_width, 140, '#AE0404')
        self.image_path = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\LPU-C-LOGO.png'
        self.gui.image_design2(self.image_path, 325, 10, 115, 115, '#AE0404')
        self.gui.label_design_center('', 2, bg)
        self.gui.label_design_center('Lyceum of the Philippines University', 30, bg)
        self.gui.label_design_center('', 10, bg)
        self.gui.label_design_center('ENROLLMENT ASSESSMENT FORM', 25, bg)

# Student Information
#gui.frames(0, 140, screen_width, 100, '#D40606')
    def student_information(self):

        self.gui.label_textbox_bold(15, 200, 'STUDENT NUMBER: ', 150, 30)
        self.gui.label_textbox_bold(15, 160, 'NAME (LN, FN, MI): ', 150, 30)
        # course
        self.gui.label_textbox_bold(550, 160, 'COURSE: ', 90, 30)
        # college
        self.gui.label_textbox_bold(550, 200, 'COLLEGE: ', 90, 30)
        # year
        self.gui.label_textbox_bold(1000, 160, 'YEAR: ', 90, 15)
        # section
        self.gui.label_textbox_bold(1000, 200, 'SECTION: ', 90, 15)

    def student_subjects(self):

        y = 302
        color = 'white'
        #self.gui.frames(0, 240, 900, 460, color)
        self.frame = tk.Frame(window, bg=color, width=900, height=460)
        self.gui.line(15, 680, 175, 'white')
        self.frame.place(x=0, y=240)
        # Class Schedule
        self.gui.label_design4(15, 255, 'CLASS SCHEDULE', 11, 'bold', 'black', color)
        self.gui.line(15, 275, 175, color)
        # Subject Code
        self.gui.label_design_bg(25, y, 'SUBJECT CODE', color, 11, 'black')
        # Course Description
        self.gui.label_design_bg(178, y, 'COURSE DESCRIPTION', color, 11, 'black')
        # Section
        self.gui.label_design_bg(395, y, 'SECTION', color, 11, 'black')
        # Time
        self.gui.label_design_bg(525, y, 'TIME', color, 11, 'black')
        # days
        self.gui.label_design_bg(640, y, 'DAY', color, 11, 'black')
        # room
        self.gui.label_design_bg(730, y, 'ROOM', color, 11, 'black')
        # units
        self.gui.label_design_bg(830, 300, 'UNITS', color, 11, 'black')
        self.gui.line(15, 320, 175, color)

        # Initial Entries for subject information
        y = 320
        fg = 'black'


        y = y + 30
        # Subject Code
        self.gui.textbox_design3(25, y, 15, 1, fg, 11)
        # Course Description
        self.gui.textbox_design3(150, y, 30, 1, fg, 11)
        # Section
        self.gui.textbox_design3(390, y, 10, 1, fg, 11)
        # Time
        self.gui.textbox_design3(490, y, 15, 1, fg, 11)
        # Days
        self.gui.textbox_design3(625, y, 9, 1, fg, 11)
        # Room
        self.gui.textbox_design3(715, y, 10, 1, fg, 11)
        # Units
        self.gui.textbox_design3(815, y, 10, 1, fg, 11)
# Add More Subject Button
        self.gui.button_design(740, 600, 'Add More Subject', '#18d409', 'black', 'black', 1, 20, 3)
# Total Units
        y = 650
        self.gui.label_textbox_bold_disabled(15, y, 'TOTAL UNITS: ', 100, 10, '')
        self.gui.vertical_line(900, 255, 110, 'black', 'white')

    def miscellaneous_fees(self):
        x = 950
        x_lbl = 950 + 10
        #self.frame = tk.Frame(window, bg = 'red', width = 550, height = 100)
        #self.frame.place(x=x, y=255)
# TUITION AND MISCELLANEOUS FEES
        distance = 270
        self.gui.line(940, 310, 110, 'white')
        self.gui.label_textbox_bold(x_lbl, 260, 'TUITION FEE: ', distance, 20)
        self.gui.label_textbox_bold(x_lbl, 290, 'TOTAL MISCELLANEOUS FEES: ', distance, 20)

# LABORATORY AND OTHER FEES
        self.gui.title_design(x_lbl, 340, 'LABORATORY AND OTHER FEES', 10)
# Other Fees
        x = x_lbl + 10
        distance = distance - 20
        self.gui.title_design(x, 370, 'OTHER FEES', 10)
        self.gui.label_textbox(x + 10, 400, 'EXAM BOOKLET: ', distance, 20)
# Laboratory Fees
        self.gui.title_design(x, 430, 'LABORATORY FEES', 10)
        self.gui.label_textbox(x + 10, 460, 'LMS FEE: ', distance, 20)
        # Other Laboratory Fees
        y = 490
        #self.gui.textbox_design3(x + 10, y, 25, 1, 'black', 11)
        #self.gui.textbox_design3(x + 10 + distance, y, 20, 1, 'black', 11)
    # Add More Laboratory Fee Button
        #self.gui.button_design(x + 165, y + 10, 'Add More Laboratory Fee', 'white', 'black', 'black', 1, 30, 3)
# line
        self.gui.line(940, 525, 110, 'white')
        self.gui.line(940, 575, 110, 'white')
# Total laboratory and other fees
        self.gui.label_textbox_bold_disabled(x_lbl, 555, 'TOTAL LABORATORY AND OTHER FEES: ', 270, 20, '')

# Total Assessment
        self.frame = tk.Frame(window, bg='white', width=550, height=225, bd=2, highlightthickness=1,
                              highlightbackground='black')
        self.frame.place(x=943, y=595)
    def total_fees(self):
        self.gui.line(950, 655, 106, 'white')
        self.gui.line(950, 730, 106, 'white')
        self.gui.double_line(952, 790, 265, 'black', 'white')
        self.gui.title_design(960, 605, 'TOTAL ASSESSMENT: ', 11)
        self.gui.textbox_design4(960 + 270, 605, 20, 1, 'black', 11)
        self.gui.label_textbox(965, 635, 'ADD: INSTALLMENT CHARGE: ', 265, 20)
        self.gui.title_design(960, 685, 'TOTAL AMOUNT DUE: ', 11)
        self.gui.textbox_design4(960 + 270, 685, 20, 1, 'black', 11)
        self.gui.label_textbox(965, 715, 'LESS: PAYMENTS MADE: ', 265, 20)
        self.gui.label_textbox_bold_disabled(965, 760, 'BALANCE(PAYABLE INSTALLMENTS): ', 265, 20, '')



    def payment_schedule(self):
        color = 'white'
        #color = 'red'
        self.frame = tk.Frame(window, bg=color, width=550, height=165, bd = 2, highlightthickness=1, highlightbackground='black')
        self.frame.place(x=115, y=710)
        self.gui.label_design4(260, 720, 'INSTALLMENT PAYMENT SCHEDULE', 11, 'bold', 'black', color)
        self.gui.label_design3(205, 750, 'PAYMENT', 10, 'black')
        self.gui.label_design3(335, 750, 'DUE DATE', 10, 'black')
        self.gui.label_design3(455, 750, 'MINIMUM AMOUNT DUE', 10, 'black')

        self.gui.label_design3(175, 780, '1ST INSTALLMENT', 10, 'black')
        self.gui.label_design3(175, 810, '2ND INSTALLMENT', 10, 'black')
        self.gui.label_design3(175, 840, '3RD INSTALLMENT', 10, 'black')

        for i in range(3):
            y = 780 + i * 30
            self.gui.textbox_design3(310, y, 15, 1, 'black', 11)
            self.gui.textbox_design3(475, y, 15, 1, 'black', 11)

    def laboratory_fees(self):
        def open_new_window():
            self.new_window = tk.Toplevel(window)
            self.new_window.geometry('500x600')
            self.new_window.title('Laboratory Fees')
            self.gui_new = gui.GuiDesign(self.new_window)
            # New Frame for Laboratory Fees
            self.gui_new.frames(-5, -5, self.screen_width + 10, self.screen_height + 10, 'white')
            self.gui_new.frames(0, 0, self.screen_width, 70, '#AE0404')
            self.gui_new.label_design_center('', 6)
            self.gui_new.label_design_center('Laboratory Fees', 20)
            self.lbl = Label(self.new_window, text='Additional Laboratory Fee Description', bg='white', fg='black', font=('Times New Roman', 10))
            self.lbl.place(x=76, y=85)
            self.gui_new.textbox_design3(40, 120, 40, 1, 'black', 11)
            self.lbl = Label(self.new_window, text='Fee (₱)', bg='white', fg='black',
                             font=('Times New Roman', 10))
            self.lbl.place(x=392, y=85)
            self.gui_new.textbox_design3(360, 120, 15, 1, 'black', 11)
            def save():
                self.new_window.destroy()
            self.button = Button(self.new_window, width=7, text='Add More', bg='white', fg='black',
                            pady=3, padx=30, cursor='hand2',
                            border=0, borderwidth=1, relief='solid', highlightbackground='black',
                            highlightcolor='black', highlightthickness=2)
            self.button.place(x=215, y=500)
            self.button = Button(self.new_window, width=5, text='Save', command=save, bg='white', fg='black',
                            pady=3, padx=30, cursor='hand2',
                            border=0, borderwidth=1, relief='solid', highlightbackground='black',
                            highlightcolor='black', highlightthickness=2)
            self.button.place(x=350, y=500)



        button = Button(window, text='Add More Laboratory Fee', command=open_new_window, bg='white', fg='black', pady = 3, padx = 30, cursor='hand2',
                        border=0, borderwidth=1, relief='solid', highlightbackground='black', highlightcolor='black', highlightthickness=2)
        button.place(x=950 + 202, y=500)
    def save_update(self):
        self.gui.button_design(1440, 825, 'Save', 'green', 'black', 'black', 2, 5, 3)
        self.gui.button_design(1380, 825, 'Update', 'green', 'black', 'black', 2, 6, 3)
        self.gui.button_design(1333, 825, 'New', 'green', 'black', 'black', 2, 4, 3)

# Calling Out the Assessment Form
assessment_form = AssessmentForm()
assessment_form.header()
assessment_form.student_information()
assessment_form.student_subjects()
assessment_form.miscellaneous_fees()
assessment_form.total_fees()
assessment_form.payment_schedule()
assessment_form.laboratory_fees()
assessment_form.save_update()

window.mainloop()