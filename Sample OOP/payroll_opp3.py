import payroll_oop2

obj = payroll_oop2.Employee_Info()
company = input("Enter Company Name: ")
department = input("Enter Employee Department: ")
employee_name = input("Enter Employee Name: ")
employee_code = input("Enter Employee Number or Code: ")
salary_cutoff = input("Enter Salary Cut-Off: ")
emp_data = obj.get_emp_data(company, department, employee_name, employee_code, salary_cutoff)

#data entry for basic pay computation
obj2 = payroll_oop2.Employee_Salary()
rate_pay = float(input("Enter Employee Rate per Hour: "))
number_working_hours = float(input("Enter Employee Number of Working Hours: "))
honorarium_pay = float(input("Enter Honorarium Pay: "))
number_absences = float(input("Enter Number of Absences in Hours: "))

#computation for basic pay
basic_pay = obj2.get_basic_pay(rate_pay, number_working_hours)
absences_deduction = obj2.get_absences_deduction(rate_pay, number_absences)

#display output
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")
obj.desiplay_data()
print("Basic Pay: %.2f" % basic_pay)
print("Honorarium Pay: %.2f" % honorarium_pay)
print("Employee Absences Deduction: %.2f" % absences_deduction)
print("---------------------------------------------------------------------")
print("---------------------------------------------------------------------")


