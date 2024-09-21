# Initialization of Pag-ibig Contribution

companyName = ""
department = ""
employeeCode = 0
employeeName = ""
salaryDateCutOff = ""
ratePerHour = 0
hoursPerDay = 0
hoursOvertimed = 0
hoursOfAbsences = 0
noOfHours = 0
hoursOfTardiness = 0
pagibigContri = 100
grossIncome = 0
philhealth = 0

# Getting the values of Company Name, Department, Employee COde, Employee Name, Salary Date Cut-Off, Rate per Hour, Hours per Day, Hours Overtiemed, Hours of Absences, Number of Hours, Hours of Tardiness

companyName = input("Company Name: ")
department = input("Departmet: ")
employeeName = input("Employee Name: ")
salaryDateCutOff = input("Salary Date Cut-Off (mm/dd/yyy): ")
ratePerHour = float(input("Rate Per Hour: "))
hoursPerDay = float(input("Number of Hours Per Day: "))
hoursOvertimed = float(input("Number of Hours Overtimed: "))
hoursOfAbsences = float(input("Number Of Hours of Absences: "))
noOfHours = float(input("No of Hours: "))
hoursOfTardiness = float(input("Number of Hours of Tardiness: "))
startDate = input("Start Date (mm/dd/yyyy): ")
endDate = input("End Date(mm/dd/yyyy): ")


payPeriod = f"{startDate} to {endDate}"

# Formulating a for Basic Pay, Overtime Pay, Absences, Honorarium, Tardiness

basicPay = ratePerHour * hoursPerDay
overtime = hoursOvertimed * ratePerHour
absences = hoursOfAbsences * ratePerHour
honorarium = noOfHours * ratePerHour
tardiness = hoursOfTardiness * ratePerHour
grossEarning = basicPay + overtime + honorarium

# Determining the Withholding Tax, SSS Contribution, and PhilHealth Contribution.

if 0 <= grossEarning < 4250:
    sssContrib = 180
elif 4250 <= grossEarning <= 4749.99:
    sssContrib = 202.50
elif 4750 <= grossEarning <= 5249.99:
    sssContrib = 225
elif 5250 <= grossEarning <= 5749.99:
    sssContrib = 247.50
elif 5750 <= grossEarning <= 6249.99:
    sssContrib = 270
elif 6250 <= grossEarning <= 6749.99:
    sssContrib = 292.50
elif 6750 <= grossEarning <= 7249.99:
    sssContrib = 315.00
elif 7250 <= grossEarning <= 7749.99:
    sssContrib = 337.50
elif 7750 <= grossEarning <= 8249.99:
    sssContrib = 360
elif 8250 <= grossEarning <= 8749.99:
    sssContrib = 382.50
elif 8750 <= grossEarning <= 9249.99:
    sssContrib = 405
elif 9250 <= grossEarning <= 9749.99:
    sssContrib = 427.50
elif 9750 <= grossEarning <= 10249.99:
    sssContrib = 450
elif 10250 <= grossEarning <= 10749.99:
    sssContrib = 472.50
elif 10750 <= grossEarning <= 11249.99:
    sssContrib = 495
elif 11250 <= grossEarning <= 11749.99:
    sssContrib = 517.50
elif 11750 <= grossEarning <= 12249.99:
    sssContrib = 540
elif 12250 <= grossEarning <= 12749.99:
    sssContrib = 562.50
elif 12750 <= grossEarning <= 13249.99:
    sssContrib = 585
elif 13250 <= grossEarning <= 13749.99:
    sssContrib = 607.50
elif 13750 <= grossEarning <= 14249.99:
    sssContrib = 630
elif 14250 <= grossEarning <= 14749.99:
    sssContrib = 652.50
elif 14750 <= grossEarning <= 15249.99:
    sssContrib = 675
elif 15250 <= grossEarning <= 15749.99:
    sssContrib = 697.50
elif 15750 <= grossEarning <= 16249.99:
    sssContrib = 720
elif 16250 <= grossEarning <= 16749.99:
    sssContrib = 742.50
elif 16750 <= grossEarning <= 17249.99:
    sssContrib = 765
elif 17250 <= grossEarning <= 18249.99:
    sssContrib = 787.50
elif 17750 <= grossEarning <= 18749.99:
    sssContrib = 810
elif 18250 <= grossEarning <= 19749.99:
    sssContrib = 832.50
elif 18750 <= grossEarning <= 19249.99:
    sssContrib = 855
elif 19250 <= grossEarning <= 19749.99:
    sssContrib = 877.50
else:
    sssContrib = 900

# Statement for witholding tax

if 0 <= grossEarning <= 20832.99:
    witholdingTax = 0.00
elif 20833 <= grossEarning <= 33332:
    witholdingTax = 0.15 / 20833
elif 33333 <= grossEarning <= 66666:
    witholdingTax = 1875 + 0.20 / 33333
elif 66667 <= grossEarning <= 166666:
    witholdingTax = 8541.80 + 0.25 / 66667
elif 166666 <= grossEarning <= 666666:
    witholdingTax = 33541.80 + 0.130 / 166667
else:
    witholdingTax = 183541.80 + 0.30 / 666667

# Philhealth
if grossIncome == 10000:
    philhealth = 500
elif 10000.01 <= grossIncome <= 99999.99:
    philhealth = grossIncome * 0.05
elif grossIncome == 100000:
    philhealth = 5000


# Formulation a formula for Deductions and Net Pay

deductions = sssContrib + witholdingTax + pagibigContri + philhealth
netPay = grossEarning - deductions

# Display Pay Check

print("======================================================================")
print("")
print("Company Name: ", companyName)
print("Employee Code: ", employeeCode)
print("Employee Name: ", employeeName)
print("Department: ", department)
print("Salary Date Cut-Off:", salaryDateCutOff)
print("Pay Period: ", payPeriod)
print("Basic Pay: ", basicPay)
print("Overtime: : ", overtime)
print("Absences: ", absences)
print("Honorarium: ", honorarium)
print("Tardiness: ", tardiness)
print("Withholding Tax: ", witholdingTax)
print("SSS Contribution: ", sssContrib)   
print("HDMF Contribution: ", pagibigContri)
print("PhilHealth Contribution: ", philhealth)
print("Deductions: ", deductions)
print("Gross Earnings: ", grossEarning)
print("Net Pay: ", netPay)
print("======================================================================")