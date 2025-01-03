import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

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
        self.inputs = []
        self.input_count = 0
        self.add_button = None
        self.button_x = 1340
        self.button_y = 392
        self.new_window = ''

    def create_curved_frame(self, x, y, width, height, radius=20, color="lightblue"):
        # Create a canvas
        canvas = tk.Canvas(self.window, width=width, height=height, bg=color, bd=0, highlightthickness=0)
        canvas.place(x=x, y=y)

        # Create a rectangle with rounded corners using create_arc for the corners
        canvas.create_arc(0, 0, radius * 2, radius * 2, start=90, extent=90, fill=color, outline=color)
        canvas.create_arc(width - radius * 2, 0, width, radius * 2, start=0, extent=90, fill=color, outline=color)
        canvas.create_arc(0, height - radius * 2, radius * 2, height, start=180, extent=90, fill=color, outline=color)
        canvas.create_arc(width - radius * 2, height - radius * 2, width, height, start=270, extent=90, fill=color,
                          outline=color)

        # Create the main rectangle (excluding the corners)
        canvas.create_rectangle(radius, 0, width - radius, height, fill=color, outline=color)
        canvas.create_rectangle(0, radius, width, height - radius, fill=color, outline=color)

        return canvas

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
        self.textbox = Entry(self.window, width=15, fg='black', font=('Arial', 13), bd = 2,highlightthickness=0, relief='groove')
        self.textbox.insert(0, text)
        self.textbox.config(state='disabled')
        self.textbox.place(x=x, y=y)
    def textbox_design3(self, x, y, width, height, fg, font_size):
        self.textbox = Text(self.window, width=width, height=height, fg=fg, bg='white', font=('Times New Roman', font_size), bd = 2,highlightthickness=0, relief='groove')
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y, width, height, fg, font_size):
        self.textbox = Text(self.window, width=width, height=height, fg=fg, bg='#f0f0f0',
                            font=('Times New Roman', font_size), bd=2, highlightthickness=0, relief='groove')
        self.textbox.config(state='disabled')
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

    def button_design(self, x, y, button_label, bg, fg, border_color, thickness, width, pady):
        self.upload_button = Button(self.window, width=width, pady=pady, text=button_label, bg=bg, fg=fg, cursor='hand2',
                                    border=0, borderwidth=1, relief='solid', highlightbackground=border_color, highlightcolor=border_color,
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
    def label_design_center(self, text_value, font_size, bg):
        self.text_value = text_value
        self.lbl = Label(self.window, text=text_value, bg=bg, fg='black', font=('Times New Roman', font_size), width=30, height=1, anchor='center')
        self.lbl.pack()

    def label_textbox_bold(self, x, y, text_value, distance, width):
        self.label_design2(x, y, text_value, 10, 'bold', 'black')
        self.textbox_design3(x + distance, y, width, 1, 'black', 11)

    def label_textbox(self, x, y, text_value, distance, width):
        self.label_design2(x, y, text_value, 10, 'normal', 'black')
        self.textbox_design3(x + distance, y, width, 1, 'black', 11)

    def label_textbox_bold_pack(self, x, y, text_value, distance, width):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg='white', fg='black', font=('Times New Roman', 11, 'bold'))
        self.lbl.grid(row=y, column=distance, padx=5, pady=5)
        distance = x + distance
        self.textbox = Text(self.window, width= distance, height=y, fg='black', bg='#f0f0f0',
                            font=('Times New Roman', 11), bd=2, highlightthickness=0, relief='groove')
        self.textbox.grid(row=y, column=distance, padx=5, pady=5)


    def label_textbox_bold_disabled(self, x, y, text_value, distance, width, text):
        self.label_design2(x, y, text_value, 10, 'bold', 'black')
        self.textbox_design_disabled(x + distance, y, text)

    def label_textbox_disabled(self, x, y, text_value, distance, width, text):
        self.label_design2(x, y, text_value, 10, 'normal', 'black')
        self.textbox_design_disabled(x + distance, y, text)

    def line(self, x, y, length, bg):
        self.lbl = Label(self.window, text='_' * length, bg=bg)
        self.lbl.place(x=x, y=y)

    def double_line(self, x_loc, y_loc, length, fg, bg):
        canvas = tk.Canvas(self.window, width=length * 2, height=10, bg=bg, bd=0, relief="flat", highlightthickness=0)
        canvas.place(x=x_loc, y=y_loc)

        canvas.create_line(0, 5, length * 4, 5, fill=fg, width=1)

        canvas.create_line(0, 9, length * 4, 9, fill=fg, width=1)


    def horizontal_line(self, x, y, length, bg):
        for i in range(length):
            # Create a label with the '|' character and place it on the window
            label = tk.Label(self.window, text='|', bg=bg, font=('Arial', 12))
            label.place(x=x, y=y + i * 10)

    def label_design_bg(self, x, y, text_value, bg, font_size, fg):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg=bg, fg=fg, font=('Times New Roman', font_size))
        self.lbl.place(x=x, y=y)

    def vertical_line(self, x_loc, y_loc, length, fg, bg):
        # Create a canvas to draw the line
        canvas = tk.Canvas(self.window, width=10, height=length * 4, bg=bg, bd=0, relief="flat", highlightthickness=0)
        canvas.place(x=x_loc, y=y_loc)

        canvas.create_line(5, 0, 5, length * 4, fill=fg, width=1)

    def label_design4(self, x, y, text_value, font_size, font_format, font_color, bg):
        self.text_value = text_value
        self.lbl = Label(text=text_value, bg=bg, fg=font_color, font=('Times New Roman', font_size, font_format))
        self.lbl.place(x=x, y=y)



