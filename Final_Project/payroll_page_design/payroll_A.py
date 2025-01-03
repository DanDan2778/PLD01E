import gui_design as gui



class payroll:
    def __init__(self, window):
        self.window = window
        self.add_y = 10
        self.x_label = 380

        self.gui = gui.GuiDesign(window)
        self.image = 'C:\\Users\\danie\\Desktop\\repository\\PLD01E\\Laboratory 6\\profile.jpg'

    def header(self):
        self.gui.frames(15, 25, 670, 850, 'white')
        #profile picture
        self.gui.image_design(self.image, 40, 70, 200, 200)
        self.gui.title_design(200, 10, 'LPU-C CHOICE PAYROLL', 20)
    def basic_info(self):
    # Windows Right Side
    # Basic Information
        self.gui.title_design(39, 45, 'Employee Basic Info', 13)

        x_textbox = 540
        # First Name
        self.gui.label_design(self.x_label, 80, 'First Name: ')
        self.gui.textbox_design_disabled(x_textbox, 70+self.add_y, '')
        # Last Name
        self.gui.label_design(self.x_label, 110, 'Last Name: ')
        self.gui.textbox_design_disabled(540, 110, '')
        # Middle Name
        self.gui.label_design(self.x_label, 140, 'Middle Name: ')
        self.gui.textbox_design_disabled(540, 140,'')
        # City Status
        self.gui.label_design(self.x_label, 170, 'Civil Status: ')
        self.gui.textbox_design_disabled(540, 170, '')
        # Qualified Dependent Status
        self.gui.label_design(self.x_label, 205, 'Qualified Dependent ')
        self.gui.label_design(self.x_label, 235, 'Status: ')
        self.gui.textbox_design1(540, 205)
        # Paydate
        self.gui.label_design(self.x_label, 260, 'Paydate: ')
        self.gui.textbox_design1(540, 260)
        # Employee Status
        self.gui.label_design(self.x_label, 290, 'Employee Status: ')
        self.gui.textbox_design_disabled(540, 290, '')
        # Designation
        self.gui.label_design(self.x_label, 320, 'Designation: ')
        self.gui.textbox_design_disabled(540, 320, '')

    def deductions(self):
        # Regular Deductions
        self.gui.title_design(350, 370, 'Regular Deductions', 13)
        # SSS
        self.gui.label_design(self.x_label, 410, 'SSS Contribution: ')
        self.gui.textbox_design_disabled(540, 410,' ')
        # PhilHealth
        self.gui.label_design(self.x_label, 440, 'PhilHealth Contribution: ')
        self.gui.textbox_design_disabled(540, 440, '')
        # Pag-IBIG
        self.gui.label_design(self.x_label, 470, 'Pag-IBIG Contribution: ')
        self.gui.textbox_design_disabled(540, 470, '')
        # Tax
        self.gui.label_design(self.x_label, 500, 'Income Tax Contribution: ')
        self.gui.textbox_design_disabled(540, 500, '')

    def other_deductions(self):
        # Other Deductions
        self.gui.title_design(350, 530, 'Other Deductions', 13)
        # SSS Loan
        self.gui.label_design(self.x_label, 560, 'SSS Loan: ')
        self.gui.textbox_design1(540, 560)
        # Pag-IBIG Loan
        self.gui.label_design(self.x_label, 590, 'Pag-IBIG Loan: ')
        self.gui.textbox_design1(540, 590)
        # Faculty Savings Deposit
        self.gui.label_design(self.x_label, 620, 'Faculty Savings Deposit: ')
        self.gui.textbox_design1(540, 620)
        # Faculty Savings Loan
        self.gui.label_design(self.x_label, 650, 'Faculty Savings Loan: ')
        self.gui.textbox_design1(540, 650)
        # Salary Loan
        self.gui.label_design(self.x_label, 680, 'Salary Loan: ')
        self.gui.textbox_design1(540, 680)
        # Other Loans
        self.gui.label_design(self.x_label, 710, 'Other Loans: ')
        self.gui.textbox_design1(540, 710)

    def deduction_summary(self):
        # DEDUCTION SUMMARY
        self.gui.title_design(350, 740, 'DEDUCTION SUMMARY', 13)
        # Total Deductions
        self.gui.label_design(self.x_label, 780, 'Total Deductions: ')
        self.gui.textbox_design_disabled(540, 780, '')
        # Button for Gross Income, Net Income, Save, Update and New
        width = 7
        pady = 2
        y = 800 + 12
        self.gui.button_design(360, y, 'Gross Income', '#000FFF', 'white', 'blue', 2., 10, pady)
        self.gui.button_design(445, y, 'Net Income', '#000FFF', 'white', 'blue', 2, 9, pady)
        self.gui.button_design(523, y, 'Save', '#5499c7', 'white', 'blue', 2, 4, pady)
        self.gui.button_design(567, y, 'Update', '#5499c7', 'white', 'blue', 2, 6, pady)
        self.gui.button_design(625, y, 'New', '#f4d03f', 'white', 'blue', 1, 4, pady)


        # Windows Left Side
        x_textbox_left = 180
        # Employee Number
        self.gui.label_design(40, 280, 'Employee Number: ')
        self.gui.textbox_design1(x_textbox_left, 280)
        # Search Employee with button
        self.gui.label_design(40, 310, 'Search Employee: ')
        self.gui.button_design(x_textbox_left, 307, 'Search', 'red', 'white', 'blue', 2, 10, 2)
        # Department
        self.gui.label_design(40, 340, 'Department: ')
        self.gui.textbox_design_disabled(x_textbox_left, 340, '')
        # Basic Income
        self.gui.title_design(20, 370, 'Basic Income', 13)
        # rate per hour y = 490
        self.gui.label_design(40, 410, 'Rate per Hour: ')
        self.gui.textbox_design1(x_textbox_left, 410)
        # no. of hours / cut off
        self.gui.label_design(40, 440, 'No. of Hours / Cut Off: ')
        self.gui.textbox_design1(x_textbox_left, 440)
        # income / cut off
        self.gui.label_design(40, 470, 'Income / Cut Off: ')
        self.gui.textbox_design_disabled(x_textbox_left, 470, '')
        # Honorarium Income
        self.gui.title_design(20, 500, 'Honorarium Income', 13)
        # Rate per hour
        self.gui.label_design(40, 550, 'Rate per Hour: ')
        self.gui.textbox_design1(x_textbox_left, 550)
        # No. of hours / cut off
        self.gui.label_design(40, 580, 'No. of Hours / Cut Off: ')
        self.gui.textbox_design1(x_textbox_left, 580)
        # Income / Cut Off
        self.gui.label_design(40, 610, 'Income / Cut Off: ')
        self.gui.textbox_design_disabled(x_textbox_left, 610, '')
        """Continue From Here"""
        # Other Income
        self.gui.title_design(20, 640, 'Other Income', 13)
        # Rate per hour
        self.gui.label_design(40, 680, 'Rate per Hour: ')
        self.gui.textbox_design1(x_textbox_left, 680)
        # Income / Cut Off
        self.gui.label_design(40, 710, 'Income / Cut Off: ')
        self.gui.textbox_design_disabled(x_textbox_left, 710, '')
        # Summary Income
        self.gui.title_design(20, 740, 'Summary Income', 13)
        # Gross Income
        self.gui.label_design(40, 780, 'Gross Income: ')
        self.gui.textbox_design_disabled(x_textbox_left, 780, '')
        # Net Income
        self.gui.label_design(40, 810, 'Net Income: ')
        self.gui.textbox_design_disabled(x_textbox_left, 810, '')

