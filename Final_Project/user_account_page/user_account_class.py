import gui_design as gui

class UserAccountPage:
    def __init__(self, window):
        self.window = window
        self.gui = gui.GuiDesign(self.window)

    def header(self):
        self.gui.frames(0, 0, 800, 500, 'white')
        self.gui.title_design(30, 30, "User Account Page", 20)

    def personal_info(self):
        image_loc = r'C:\Users\danie\Desktop\repository\PLD01E\Final_Project\user_account_page\AGUSTIN_DANIEL_CPE201.jpg'
        self.gui.frames(30, 130, 740, 200, 'light grey')
        self.gui.image_design(image_loc, 50, 70, 100, 100)
    # First Name
        self.gui.label_design_bg(190, 135, "First Name: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(190, 160, "Daniel", 10)
    # Middle Name
        self.gui.label_design_bg(300, 135, "Middle Name: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(300, 160, "Advincula", 10)
    # Last Name
        self.gui.label_design_bg(410, 135, "Last Name: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(410, 160, "Agustin", 10)
    # Suffix
        self.gui.label_design_bg(520, 135, "Suffix: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(520, 160, "", 10)
    # Department
        self.gui.label_design_bg(630, 135, "Department: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(630, 160, "DOE", 10)
    # Designation
        self.gui.label_design_bg(60, 190, "Designation: ", 'light grey', 12, 'black')
        self.gui.textbox_design_disabled2(60, 215, "Computer Engineering", 24)
    # Username
        self.gui.label_design_bg(300, 190, "Username: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(300, 215, 20, 1, 'black', 12)
    # Password
        self.gui.label_design_bg(490, 190, "Password: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(490, 215, 20, 1, 'black', 12)
    # Confirm Password
        self.gui.label_design_bg(60, 250, "Confirm Password: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(60, 280, 20, 1, 'black', 12)
    # User Type
        self.gui.label_design_bg(250, 250, "User Type: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(250, 280, 15, 1, 'black', 12)
    # User Status
        self.gui.label_design_bg(400, 250, "User Status: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(400, 280, 15, 1, 'black', 12)
    # Employee Number
        self.gui.label_design_bg(550, 250, "Employee Number: ", 'light grey', 12, 'black')
        self.gui.textbox_design3(550, 280, 22, 1, 'black', 12)

    def button(self):
        self.gui.button_design(260, 350, "Update", '#4A5CFF', 'black', 'black', 1, 10, 1)
        self.gui.button_design(350, 350, "Delete", '#E5CA18', 'black', 'black', 1, 10, 1)
        self.gui.button_design(440, 350, "Cancel", '#EEEDEC', 'black', 'black', 1, 10, 1)
