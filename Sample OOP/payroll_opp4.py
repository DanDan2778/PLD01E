import payroll_oop2

employee_payroll = payroll_oop2.Employee_Salary()
emp_rate_per_hour = float(input("Enter Value for Rate Per Hour: "))
emp_num_of_absences = int(input("Enter Value for Number of Absences: "))
tardiness_hours = int(input("Enter Number of Tardiness: "))

absences_deduction = employee_payroll.get_absences_deduction(emp_rate_per_hour, emp_num_of_absences)
tardiness_deduction = employee_payroll.get_tardiness_deduction(emp_rate_per_hour, tardiness_hours)

partial_deductions = absences_deduction + tardiness_deduction
print("Employee Partial Deduction: %.2f" % partial_deductions)
