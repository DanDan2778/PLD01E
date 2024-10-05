import payroll_oop2

payroll1 = payroll_oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter the Value for Rate per Hour: "))
emp_hour_overtime = float(input("Enter the Number of Hours Overtime: "))
emp_hour_tardiness = float(input("Enter the Number of Tardiness: "))

tardiness_deduction = payroll1.get_tardiness_deduction(emp_hour_tardiness, emp_rate_per_hour)
overtime_pay = payroll1.get_overtime_pay(emp_hour_overtime, emp_rate_per_hour)

print("Employee Tardiness Deduction is: %.2f" % tardiness_deduction)
print("Employee Overtime Pay: %.2f" % overtime_pay)
