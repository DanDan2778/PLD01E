# Initialization and Getting the Input Values
output_width = 100
description_width = 15
value_width = 10

class CostumerInformation:
    def __init__(self):
        self.costumer_name = input("Enter Customer Name: ")
        self.address_line_1 = input("Enter House No. and Street: ")
        self.barangay = input("Enter Barangay: ")
        self.city = input("Enter City: ")
        self.municipality = input("Enter Municipality: ")
        self.account_number = input("Enter Account Number: ")
        self.balance = float(input("Enter Balance from Previous Billing: "))
        self.due_date = input("Enter Due Date (dd/mm/yyyy): ")
        self.rate = input("Enter Costumer Type: ")
        self.bill_date = input("Enter Billing Date (dd month yyyy): ")
        self.meter_reading_date = input("Enter Meter Reading Date (dd month yyyy): ")
        self.bill_period = input("Enter Billing Period Start (dd month yyyy): ")
        self.due_date_2 = input("Enter Due Date (dd month yyyy): ")
        self.total_kwh = float(input("Enter Total Consumption: "))
        self.next_meter_reading = input("Enter Next Meter Reading Date (dd month yyyy): ")
        self.electric_meter_number = float(input("Enter Electric Meter Number: "))
        self.current_reading = float(input("Enter Current Reading: "))
        self.previous_reading = float(input("Enter Previous Reading: "))
        self.rate_this_month = float(input("Enter the Rate for this Month per kWH: "))
        self.total_amount = self.total_kwh * self.rate_this_month

class BillComputationSummary:
    def __init__(self):
        print("Enter Additional Charges: ")
        self.generation = float(input("Generation : "))
        self.transmission = float(input("Transmission: "))
        self.system_loss = float(input("System Loss: "))
        self.distribution = float(input("Distribution: "))
        self.subsidies = float(input("Subsidies: "))
        self.government_taxes = float(input("Government Taxes: "))
        self.universal_charges = float(input("Universal Charges: "))
        self.fit_all = float(input("FIT-ALL (renewable): "))
        self.applied_credits = float(input("Applied Credits: "))
        self.other_charges = float(input("Other Charges: "))
        self.installment = float(input("Installment: "))
        self.total_amount_due = self.generation + self.transmission + self.system_loss + self.distribution + self.subsidies + self.government_taxes + self.universal_charges + self.fit_all + self.applied_credits + self.other_charges

class DisplayBill:
    def __init__(self, costumer, bill):
        self.costumer_name = costumer.costumer_name
        self.address_line_1 = costumer.address_line_1
        self.barangay = costumer.barangay
        self.city = costumer.city
        self.municipality = costumer.municipality
        self.account_number = costumer.account_number
        

    def display_costumer_info(self):
        print("\n" * 3)
        print(self.costumer_name)
        print(self.address_line_1)
        print(self.barangay)
        print(self.city)
        print(self.municipality)
        print(f"{"ELECTRIC BILL":^{output_width}}")
        print(f"|{"-" * 98}|")
        print(f"|{'Summary for Customer Account Number (CAN)':<{50}}{self.account_number:<{48}}|")
        print(f"|{"-" * 98}|")
        print(f"|{'Balance from Previous Billing':^{49}}|{'Current Charges':^{24}}|{'Total Amount Due':^{24}}")

        

customer = CostumerInformation()
bill = BillComputationSummary()
display = DisplayBill(customer, bill)
display.display_costumer_info()
