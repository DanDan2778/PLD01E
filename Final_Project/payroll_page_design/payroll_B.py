import tkinter as tk
from tkinter import *
import payroll_A as pay
window = tk.Tk()
window.title("Payroll System")
window.geometry('700x850')
window.resizable(False, False)
lbl = Label(window, bg='white', width=1540, height=900)
lbl.place(x=1, y= 1)

payroll = pay.payroll(window)
payroll.header()
payroll.basic_info()
payroll.deductions()
payroll.other_deductions()
payroll.deduction_summary()

mainloop()