
# initialization values .....

net_income = 0
gross_income = 0
total_deduction = 0
employee_name = " "
pagibig_contri = 100.00

#Getting the values of employee's name, rate per hour, no. of days per week, number of weeks per month

employee_name = input("Employee's Name: ")
rate_per_hour = float(input("Enter Employee's Rate per Hour: "))
number_of_days_per_week = float(input("Enter Employee's Number of Days per Week: "))
number_of_weeks_per_month = float(input("Enter Employee's Number of Weeks per Month: "))
sss_contri = float(input("Enter Employee's SSS Contribution: "))
philhealth_contri = float(input("Enter Employee's Philhealth Contribution: "))
tax_contri = float(input("Enter Employee's Tax Contribution: "))


# setting formula for the computation of gross income

gross_income = rate_per_hour * number_of_days_per_week * number_of_weeks_per_month
total_deduction = sss_contri + philhealth_contri + tax_contri + pagibig_contri
net_income = gross_income - total_deduction

# Displaying the value of employee's name, net income, gross income, total deduction

print("Employee's Name:", employee_name)
print("Net Income:", net_income)
print("Gross Income:", gross_income)
print("Total Deduction", total_deduction)
