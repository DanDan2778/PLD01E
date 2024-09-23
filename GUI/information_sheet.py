import tkinter

window = tkinter.Tk()
window.title("Employee Pay Check")
#window.geometry("1080x600")


# Main Frame
main_frame = tkinter.Frame(window)
main_frame.grid()

# Employee Paycheck Information Frame
company_frame = tkinter.Frame(main_frame)
company_frame= tkinter.LabelFrame(window, text="Company Information")
company_frame.grid()

# Company Information Widgets
company_name_label = tkinter.Label(company_frame, text="Company Name: ")
company_name_entry = tkinter.Entry(company_frame)
employee_department = tkinter.Label(company_frame, text="Department: ")
department_entry = tkinter.Entry(company_frame)

# Employee Information Frame

# Employee Information Widgets
employee_name_label = tkinter.Label(company_frame, text="Employee Name: ")
employee_name_entry = tkinter.Entry(company_frame)
employee_code_number = tkinter.Label(company_frame, text="Employee Code/Number: ")
employee_code_entry = tkinter.Entry(company_frame)
pay_period_label = tkinter.Label(company_frame, text="Pay Period: ")
start_date_label = tkinter.Label(company_frame, text="From")
start_date_entry = tkinter.Entry(company_frame)
end_date_label = tkinter.Label(company_frame, text="to")
end_date_entry = tkinter.Entry(company_frame)

# Employee Salary Information Frame

# Rate per Hour, Hours per Day, Hours Overtimed, Hours of Absences, Number of Hours, Hours of Tardiness

# Company Information Display
company_name_label.grid(row=0, column=0,pady=10)
company_name_entry.grid(row=0, column=1)
employee_department.grid(row=0, column=2)
department_entry.grid(row=0, column=3)

# Employee Information Display
employee_name_label.grid(row=1, column=0, pady=20)
employee_name_entry.grid(row=1, column=1)
employee_code_number.grid(row=1, column=2)
employee_code_entry.grid(row=1, column=3)
pay_period_label.grid(row=2, column=0, sticky='w')
start_date_label.grid(row=2, column=1)  
start_date_entry.grid(row=2, column=2)
end_date_label.grid(row=2, column=3)
end_date_entry.grid(row=2, column=4)

window.mainloop()