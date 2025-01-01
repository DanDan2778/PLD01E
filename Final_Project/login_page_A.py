import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

from anaconda_cloud_auth import login

import gui_design as gui


class LoginPage:
    def __init__(self, window):
        self.window = window
        self.gui = gui.GuiDesign(self.window)
        self.window.title('DA\'s Login Page')
        self.lbl = Label(window, bg='white', width=1540, height= 900)
        self.lbl.place(x=-1, y=-1)
        self.image = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\amanahis_logo.png'

    def header(self):
        self.gui.frames(0, 0, 1540, 900, "#D9D9D9")
    # Logo
        image = Image.open(self.image)
        bck_pic = ImageTk.PhotoImage(image.resize((200, 120)))
        image_label = Label(self.window, image=bck_pic, bg='#D9D9D9')
        image_label.place(x=175, y=30)
        image_label.image = bck_pic
    # Title
        # GEAR's txt
        label = Label(self.window, text='GEAR\'s', bg='#D9D9D9', font=('Calibre', 50, 'bold'))
        label.place(x=367, y=30)
        # Login Page txt
        label = Label(self.window, text='Login Page', bg='#D9D9D9', font=('Calibre', 25))
        label.place(x=390, y=100)

    def login_details(self):
        self.gui.frames(0, 150, 1540, 100, 'blue')


"""window = tk.Tk()
window.geometry('700x850')"""
"""loginpage = LoginPage(window)
loginpage.header()
loginpage.login_details()
window.mainloop()"""