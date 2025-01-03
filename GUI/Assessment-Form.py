import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

#windows
window = tk.Tk()
image = Image.open('C:\\Users\\danie\\Desktop\\repository\\PLD01E\\GUI\\lpucav.PNG')
bck_pic = ImageTk.PhotoImage(image.resize((500, 500)))
lbl = Label(window, image=bck_pic)
lbl.place(x=1, y= 1)
window.title("ASSESSMENT FORM")
window.geometry('1540x900')

#design gui interface
class DesignGuiInterface:
        def __init__(self):
            self.frame1= ''
            self.textbox = ''
            self.text_value = ''
            self.lbl = ''
            self.upload_button = ''
            self.length = ''
            self.width = ''
            self.image_location = ''
            self.image = ''
            self.bck_pic = ''
        def frames(self, x, y):
            self.frame1 = Frame(window, width=1100, height=160, border=0, bg='#FF2400')
            self.frame1.place(x=x, y=y)
        def textbox_design1(self, x, y):
            self.textbox = Text(width=25, height=1, fg='black', bg='white', font=('Arial', 11, 'bold'))
            self.textbox.place(x=x, y=y)
        def textbox_design2(self, x, y):
            self.textbox = Text(width=31, height=1, fg='black', bg='white',font=('Arial', 11, 'bold'))
            self.textbox.place(x=x, y=y)
        def label_design(self,x, y, text_value):
            self.text_value = text_value
            self.lbl = Label(text=text_value, bg='#FF2400', font=('Calibre', 10))
            self.lbl.place(x=x, y=y)
        def label_design2(self, x, y, text_value, font_size, font_format, font_color):
            self.text_value = text_value
            self.lbl = Label(text=text_value, bg='white', fg=font_color,  font=('Times New Roman', font_size, font_format))
            self.lbl.place(x=x, y=y)
        def label_design3(self, x, y, text_value, font_size, font_color):
            self.text_value = text_value
            self.lbl = Label(text=text_value, bg='white', fg=font_color, font=('Times New Roman', font_size))
            self.lbl.place(x=x, y=y)
        def button_design(self, x, y):
            self.upload_button = Button(width=15, pady=7, text='Choose File', bg='#57a1f8', fg='white', cursor='hand2', border=0)
            self.upload_button.place(x=x, y=y)
        def image_design(self, image_location, x, y, length, width):
            self.length = length
            self.width = width
            self.image_location = image_location
            self.image = Image.open(image_location)
            self.bck_pic = ImageTk.PhotoImage(self.image.resize((self.length, self.width)))
            self.lbl = Label(window, image=self.bck_pic)
            self.lbl.place(x=x, y=y)

#displaying the frames
#instantiation of the class
my_gui_design = DesignGuiInterface()
my_gui_design.frames(200,220)
my_gui_design.frames(200,390)
my_gui_design.frames(200,560)

firstnametxt = my_gui_design.textbox_design1(240, 262)
middle_nametxt = my_gui_design.textbox_design1(x=449, y=262)
surnametxt = my_gui_design.textbox_design1(x=658, y=262)
suffixtxt = my_gui_design.textbox_design1(867, 262)
date_of_birthtxt = my_gui_design.textbox_design1(240, 330)
nationalitytxt = my_gui_design.textbox_design1(867, 330)
#display for second frame
departmenttxt = my_gui_design.textbox_design2(232, 500)
designationtxt = my_gui_design.textbox_design2(495, 500)
employee_statustxt = my_gui_design.textbox_design2(760, 500)
employee_numbertxt = my_gui_design.textbox_design2(1025, 500)
contact_numbertxt = my_gui_design.textbox_design2(232, 435)
email_addresstxt = my_gui_design.textbox_design2(495, 435)
other_social_mediatxt = my_gui_design.textbox_design2(760, 435)
social_media_accounttxt = my_gui_design.textbox_design2(1025, 435)
#display for third frame
address_line1txt = my_gui_design.textbox_design2(232, 600)
address_line2txt = my_gui_design.textbox_design2(495, 600)
baranggaytxt = my_gui_design.textbox_design2(760, 600)
municipalittxt = my_gui_design.textbox_design2(1025, 600)

zip_codetxt = my_gui_design.textbox_design2(760, 670)
countrytxt = my_gui_design.textbox_design2(495, 670)
picturepathtxt = my_gui_design.textbox_design2(1025, 670)
#textbox label for first frame
firstname_lbl = my_gui_design.label_design(240, 235, 'Firstname')
middle_namelbl = my_gui_design.label_design(450, 235, 'Middlename')
surnamelbl = my_gui_design.label_design(658, 235, 'Surname')
suffixlbl = my_gui_design.label_design(867, 235, 'Suffix')
date_of_birthlbl = my_gui_design.label_design(240, 305, 'Date of Birth')
nationalitylbl = my_gui_design.label_design(867, 305, 'Nationality')
civil_statuslbl = my_gui_design.label_design(660, 305, 'Civil Status')
genderlbl = my_gui_design.label_design(450, 305, 'Gender')
#text labal for second frame
departmentlbl = my_gui_design.label_design(232, 410, 'Department')
designationlbl = my_gui_design.label_design(498, 410, 'Designation')
emp_statuslbl = my_gui_design.label_design(764, 410, 'Employee Status')
emp_numberlbl = my_gui_design.label_design(1030, 410, 'Employee Number')
emp_contact_numlbl = my_gui_design.label_design(232, 475, 'Contact Number')
emp_email_addlbl = my_gui_design.label_design(498, 475, 'Email Address')
emp_other_social_media_accountlbl = my_gui_design.label_design(764, 475,'Other Social Media Account')
emp_social_media_accountlb = my_gui_design.label_design(1030, 475, 'Social Media Account')
#text label for third frame
address_line1txt = my_gui_design.label_design(232, 575, 'Address Line 1')
address_line2txt = my_gui_design.label_design(495, 575, 'Address Line 2(Optional)')
baranggaytxt = my_gui_design.label_design(760, 575, 'Baranggay')
municipalittxt = my_gui_design.label_design(1025, 575, 'Municipality')
provincetxt = my_gui_design.label_design(232, 645, 'Province')
zip_codetxt = my_gui_design.label_design(498, 645, 'Zip Code')
countrytxt = my_gui_design.label_design(764, 645, 'Country')
picturepathtxt = my_gui_design.label_design(1024, 645, 'Picture Path of Uploaded Image')
# Combobox creationn = tk.StringVar()
# combo_field = ttk.Combobox(window, width = 30, textvariable = n)
# # Adding combobox drop down list
# combo_field['values'] = (' Female', ' Male ', ' Unidentified')
# combo_field.place(x=450, y=330)
# combo_field.current()

# Adding combox for civil status
# Combobox creation
n = tk.StringVar()
combo_field1 = ttk.Combobox(window, width = 30, textvariable = n)
combo_field1['values'] = (' Single', ' Married ', ' Widow', ' Legally Separated', ' Annulled')
combo_field1.place(x=660, y=330)
combo_field1.current()
window.mainloop()




