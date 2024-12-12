import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


# Window Class
class GuiDesign:
    def __init__(self, window):
        self.window = window  # Store the window object
        self.frame1 = ''
        self.textbox = ''
        self.text_value = ''
        self.lbl = ''
        self.upload_button = ''
        self.length = ''
        self.width = ''
        self.image_location = ''
        self.image = ''
        self.bck_pic = ''
        self.round_button = ''
        self.image_label = ''

    def frames(self, x, y, width, height, bg):
        self.frame1 = Frame(self.window, width=width , height=height, border=0, bg=bg)
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(self.window, width=15, height=1, fg='black', bg='white', font=('Times New Roman', 13))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(self.window, width=31, height=1, fg='black', bg='white', font=('Arial', 13, 'bold'))
        self.textbox.place(x=x, y=y)
    def textbox_design_disabled(self, x, y, text):
        self.textbox = Entry(self.window, width=15, fg='black', font=('Arial', 13))
        self.textbox.insert(0, text)
        self.textbox.config(state='disabled')
        self.textbox.place(x=x, y=y)
    def textbox_design3(self, x, y, width, height, fg, font_size):
        self.textbox = Text(self.window, width=width, height=height, fg=fg, bg='white', font=('Times New Roman', font_size))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.text_value = text_value
        self.lbl = Label(self.window, text=text_value, bg='white', fg='black', font=('Calibre', 10, ))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value, font_size, font_format, font_color):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', fg=font_color, font=('Times New Roman', font_size, font_format))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value, font_size, font_color):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', fg=font_color, font=('Times New Roman', font_size))
        self.lbl.place(x=x, y=y)

    def title_design(self, x, y, text_value, font_size):
        self.text_value = text_value
        self.lbl = Label(self.window, text=text_value, bg='white', fg='black', font=('Calibre', font_size, 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y, button_label, bg, fg, border, thickness, width, pady):
        self.upload_button = Button(self.window, width=width, pady=pady, text=button_label, bg=bg, fg=fg, cursor='hand2',
                                    border=0, borderwidth=1, relief='solid', highlightbackground=border, highlightcolor=border,
                                    highlightthickness=2,)
        self.upload_button.place(x=x, y=y)

    def image_design(self, image_location, x, y, length, width):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)  # Load the image
        self.bck_pic = ImageTk.PhotoImage(self.image.resize((self.length, self.width)))  # Resize and convert to PhotoImage
        self.image_label = Label(self.window, image=self.bck_pic)  # Use a specific name for the image label
        self.image_label.place(x=x, y=y)  # Place the image on the window
        # Keep a reference to the image to prevent it from being garbage collected
        self.image_label.image = self.bck_pic  # Necessary to keep the image object alive

    def image_design2(self, image_location, x, y, length, width, bg):
        self.length = length
        self.width = width
        self.image_location = image_location
        self.image = Image.open(image_location)  # Load the image
        self.bck_pic = ImageTk.PhotoImage(
            self.image.resize((self.length, self.width)))  # Resize and convert to PhotoImage
        self.image_label = Label(self.window, image=self.bck_pic, bd=0, bg=bg)  # Use a specific name for the image label
        self.image_label.place(x=x, y=y)  # Place the image on the window
        # Keep a reference to the image to prevent it from being garbage collected
        self.image_label.image = self.bck_pic  # Necessary to keep the image object alive
    def label_design_center(self, text_value, font_size):
        self.text_value = text_value
        self.lbl = Label(self.window, text=text_value, bg='#AE0404', fg='black', font=('Times New Roman', font_size), width=30, height=1, anchor='center')
        self.lbl.pack()

    def label_textbox_bold(self, x, y, text_value, distance, width):
        self.label_design2(x, y, text_value, 10, 'bold', 'black')
        self.textbox_design3(x + distance, y, width, 1, 'black', 11)
    def line(self, x1, y1, x2, y2):
        canvas = tk.Canvas(self.window, width=400, height=400, bg='blue')
        canvas.pack()

        # Draw a line (x1, y1, x2, y2)
        canvas.create_line(x1, y1, x2, y2, fill="black", width=2)
