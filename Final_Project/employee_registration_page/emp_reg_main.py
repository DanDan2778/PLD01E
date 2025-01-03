import tkinter as tk
import Emp_reg_class as erc



main = tk.Tk()
main.geometry('700x850')
emp_reg_page = erc.EmpRegPage(main)
emp_reg_page.header()
emp_reg_page.emp_pers_info()
emp_reg_page.company_info()
emp_reg_page.contact_info()
emp_reg_page.adress()
emp_reg_page.save_cancel_button()
main.resizable(False, False)
main.mainloop()