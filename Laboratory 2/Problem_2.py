# Initialization of Pag-Ibig Contribution

pagibig_contrib = 100

# Getting the value of Employee's Name, Department, Rate per Hr.,
# No. of Working Hrs. per Day, No. of Days per Week, and No. of Weeks per Month

employees_name = str(input("Employee's Name: "))
department = str(input("Department: "))
rate_per_hr = float(input("Rate Per Hour: "))
hrs_per_day = float(input("Working Hours per Day: "))
days_per_week = int(input("Numbers of Days per Week: "))
weeks_per_month = int(input("Number of Weeks per Month: "))

# Setting a Formula for Gross Income

gross_income = round(hrs_per_day * days_per_week * weeks_per_month * rate_per_hr)

# Defining the value of SSS Contribution and Philhealth Contribution Based on the Computed Gross Income

if 0 <= gross_income <= 20000:
    sss_contrib = 125.75
    philhealth_contrib = 100.00
elif 20001 <= gross_income <= 50000.00:
    sss_contrib = 2200.50
    philhealth_contrib = 1200.00
elif 50001 <= gross_income <= 75000.00:
    sss_contrib = 4800.00
    philhealth_contrib = 6800.00
else:
    sss_contrib = 5800.00
    philhealth_contrib = 8800.00

# Setting a Formula for Total Deduction, and Net Income

total_deduction = sss_contrib + pagibig_contrib + philhealth_contrib
net_income = gross_income - total_deduction

# Displaying Employee's Paycheck


print("\nEmployee's Name:", employees_name)
print("Department:", department)
print("Total Deduction:", f"{total_deduction:.2f}")
print("Gross Income:", f"{gross_income:.2f}")
print("Net Income:", f"{net_income: .2f}")
