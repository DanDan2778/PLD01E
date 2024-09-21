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

# Getting the values of Company Name, Department, Employee COde, Employee Name, Salary Date Cut-Off, Rate per Hour, Hours per Day, Hours Overtiemed, Hours of Absences, Number of Hours, Hours of Tardiness

companyName = input("Company Name: ")
department = input("Departmet: ")
employeeName = input("Employee Name: ")
salaryDateCutOff = ("Salary Date Cut-Off (mm/dd/yyy): ")
ratePerHour = input("Rate Per Hour: ")
hoursPerDay = input("Number of Hours Per Day: ")
hoursOvertimed = input("Number of Hours Overtimed: ")
hoursOfAbsences = input("Number Of Hours of Absences: ")
noOfHours = input("No of Hours: ", noOfHours)
hoursOfTardiness = input("Number of Hours of Tardiness: ")
startDate = input("Start Date: ")
endDate = input("End Date: ")


payPeriod = f"{startDate} to {endDate}"



# Formulating a for Basic Pay, Overtime Pay, Absences, Honorarium, Tardiness

basicPay = ratePerHour * hoursPerDay
overtime = hoursOvertimed * ratePerHour
absences = hoursOfAbsences * ratePerHour
honorarium = noOfHours * ratePerHour
tardiness = hoursOfTardiness * ratePerHour
gross_earning = basicPay + overtime + honorarium

# Determining the Withholding Tax, SSS Contribution, and PhilHealth Contribution.

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
    sss_contrib = 360
elif 8250 <= gross_earning <= 8749.99:
    sss_contrib = 382.50
elif 8750 <= gross_earning <= 9249.99:
    sss_contrib = 405
elif 9250 <= gross_earning <= 9749.99:
    sss_contrib = 427.50
elif 9750 <= gross_earning <= 10249.99:
    sss_contrib = 450
elif 10250 <= gross_earning <= 10749.99:
    sss_contrib = 472.50
elif 10750 <= gross_earning <= 11249.99:
    sss_contrib = 495
elif 11250 <= gross_earning <= 11749.99:
    sss_contrib = 517.50
elif 11750 <= gross_earning <= 12249.99:
    sss_contrib = 540
elif 12250 <= gross_earning <= 12749.99:
    sss_contrib = 562.50
elif 12750 <= gross_earning <= 13249.99:
    sss_contrib = 585
elif 13250 <= gross_earning <= 13749.99:
    sss_contrib = 607.50
elif 13750 <= gross_earning <= 14249.99:
    sss_contrib = 630
elif 14250 <= gross_earning <= 14749.99:
    sss_contrib = 652.50
elif 14750 <= gross_earning <= 15249.99:
    sss_contrib = 675
elif 15250 <= gross_earning <= 15749.99:
    sss_contrib = 697.50
elif 15750 <= gross_earning <= 16249.99:
    sss_contrib = 720
elif 16250 <= gross_earning <= 16749.99:
    sss_contrib = 742.50
elif 16750 <= gross_earning <= 17249.99:
    sss_contrib = 765
elif 17250 <= gross_earning <= 18249.99:
    sss_contrib = 787.50
elif 17750 <= gross_earning <= 18749.99:
    sss_contrib = 810
elif 18250 <= gross_earning <= 19749.99:
    sss_contrib = 832.50
elif 18750 <= gross_earning <= 19249.99:
    sss_contrib = 855
elif 19250 <= gross_earning <= 19749.99:
    sss_contrib = 877.50
else:
    sss_contrib = 900

#statement for witholding tax
if 0 <= gross_earning <= 20832.99:
    witholding_tax = 0.00
elif 20833 <= gross_earning <= 33332:
    witholding_tax = 15% / 20833
elif 33333 <= gross_earning <= 66666:
    witholding_tax = 1875 + 20% / 33333
elif 66667 <= gross_earning <= 166666:
    witholding_tax = 8541.80 + 25% / 66667
elif 166666 <= gross_earning <= 666666:
    witholding_tax = 33541.80 + 30% / 166667
else:
    witholding_tax = 183541.80 + 35% / 666667

# Philhealth
if gross_income == 10000
    philhealth = 500
elif 10000.01 <= gross_income <= 99999.99:
    philhealth = gross_income * 0.05
elif gross_income == 100000
    philhealth = 5000


# Formulation a formula for Deductions.




# display
print("======================================================================")
print("Company Name: ", companyName)
print("Employee Code: ", employeeCode)
print("Employee Name: ", employeeName)
print("Department: ", department)
print("Salary Date Cut-Off:", salaryDateCutOff)
print("Pay Period: ", pay_period)
print("Basic Pay: ", basicPay)
print("Overtime: : ", overtime)
print("")

print("======================================================================")