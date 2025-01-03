import tkinter as tk
import user_account_class as uac


window = tk.Tk()
window.title("User Account Page")
window.geometry("800x400")
window.resizable(False, False)
user_account_page = uac.UserAccountPage(window)
user_account_page.header()
user_account_page.personal_info()
user_account_page.button()
window.mainloop()