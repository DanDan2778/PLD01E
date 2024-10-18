from ctypes.wintypes import HACCEL


class Employee:

    # initialization

    def __init__(self):

        # Getting Employee Information
        self.hmdf_contribution = 100.00
        self.company_name = input("Enter Company Name: ")
        self.emp_department = input("Enter Employee Department: ")
        self.emp_name = input("Enter Employee Name: ")
        self.emp_code = input("Enter Employee Code: ")
        self.salary_cut_off = input("Enter Cut-Off Date: ")

        # Getting Employee Earnings
        self.emp_rate_per_hour = float(input("Enter Rate per Hour: "))
        self.emp_num_of_hours_per_payday = int(input("Enter Number of Hours Worked Per PayDay: "))
        self.emp_hour_overtime = float(input("Employee Hour Overtime: "))
        self.honorarium_pay = int(input("Employee Honorarium Pay: "))
        self.emp_num_of_absences = int(input("Employee Absences: "))
        self.emp_num_tardiness = int(input("Employee Tardiness: "))


    # Computation of Employee Salary
    def emp_salary_computation(self):
        self.basic_pay = self.emp_rate_per_hour * self.emp_num_of_hours_per_payday
        self.overtime_pay = self.emp_hour_overtime * self.emp_rate_per_hour
        self.emp_gross_earnings = self.basic_pay + self.overtime_pay + self.honorarium_pay
        self.emp_absences = self.emp_num_of_absences * self.emp_rate_per_hour
        self.emp_tardiness = self.emp_num_tardiness * self.emp_rate_per_hour

    # Getting SSS Contribution

    def emp_sss_contribution(self):
        sss_brackets = [
            (0, 4249.99, 180.00),
            (4250.00, 4749.99, 202.50),
            (4750.00, 5249.99, 225.00),
            (5250.00, 5749.99, 247.50),
            (5750.00, 6249.99, 270.00),
            (6250.00, 6749.99, 292.50),
            (6750.00, 7249.99, 315.00),
            (7250.00, 7749.99, 337.50),
            (7750.00, 8249.99, 360.00),
            (8250.00, 8749.99, 382.50),
            (8750.00, 9249.99, 405.00),
            (9250.00, 9749.99, 427.50),
            (9750.00, 10249.99, 450.00),
            (10250.00, 10749.99, 472.50),
            (10750.00, 11249.99, 495.00),
            (11250.00, 11749.99, 517.50),
            (11750.00, 12249.99, 540.00),
            (12250.00, 12749.99, 562.50),
            (12750.00, 13249.99, 585.00),
            (13250.00, 13749.99, 607.50),
            (13750.00, 14249.99, 630.00),
            (14250.00, 14749.99, 652.50),
            (14750.00, 15249.99, 675.00),
            (15250.00, 15749.99, 697.50),
            (15750.00, 16249.99, 720.00),
            (16250.00, 16749.99, 742.50),
            (16750.00, 17249.99, 765.00),
            (17250.00, 17749.99, 787.50),
            (17750.00, 18249.99, 810.00),
            (18250.00, 18749.99, 832.50),
            (18750.00, 19249.99, 855.00),
            (19250.00, 19749.99, 877.50),
            (19750.00, float('inf'), 900.00)
        ]
        
        self.sss_contribution = 0.00

        for lower_bound, upper_bound, contribution in sss_brackets:
            if lower_bound <= self.emp_gross_earnings <= upper_bound:
                self.sss_contribution = contribution
                return self.sss_contribution

    # Getting PhilHealth Contribution
    def emp_philhealth_contribution(self):
        if self.emp_gross_earnings < 10000:
            self.philhealth_contribution = 0.00
        else:
            self.philhealth_contribution = self.emp_gross_earnings * 0.0450
        
        return self.philhealth_contribution

    # Getting Tax Contribution
    def emp_tax_contribution(self):
        tax_brackets = [
            (0, 20832.00, 0.00, 0.00),
            (20833.00, 33332.00, 0.20, 20833.00),
            (33333.00, 66666.00, 0.25, 33333.00),
            (66667.00, 166666.00, 0.30, 66667.00),
            (166667.00, 666666.00, 0.32, 166667.00),
            (666667.00, float('inf'), 0.35, 666667.00)
        ]

        self.tax_contribution = 0.00

        for lower_bound, upper_bound, rate, base_tax in tax_brackets:
            if lower_bound <= self.emp_gross_earnings <= upper_bound:
                self.tax_contribution = (self.emp_gross_earnings - base_tax) * rate
                return self.tax_contribution


    # Formula to get the total deduction
    def emp_total_deduction(self):
        self.deduction = self.emp_absences + self.emp_tardiness + self.tax_contribution + self.sss_contribution + self.philhealth_contribution + self.hmdf_contribution

    # Formula to get the net pay
    def emp_employee_netpay(self):
        self.net_pay = self.emp_gross_earnings - self.deduction
    
    # Display Employee Information
    def emp_displayEmployee(self):
        print("\n\n\n\n=====================================")
        print("Company Name: ", self.company_name)
        print("Employee Department: ", self.emp_department)
        print("=====================================")
        print("Employee Name: ", self.emp_name)
        print("Employee Code: ", self.emp_code)
        print("Cut-Off Date: ", self.salary_cut_off)
        print("=====================================")
        print("Basic pay: %.2f" % self.basic_pay)
        print("Overtime Pay: %.2f" % self.overtime_pay)
        print("Honorarium Pay: %.2f" % self.honorarium_pay)
        print("Gross Income: %.2f" % self.emp_gross_earnings)
        print("Absences: %.2f" % self.emp_absences)
        print("Tardiness: %.2f " % self.emp_tardiness)
        print("=====================================")
        print("SSS Contribution: %.2f" % self.sss_contribution)
        print("Tax Contribution: %.2f" % self.tax_contribution)
        print("Philhealth Contribution: %.2f" % self.philhealth_contribution)
        print("HMDF Contribution: %.2f" % self.hmdf_contribution)
        print("=====================================")
        print("Total Deduction: %.2f" % self.deduction)
        print("Net Pay: %.2f" % self.net_pay)
        print("\n=====================================\n")

emp1 = Employee()
emp1.emp_salary_computation()
emp1.emp_sss_contribution()
emp1.emp_philhealth_contribution()
emp1.emp_tax_contribution()
emp1.emp_total_deduction()
emp1.emp_employee_netpay()
emp1.emp_displayEmployee()