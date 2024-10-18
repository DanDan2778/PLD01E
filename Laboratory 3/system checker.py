class Employee:
    def __init__(self, emp_gross_earnings):
        self.emp_gross_earnings = emp_gross_earnings
        self.sss_contribution = 0.00

    # Define a list of tuples containing the income ranges and corresponding SSS contributions
    income_ranges = [
        (0, 4250, 180.00),
        (4251, 4749.99, 202.50),
        (4750, 5249.99, 225.00),
        (5250, 5749.99, 247.50),
        (5720, 6249.99, 270.00),
        (6250, 6749.99, 292.50),
        (6750, 7249.99, 315.00),
        (7250, 7749.99, 337.50),
        (7750, 8249.99, 360.00),
        (8250, 8749.99, 382.50),
        (8750, 9249.99, 405.00),
        (9250, 9749.99, 427.50),
        (9750, 10249.99, 450.00),
        (10250, 10749.99, 472.50),
        (10750, 11249.99, 495.00),
        (11250, 11749.99, 517.50),
        (11750, 12249.99, 540.00),
        (12250, 12749.99, 562.50),
        (12750, 13249.99, 585.00),
        (13250, 13749.99, 607.50),
        (13750, 14249.99, 630.00),
        (14250, 14749.99, 652.50),
        (14750, 15249.99, 675.00),
        (15250, 15749.99, 697.50),
        (15750, 16249.99, 720.00),
        (16250, 16749.99, 742.50),
        (16705, 17249.99, 765.00),
        (17250, 17749.99, 787.50),
        (17750, 18249.99, 810.00),
        (18250, 18749.99, 832.50),
        (18750, 19249.99, 855.00),
        (19250, 19749.99, 877.50),
        (19750, 20249.99, 900.00),
        (20250, 20749.99, 900.00),
        (20750, 21249.99, 900.00),
        (21250, 21749.99, 900.00),
        (21750, 22249.99, 900.00),
        (22250, 22749.99, 900.00),
        (22750, 23249.99, 900.00),
        (23250, 23749.99, 900.00),
        (23750, 24249.99, 900.00),
        (24250, float('inf'), 900.00)

        # Handle cases where income is above 24250
    ]

    def calculate_sss_contribution(self):
        """Calculate the SSS contribution based on gross earnings."""
        for low, high, contribution in self.income_ranges:
            if low <= self.emp_gross_earnings <= high:
                self.sss_contribution = contribution
                return self.sss_contribution
        return 0.00  # Default contribution if income is not in any range

    def display_contribution(self):
        """Display the calculated SSS contribution."""
        print(f"Gross Earnings: {self.emp_gross_earnings}, SSS Contribution: {self.sss_contribution}")

# SSS Contribution:
emp = Employee(50000)
emp.calculate_sss_contribution()
emp.display_contribution()