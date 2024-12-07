class CostumerInformation:
    # Initialization of the CostumerInformation Class
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
    # Initialization of the BillComputationSummary Class
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
    # Initialization of the DisplayBill Class
    def __init__(self, costumer, bill):
        self.costumer_name = costumer.costumer_name
        self.address_line_1 = costumer.address_line_1
        self.barangay = costumer.barangay
        self.city = costumer.city
        self.municipality = costumer.municipality
        self.account_number = costumer.account_number
        self.balance = costumer.balance
        self.due_date = costumer.due_date
        self.rate = costumer.rate_this_month
        self.bill_date = costumer.bill_date
        self.bill_period = costumer.bill_period
        self.meter_reading_date = costumer.meter_reading_date
        self.next_meter_reading = costumer.next_meter_reading
        self.electric_meter_number = costumer.electric_meter_number
        self.current_reading = costumer.current_reading
        self.previous_rea
        1ding = costumer.previous_reading
        self.total_kwh = costumer.total_kwh
        self.current_charges = costumer.total_amount
        self.amount_due = costumer.total_amount
        self.total_amount_due = self.amount_due + self.balance + bill.total_amount_due
        self.costumer_type = costumer.rate
        self.generation = bill.generation
        self.transmission = bill.transmission
        self.system_loss = bill.system_loss
        self.distribution = bill.distribution
        self.subsidies = bill.subsidies
        self.government_taxes = bill.government_taxes
        self.universal_charges = bill.universal_charges
        self.fit_all = bill.fit_all
        self.applied_credits = bill.applied_credits
        self.other_charges = bill.other_charges
        self.installment = bill.installment

    #  Display the Costumer Information
    def display_costumer_info(self):
        print("\n" * 3)
        print(self.costumer_name)
        print(self.address_line_1)
        print(self.barangay)
        print(self.city)
        print(self.municipality)
        print("-" * 75)
        print("ELECTRIC BILL")
        print("Account Number: ", self.account_number)
        print("Balance from Previous Billing: ", self.balance)
        print("Current Charges:", self.current_charges)
        print("Due Date:", self.due_date)
        print("Total Amount Due:", self.total_amount_due)
        print("-" * 75)
        print("Service Info")
        print("-" * 75)
        print("Service ID Number: ", self.account_number)
        print("Rate: ", self.rate)
        print("Bill Date:", self.bill_date)
        print("Contract in the name of: ", self.costumer_name)
        print("Service Address: ", self.address_line_1, self.barangay, self.city)
        print(self.municipality)
        print("-" * 75)
        print("")
        print("")
        print("")
        print("-" * 75)
        print("Billing Period: ", self.bill_period, "to", self.bill_date)
        print("Billing Date: ", self.bill_date)
        print("Date of Meter Reading: ", self.meter_reading_date)
        print("Date of Next Meter Reading: ", self.next_meter_reading)
        print("Customer Type:", self.costumer_type)
        print("Electric Meter Number: ", self.electric_meter_number)
        print("Current Reading: ", self.current_reading)
        print("Previous Reading: ", self.previous_reading)
        print("Actual Consumption: ", self.total_kwh)
        print("-" * 75)
        print("Please Pay: ", self.total_amount_due)
        print("-" * 75)
        print("Bill Computation Summary")
        print("Remaining Balance: ", self.balance)
        print("Charges for this Billing Period: ", self.current_charges)
        print("Generation: ", self.generation)
        print("Transmission: ", self.transmission)
        print("System Loss: ", self.system_loss)
        print("Distribution: ", self.distribution)
        print("Subsidies: ", self.subsidies)
        print("Government Taxes: ", self.government_taxes)
        print("Universal Charges: ", self.universal_charges)
        print("FIT-ALL (renewable): ", self.fit_all)
        print("Applied Credits: ", self.applied_credits)
        print("Other Charges: ", self.other_charges)
        print("Installment: ", self.installment)
        print("-" * 75)
        print("Total Amount Due: ", self.total_amount_due)
        print("-" * 75)


# Main Program
customer = CostumerInformation()
bill = BillComputationSummary()
display = DisplayBill(customer, bill)
display.display_costumer_info()

