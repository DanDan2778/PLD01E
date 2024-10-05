class Employee:
    hdmf = 100

    # Initialization or constructor method of
    def __init__(self):
        # class employee
        self.hmdf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.employee_department = input("Enter Employee Department: ")
        self.employee_name = input("Enter Employee Name: ")
        self.employee_code = input("Employee Code: ")
        self.salary_cut_off = input("Enter Cut-Off Date: ")

        # Input for Salary Computation

        self.emp_rate_per_hour = float(input("Employee Rate Per Hour: "))
        self.emp_num_of_hours_per_payday = int(input("Employee's Number of Hours Worked Per Payday: "))
        self.emp_hour_overtime = float(input("Employee Hour Overtime: "))
        self.honorarium_pay = int(input("Employee Honorarium Pay: "))
        self.emp_num_of_absences = int(input("Employee Absences: "))
        self.emp_num_tardiness = int(input("Employee Tardiness: "))

    def emp_salary_computation(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday
        self.overtime_pay = self.emp_hour_overtime * self.emp_rate_per_hour
        self.emp_gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium_pay
        self.emp_absences = self.emp_num_of_absences * self.emp_rate_per_hour
        self.emp_tardiness = self.emp_num_tardiness * self.emp_rate_per_hour

    def emp_sss_contribution(self):
        if self.emp_gross_earnings < 0:
            self.sss_contribution = 0.00
        elif self.emp_gross_earnings >= 0 and self.emp_gross_earnings < 4250.00:
            self.sss_contribution = 180.00
        elif self.emp_gross_earnings >= 4251 and self.emp_gross_earnings < 4749.99:
            self.sss_contribution = 202.50
        elif self.emp_gross_earnings >= 4750.00 and self.emp_gross_earnings < 5249.99:
            self.sss_contribution = 225.00
        elif self.emp_gross_earnings >= 5250 and self.emp_gross_earnings < 5749.99:
            self.sss_contribution = 247.50
        elif self.emp_gross_earnings >= 5750 and self.emp_gross_earnings < 6249.99:
            self.sss_contribution = 270.00
        elif self.emp_gross_earnings >= 6250.00 and self.emp_gross_earnings < 6749.99:
            self.sss_contribution = 292.50
        elif self.emp_gross_earnings >= 6750.00 and self.emp_gross_earnings < 7249.99:
            self.sss_contribution = 315.00
        elif self.emp_gross_earnings >= 7250.00 and self.emp_gross_earnings < 7749.99:
            self.sss_contribution = 337.50
        elif self.emp_gross_earnings >= 7750.00 and self.emp_gross_earnings < 8249.99:
            self.sss_contribution = 360.00
        elif self.emp_gross_earnings >= 8250.00 and self.emp_gross_earnings < 8749.99:
            self.sss_contribution = 382.50
        elif self.emp_gross_earnings >= 8750.00 and self.emp_gross_earnings < 9249.99:
            self.sss_contribution = 405.00
        elif self.emp_gross_earnings >= 9250.00 and self.emp_gross_earnings < 9749.99:
            self.sss_contribution = 427.50
        elif self.emp_gross_earnings >= 9750.00 and self.emp_gross_earnings < 10249.99:
            self.sss_contribution = 450.00
        elif self.emp_gross_earnings >= 10250.00 and self.emp_gross_earnings < 10749.99:
            self.sss_contribution = 472.50
        elif self.emp_gross_earnings >= 10750.00 and self.emp_gross_earnings < 11249.00:
            self.sss_contribution = 495.00
        elif self.emp_gross_earnings >= 11250.00 and self.emp_gross_earnings < 11749.99:
            self.sss_contribution = 517.50
        elif self.emp_gross_earnings >= 11750.00 and self.emp_gross_earnings < 12249.99:
            self.sss_contribution = 540.00
        elif self.emp_gross_earnings >= 12250.00 and self.emp_gross_earnings < 12749.99:
            self.sss_contribution = 562.50
        elif self.emp_gross_earnings >= 12750.00 and self.emp_gross_earnings < 13249.99:
            self.sss_contribution = 585.00
        elif self.emp_gross_earnings >= 13250.00 and self.emp_gross_earnings < 13749.00:
            self.sss_contribution = 607.50
        elif self.emp_gross_earnings >= 13750.00 and self.emp_gross_earnings < 14249.99:
            self.sss_contribution = 630.00
        elif self.emp_gross_earnings >= 14250.00 and self.emp_gross_earnings < 14749.99:
            self.sss_contribution = 652.50
        elif self.emp_gross_earnings >= 14750.00 and self.emp_gross_earnings < 15249.99:
            self.sss_contribution = 675.00
        elif self.emp_gross_earnings >= 15250.00 and self.emp_gross_earnings < 15749.99:
            self.sss_contribution = 697.50
        elif self.emp_gross_earnings >= 15750.00 and self.emp_gross_earnings < 16249.99:
            self.sss_contribution = 720.00
        elif self.emp_gross_earnings >= 16250.00 and self.emp_gross_earnings < 16749.99:
            self.sss_contribution = 742.50
        elif self.emp_gross_earnings >= 16750.00 and self.emp_gross_earnings < 17249.99:
            self.sss_contribution = 765.00
        elif self.emp_gross_earnings >= 17250.00 and self.emp_gross_earnings < 17749.99:
            self.sss_contribution = 787.50
        elif self.emp_gross_earnings >= 17750.00 and self.emp_gross_earnings < 18249.99:
            self.sss_contribution = 810.00
        elif self.emp_gross_earnings >= 18250.00 and self.emp_gross_earnings < 18749.99:
            self.sss_contribution = 832.50
        elif self.emp_gross_earnings >= 18750.00 and self.emp_gross_earnings < 19249.99:
            self.sss_contribution = 855.00
        elif self.emp_gross_earnings >= 19250.00 and self.emp_gross_earnings < 19749.99:
            self.sss_contribution = 877.50
        elif self.emp_gross_earnings >= 19750.00 and self.emp_gross_earnings < 20249.99:
            self.sss_contribution = 877.50
        else:
            self.sss_contribution = 900.00

    def emp_philhealth_contribution(self):
        # Setting conditions in getting Philhealth Contributions
        if self.emp_gross_earnings < 10000:
            self.philhealth_contribution = 0.00
        else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450


    def emp_tax_contribution(self):
        if self.emp_gross_earnings < 10417:
            self.tax_contribution = 0.00
        elif self.emp_gross_earnings >= 10417 and self.emp_gross_earnings <= 16666:
            self.tax_contribution = ((self.emp_gross_earnings - 10417) * 0.15 + 0.00)
        elif self.emp_gross_earnings >= 16667 and self.emp_gross_earnings <= 33332:
            self.tax_contribution = ((self.emp_gross_earnings - 16667) * 0.20 + 937.50)
        elif self.emp_gross_earnings >= 33333 and self.emp_gross_earnings <= 83332:
            self.tax_contribution = ((self.emp_gross_earnings - 33333) * 0.25 +4270.70)
        elif self.emp_gross_earnings >= 83333 and self.emp_gross_earnings <= 333332:
            self.tax_contribution = ((self.emp_gross_earnings - 83333) * 0.30 + 16770.70)
        else:
            self.tax_contribution = ((self.emp_gross_earnings - 333333) * 0.35 +91770.70)

    def emp_total_deduction(self):
        self.deduction = self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution + self.philhealth_contribution + self.hmdf_contribution

    def emp_employee_netpay(self):
        self.net_pay = self.emp_gross_earnings - self.deduction

    def emp_displayEmployee(self):
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.employee_department)
        print("Employee Name: ", self.employee_name)
        print("Employee Code: ", self.employee_code)
        print("Cut-Off Date: ", self.salary_cut_off)
        print("Basic pay: %.2f" % self.basic_pay)
        print("Overtime Pay: %.2f" % self.overtime_pay)
        print("Gross Income: %.2f" % self.emp_gross_earnings)
        print("Absences: %.2f" % self.emp_absences)
        print("Tardiness: %.2f " % self.emp_tardiness)
        print("SSS Contribution: %.2f" % self.sss_contribution)
        print("Philhealt Contribution: %.2f" % self.philhealth_contribution)
        print("Total Deduction: %.2f" % self.deduction)
        print("Net Pay: %.2f" % self.net_pay)

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_netpay()
emp1.emp_displayEmployee()
