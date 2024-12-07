import midterm_exam

service = midterm_exam.ServiceInformation()
service.customers_data()
meter = midterm_exam.MeteringInformation()

def display_receipt():
        print("\n" * 3)
        # Displaying Service Information
        print(f"{"STATEMENT OF ACCOUNT":^{75}}")
        print(f"{"For the Month of: February 2024":^{75}}\n")
        print(f"{"SERVICE INFORMATION":^{75}}")
        print(f"{"CONTRACT ACCOUNT NUMBER: ":<{30}}{service.account_number}")
        print(f"{"Account Name: ":<{30}}{service.account_name}")
        print(f"{"TIN":<{30}}{service.tin}")
        print(f"{"Rate Class: ":<{30}}{service.rate_class}")
        print(f"{"Business Area: ":<{30}}{service.business_area}")
        print("-" * 75)
        # Displaying Metering Information
        print(f"{"METERING INFORMATION":^{75}}")
        # 20, 27, 28
        print(f"{"Meter No.":<{20}}{"MRU No.":<{27}}{"Seq. No.":<{28}}")
        print(f"{meter.meter_number:<{20}}{meter.mru:<{27}}{meter.seq_number:<{28}}\n")
        print(f"{"Reading Date: ":<{30}}{meter.reading_date}")
        print(f"{"Present Reading: ":<{30}}{meter.present_reading}")
        print(f"{"Previous Reading: ":<{30}}{meter.previous_reading}")
        print(f"{"Consumption: ":<{30}}{meter.consumption}\n")
        print(f"{"Previous 3 Months":^{18}}")
        print(f"{"Consumption":^{18}}")
        print("-" * 75)

        # Displaying Bill and Payment History
        # 10, 27, 27, 11
        print("\n")
        print(f"{"BILL AND PAYMENT HISTORY":^{75}}")
        print(f"{"Desc":<{10}}{"Total Amount":<{27}}{"OR#":<{27}}{"Date":<{11}}")
        print("\nDescription: WB-Water Bill, GD-Guarantee Deposit, MISC-Reopening Fee, ")
        print("Connection Fee, Metering Charge")
        print("-" * 75)

        # Displaying Summary
        print(f"{"BILLING PERIOD:":<{15}}{meter.start_billing_period:<{15}}TO {meter.reading_date:<{15}}")
        print(f"{"CURRENT CHARGES":<{30}}{meter.total_charge_with_tax:>{10}}")
        print(f"{"Basic Charge: ":<{30}}{meter.basic_charge}")
        print(f"{"Environmental Charge: ":<{30}}{meter.environmental_charge}")
        print(f"{"Maintenance Service Charge (MSC): ":<{30}}{meter.maintenance_service_charge}")
        print(f"{"Total Charge without Tax: ":<{30}}{meter.total_charge_without_tax}")
        print(f"{"Government Tax: ":<{30}}{meter.government_tax}")
        print("\n" * 2)
        print("-" * 75)
        print(f"{"TOTAL AMOUNT DUE":<{64}}PHP {meter.total_charge_with_tax:<{11}}")
        print(f"{"PAYMENT DUE DATE:":<{60}}{meter.due_date:<{15}}")
        print("-" * 75)
        print("Please examine your bill carefully. If no complaint is made within 60 days")
        print("of receipt, the bill is considered true and correct.")
        print("-" * 75)
        print('"THIS DOCUMENT IS NOT VALID FOR CLAIM OF INPUT TAX."')
        print("-" * 75)
        print("FOR INQUIRIES AND CONCERNS OF SANITATION, PLEASE CALL:")
        print("MAYNILAD HOTLINE 1826 (METRO MANILA) AND 1800-1000-92837 (CAVITE AREA)")
        print("ONLY")
        print("-" * 75)
        print(f"{" ":<{45}}{"PAYMENT CENTER / BANK COPY":>{30}}")
        print(f"{"Contract Account No. : ":<{25}}{service.account_number:<{20}}{"Amount Due PHP":<{15}}{meter.total_charge_with_tax:<{15}}")
        print(f"{"Account Name: ":<{15}}{service.account_name:<{15}}{"   BILLING PERIOD:":<{15}}{meter.start_billing_period:<{11}}TO {meter.reading_date:<{15}}")
        print("\n" * 3)




display_receipt()