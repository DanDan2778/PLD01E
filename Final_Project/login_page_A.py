from tkinter import *
from PIL import Image, ImageTk
import gui_design as gui


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.gui = gui.GuiDesign(self.window)
        self.window.title('GEAR\'s Login Page')
        self.lbl = Label(window, bg='#8CA3A3', width=1540, height= 900)
        self.lbl.place(x=-1, y=-1)
        self.logo = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\amanahis_logo.png'
        self.prof = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\prof_login.png'
        self.lock = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\lock_logo.jpg'

    def header(self):
        color = '#563F46'
        frame = self.gui.frames(0, 0, 1540, 178, color)
    # Logo
        image = Image.open(self.logo)
        bck_pic = ImageTk.PhotoImage(image.resize((200, 120)))
        image_label = Label(frame, image=bck_pic, bg=color)
        image_label.place(x=155, y=30)
        image_label.image = bck_pic
    # Title
        # GEAR's txt
        label = Label(frame, text='GEAR\'s', bg=color, font=('Calibre', 50, 'bold'))
        label.place(x=347, y=30)
        # Login Page txt
        label = Label(frame, text='Login Page', bg=color, font=('Calibre', 25))
        label.place(x=370, y=100)

    def login_details(self):
        color = '#D9D9D9'
        main_color = '#C8C3CC'
        frame = self.gui.frames(90, 209, 540, 400, main_color)
        frame2 = self.gui.frames(181, 256, 361, 55, color)
        self.gui.frames(181, 340, 361, 55, color)
    # Username
        # txt
        label = Label(frame, text='Username', bg=main_color, font=('Calibre', 11, 'bold'))
        label.place(x=181, y=226)
        # Logo
        image = Image.open(self.prof)
        bck_pic = ImageTk.PhotoImage(image.resize((49, 50)))
        image_label = Label(frame2, image=bck_pic, bg=color)
        image_label.place(x=181, y=256)
        image_label.image = bck_pic
        # Texbox
        textbox = Text(frame, width=23, height=1, bg=color, font=('Calibre', 16))
        textbox.place(x=250, y=270)
        textbox.insert(1.0, 'Enter Username')
    # Password
        label = Label(frame, text='Password', bg=main_color, font=('Calibre', 11, 'bold'))
        label.place(x=181, y=310)
        # Logo
        image = Image.open(self.lock)
        bck_pic = ImageTk.PhotoImage(image.resize((49, 50)))
        image_label = Label(frame2, image=bck_pic, bg=color)
        image_label.place(x=181, y=340)
        image_label.image = bck_pic
        # Texbox
        textbox_pass = Text(frame, width=23, height=1, bg=color, font=('Calibre', 16))
        textbox_pass.place(x=250, y=354)
        textbox_pass.insert(1.0, 'Enter Password')
        # Show/Hide Password Button
        def toggle_password():
            current_text = textbox_pass.get("1.0", "end-1c")
            if show_password_button.cget("text") == "Show":
                textbox_pass.delete("1.0", "end-1c")
                textbox_pass.insert("1.0", current_text.replace("*", ""))  # Remove asterisks
                show_password_button.config(text="Hide")
            else:
                password = textbox_pass.get("1.0", "end-1c")
                textbox_pass.delete("1.0", "end-1c")
                textbox_pass.insert("1.0", "*" * len(password))
                show_password_button.config(text="Show")

        # Show Button for Password
        show_password_button = Button(frame, text="Show", command=toggle_password, font=('Calibre', 12), bg="lightgreen")
        show_password_button.place(x=480, y=400)

    def login_buttons(self):
        self.gui.button_design(320, 435, 'Login', '#563F46', 'white', '#563F46', 15, 15, 7)
        #self.gui.button_design(400, 465, 'Forgot Password!', '#563F46', 'white', '#563F46', 15, 15, 7)
        button = Button(self.window, width=15, pady=7,fg='blue', text='Forgot Password!',
                        bg='#C8C3CC', cursor='hand2', border=0, borderwidth=0, relief='solid',
                        highlightthickness=0)
        button.place(x=325, y=485)
        #self.gui.button_design(221, 500, 'Create Account', '#563F46', 'white', '#563F46', 15, 15, 7)
        button = Button(self.window, width=6, pady=7, text='Sign Up',
                        bg='#C8C3CC', fg='red', cursor='hand2', border=0, borderwidth=0, relief='solid',
                        highlightthickness=0)
        button.place(x=415, y=550)
        label = Label(self.window, text='Don\'t have an account?', bg='#C8C3CC', font=('Calibre', 9, 'bold'))
        label.place(x=271, y=555)




