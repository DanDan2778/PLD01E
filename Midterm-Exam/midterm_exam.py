# Service Information Class
class ServiceInformation:
    def __init__(self):
        self.account_number = input("Enter Contract Account Number (CAN): ")
        self.account_name = input("Enter Account Name: ")
        self.service_address = input("Enter Service Address: ")
        self.tin = input("Enter TIN ###-###-###-###: ")
        self.rate_class = input("Enter Rate Class: ")
        self.account_balance = 0
        self.business_area = input("Enter Business Area: ")
    def customers_data(self):

        # customer informations
        if self.account_number == 12345678:
            self.service_address = "890 BLUE ST TUNASA2 MUNTINLUPA"
            self.account_balance = 1000
        elif self.account_number == 8654321:
            self.service_address == "123 RED ST TUNASA1 MUNTINLUPA"
            self.account_balance = 2000

class MeteringInformation:
    def __init__(self):
        self.meter_number = input("Enter Meter Number: ")
        self.mru = input("Enter MRU: ")
        self.seq_number = input("Enter Sequence Number: ")
        self.reading_date = input("Enter Reading Date (mm/dd/yyyy): ")
        self.start_billing_period = input("Enter Start Billing Period (mm/dd/yyyy): ")
        self.due_date = input("Enter Due Date (mm/dd/yyyy): ")
        self.present_reading = float(input("Enter Present Reading: "))
        self.previous_reading = float(input("Enter Previous Reading: "))
        self.consumption = (self.present_reading) - (self.previous_reading)
        self.basic_charge = 23.52 * self.consumption
        self.environmental_charge = 0.2 * self.basic_charge
        self.maintenance_service_charge = 1.53
        self.total_charge_without_tax = self.basic_charge + self.environmental_charge + self.maintenance_service_charge
        self.government_tax = self.total_charge_without_tax * 0.025
        self.total_charge_with_tax = self.total_charge_without_tax + self.government_tax

        self.environmental_charge = f"{self.environmental_charge:.2f}"