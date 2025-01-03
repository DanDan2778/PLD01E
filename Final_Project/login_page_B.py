import login_page_A as log
import tkinter as tk

window = tk.Tk()
window.geometry('700x700')
login = log.LoginPage(window)
login.header()
login.login_details()
login.login_buttons()
window.resizable(False, False)
window.mainloop()
