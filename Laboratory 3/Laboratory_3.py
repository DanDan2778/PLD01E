# Initialization of Employee's and Company Information

company_name = ""
department = ""
employee_code = 0
employee_name = ""
salary_date_cut_off = ""
start_date = ""
rate_per_hour = 0
hours_per_payday = 0
hours_overtimed = 0
hours_of_absences = 0
no_of_hours = 0
hours_of_tardiness = 0
sss_contrib = 0
withholding_tax = 0
philhealth_contrib = 0
pagibig_contri = 100
gross_income = 0

# Getting the values of Company Name, Department, Employee Code, Employee Name, 
# Salary Date Cut-Off, Start Date, Rate per Hour, Hours per Day, Hours Overtimed, Hours of 
# Absences, Number of Hours, Hours of Tardiness

company_name = input("Company Name: ")
department = input("Department: ")
employee_code = int(input("Employee Code: "))
employee_name = input("Employee Name: ")
salary_date_cut_off = input("Salary Date Cut-off: ")
start_date = input("Start Date: ")
rate_per_hour = float(input("Rate Per Hour: "))
hours_per_payday = float(input("Number of Hours Per PayDay: "))
hours_overtimed = float(input("Number of Hours Overtimed: "))
hours_of_absences = float(input("Number of Hours of Absences: "))
no_of_hours = float(input("Number of Hours: "))
hours_of_tardiness = float(input("Number of Hours of Tardiness: "))

# Setting the Pay Period

pay_period = f"{start_date} to {salary_date_cut_off}"

# Formulating a For Basic Pay, Overtime Pay, Absences, Honorarium, 
# Tardiness, and Gross Earning

basic_pay = rate_per_hour * hours_per_payday
overtime = hours_overtimed * rate_per_hour
absences = hours_of_absences * rate_per_hour
honorarium = no_of_hours * rate_per_hour
tardiness = hours_of_tardiness * rate_per_hour
gross_earning = basic_pay + overtime + honorarium

# Determining the Withholding Tax, SSS Contribution, and PhilHealth Contribution 
# Based on the Gross Earning

# Value of Withholding Tax Based on the Gross Earning

if 0 <= gross_earning <= 10417:
    withholding_tax = 0.00
elif 10418 <= gross_earning <= 16666:
    withholding_tax = (0.15 * (gross_earning - 10417))
elif 16667 <= gross_earning <= 33332:
    withholding_tax = 937.50 + (0.20 * (gross_earning - 16666))
elif 33333 <= gross_earning <= 83332:
    withholding_tax = 4270.70 + (0.25 * (gross_earning - 33332))
elif 83333 <= gross_earning <= 333332:
    withholding_tax = 16770.70 + (0.30 * (gross_earning - 83332))
else:
    withholding_tax = 91770.70 + (0.35 * (gross_earning - 333332))

# Value of SSS Contribution Based on the Gross Earning

if 0 <= gross_earning < 4250:
    sss_contrib = 180
elif 4250 <= gross_earning <= 4749.99:
    sss_contrib = 202.50
elif 4750 <= gross_earning <= 5249.99:
    sss_contrib = 225
elif 5250 <= gross_earning <= 5749.99:
    sss_contrib = 247.50
elif 5750 <= gross_earning <= 6249.99:
    sss_contrib = 270
elif 6250 <= gross_earning <= 6749.99:
    sss_contrib = 292.50
elif 6750 <= gross_earning <= 7249.99:
    sss_contrib = 315.00
elif 7250 <= gross_earning <= 7749.99:
    sss_contrib = 337.50
elif 7750 <= gross_earning <= 8249.99:
    sss_contrib = 360.00
elif 8250 <= gross_earning <= 8749.99:
    sss_contrib = 382.50
elif 8750 <= gross_earning <= 9249.99:
    sss_contrib = 405.00
elif 9250 <= gross_earning <= 9749.99:
    sss_contrib = 427.50
elif 9750 <= gross_earning <= 10249.99:
    sss_contrib = 450.00
elif 10250 <= gross_earning <= 10749.99:
    sss_contrib = 472.50
elif 10750 <= gross_earning <= 11249.99:
    sss_contrib = 495.00
elif 11250 <= gross_earning <= 11749.99:
    sss_contrib = 517.50
elif 11750 <= gross_earning <= 12249.99:
    sss_contrib = 540.00
elif 12250 <= gross_earning <= 12749.99:
    sss_contrib = 562.50
elif 12750 <= gross_earning <= 13249.99:
    sss_contrib = 585.00
elif 13250 <= gross_earning <= 13749.99:
    sss_contrib = 607.50
elif 13750 <= gross_earning <= 14249.99:
    sss_contrib = 630.00
elif 14250 <= gross_earning <= 14749.99:
    sss_contrib = 652.50
elif 14750 <= gross_earning <= 15249.99:
    sss_contrib = 675.00
elif 15250 <= gross_earning <= 15749.99:
    sss_contrib = 697.50
elif 15750 <= gross_earning <= 16249.99:
    sss_contrib = 720.00
elif 16250 <= gross_earning <= 16749.99:
    sss_contrib = 742.50
elif 16750 <= gross_earning <= 17249.99:
    sss_contrib = 765.00
elif 17250 <= gross_earning <= 18249.99:
    sss_contrib = 787.50
elif 17750 <= gross_earning <= 18249.99:
    sss_contrib = 810.00
elif 18250 <= gross_earning <= 18749.99:
    sss_contrib = 832.50
elif 18750 <= gross_earning <= 19249.99:
    sss_contrib = 855.00
elif 19250 <= gross_earning <= 19749.99:
    sss_contrib = 877.50
else:
    sss_contrib = 900.00

# Value of PhilHealth Contribution Based on the Gross Earning
if (gross_earning < 10000):
    philhealth_contrib = 10000 * 0.05
elif (10001 <= gross_earning <= 99999.99):
    philhealth_contrib = gross_earning * 0.05
else:
    philhealth_contrib = 100000 * 0.05

# Formulating a Formula for Total Deduction and Net Income

total_deduction = absences + tardiness + sss_contrib + withholding_tax + philhealth_contrib + pagibig_contri
net_income = gross_earning - total_deduction

# Displaying the Employee's Payroll/Income Information including the Company Information

print("====================================================================================================")
print("\nCompany Name:", company_name)
print("Employee Code/Number: ", employee_code)
print("Employee Name:", employee_name)
print("Department:", department)
print("Salary Date Cut-Off: ", salary_date_cut_off)
print("Pay Period:", pay_period)
print("Basic Pay:", f"{basic_pay:.2f}")
print("Overtime Pay:", f"{overtime:.2f}")
print("Absences:", f"{absences:.2f}")
print("Honorarium:", f"{honorarium:.2f}")
print("Tardiness:", f"{tardiness:.2f}")
print("Withholding Tax:", f"{withholding_tax:.2f}")
print("SSS Contribution:", f"{sss_contrib:.2f}")
print("Pag-Ibig Contribution:", f"{pagibig_contri:.2f}")
print("PhilHealth Contribution:", f"{philhealth_contrib:.2f}")
print("Total Deduction:", f"{total_deduction:.2f}")
print("Gross Income:", f"{gross_earning:.2f}")
print("Net Income:", f"{net_income:.2f}")
print("\n====================================================================================================")