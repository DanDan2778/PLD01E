class Employee_Info:
    def __init__(self):
        self.company_name = ""
        self.emp_department = ""
        self.emp_name = ""
        self.emp_code = ""
        self.salary_cut_off = ""

    def get_emp_data(self, company_name, emp_department, emp_name, emp_code, salary_cut_off):
        self.company_name = company_name
        self.emp_department = emp_department
        self.emp_name = emp_name
        self.emp_code = emp_code
        self.salary_cut_off = salary_cut_off

    def desiplay_data(self):
        print("Company Name: ", self.company_name)
        print("Employee Department", self.emp_department)
        print("Employee Name: ", self.emp_name)
        print("Employee Code: ", self.emp_code)
        print("Cut-Off Date: ", self.salary_cut_off)

class Employee_Salary:
    def __init__(self):
        self.sss_contribution = 0.00
        self.hdmf_contribution = 100.00
        self.philhealth_contribution = 0.00
        self.tax_contribution = 0.00
        self.emp_absences = 0.00
        self.tardiness = 0.00
        self.total_deduction = 0.00
        self.emp_rate_per_hour = 0.00
        self.emp_num_of_hours_per_payday = 0.00
        self.hour_overtime = 0.00
        self.basic_pay = 0.00
        self.honorarium_pay = 0.00
        self.emp_num_of_absences = 0.00
        self.tardiness_deduction = 0.00
        self.tardiness_num_hours = 0
        self.emp_gross_earnings = 0.00
        self.emp_net_income = 0.00

    def get_total_deductions(self, sss_contribution, philhealth_contribution, tax_contribution, emp_absences, emp_tardiness):
        self.total_deduction = sss_contribution + philhealth_contribution + tax_contribution + emp_absences + emp_tardiness
        return self.total_deduction

    def get_basic_pay(self, emp_rate_per_hour, emp_num_of_hours_per_payday):
        self.basicpay = emp_rate_per_hour * emp_num_of_hours_per_payday
        return self.basicpay

    def get_absences_deduction(self, emp_rate_per_hour, emp_num_of_absences):
        self.emp_absences = emp_num_of_absences * emp_rate_per_hour
        return self.emp_absences

    def get_overtime_pay(self, emp_hour_overtime, emp_rate_per_hour):
        self.emp_overtime_pay = emp_hour_overtime * emp_rate_per_hour
        return self.emp_overtime_pay

    def get_tardiness_deduction(self, emp_rate_per_hour, tardiness_num_hours):
        self.tardiness_deduction = tardiness_num_hours * emp_rate_per_hour
        return self.tardiness_deduction


