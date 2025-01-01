import login_page_A as log
import tkinter as tk

window = tk.Tk()
window.geometry('700x850')
login = log.LoginPage(window)
login.header()

window.mainloop()


