# Initialization and Getting the Input Values

class CostumerInformation:
    def __init__(self):
        self.costumer_name = input("Enter Customer Name: ")
        self.address_line_1 = input("Enter House No. and Street: ")
        self.barangay = input("Enter Barangay: ")
        self.city = input("Enter City: ")
        self.municipality = input("Enter Municipality: ")
        self.account_number = int(input("Enter Account Number: "))
        self.balance = int(input("Enter Balance from Previous Billing: "))
        self.current_charges = int(input("Enter Current Charges: "))
        self.due_date = input("Enter Due Date (dd/mm/yyyy): ")
        self.rate = input("Enter Costumer Type: ")
        self.bill_date = input("Enter Billing Date (dd month yyyy): ")
        self.meter_reading_date = input("Enter Meter Reading Date (dd month yyyy): ")
        self.bill_period = input("Enter Billing Period Start (dd month yyyy): ")
        self.due_date_2 = input("Enter Due Date (dd month yyyy): ")
        self.total_kwh = int(input("Enter Total Consumption: "))
        self.next_meter_reading = input("Enter Next Meter Reading Date (dd month yyyy): ")
        self.electric_meter_number = int(input("Enter Electric Meter Number: "))
        self.current_reading = int(input("Enter Current Reading: "))
        self.previous_reading = int(input("Enter Previous Reading: "))
        self.rate_this_month = int(input("Enter the Rate for this Month per kWH: "))
        self.total_amount = ""

class BillComputationSummary:
    def __init__(self):
        print("Enter Charges for Billing Period:")
        self.generation = int(input("Generation : "))
        self.transmission = int(input("Transmission: "))
        self.system_loss = int(input("System Loss: "))
        self.distribution = int(input("Distribution: "))
        self.subsidies = int(input("Subsidies: "))
        self.government_taxes = int(input("Government Taxes: "))
        self.universal_charges = int(input("Universal Charges: "))
        self.fit_all = int(input("FIT-ALL: "))
        self


