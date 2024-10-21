# Class for Student Information
class Student:

    # Initialization
    def __init__(self):

        # Getting the Values of Student Information
        self.student_name = input("Enter Student Name: ")
        self.student_course = input("Enter Student Course: ")
        self.student_number = input("Enter Student Number: ")
        self.academic_year = input("Enter Academic Year: ")
        self.date_printed = input("Enter Date of Printed: ")
        self.subject_info = []

    # Getting Student Subjects and Units
    def student_subjects(self):
        for i in range(5):
            print(f"Subject {i + 1}")
            section = input("Enter Section: ")
            subject = input("Enter Subject: ")
            unit = int(input("Enter Unit: "))
            self.subject_info.append((section, subject, unit))

    # getting the sum of units
    def sum_units(self):
        return sum(unit for _, _, unit in self.subject_info)


# Class for Assessment Fee
class AssessmentFee:

    # Getting the Value for Student Assessment Fees
    def __init__(self, student):
        self.student = student
        self.total_units = self.student.sum_units()
        self.tuition = 0
        self.chronicle = float(input("Enter ADU Chronicle Fee: "))
        self.athletic_fee = float(input("Enter Athletic Fee: "))
        self.audio_visual_lib = float(input("Enter Athletic Fee: "))
        self.student_government = float(input("Enter Student Government Fee: "))
        self.culture = float(input("Enter Culture Fee: "))
        self.energy_cost_aircon_classroom = float(input("Enter Energy Cost, Aircon Classroom Fee: "))
        self.guidance = float(input("Enter Guidance Fee: "))
        self.insurance = float(input("Enter Insurance Fee: "))
        self.learning_management_system = float(input("Enter Learning Management System Fee: "))
        self.library = float(input("Enter Library Fee: "))
        self.medical_dental = float(input("Enter Medical and Dental Fee: "))
        self.registration = float(input("Enter Registration Fee: "))
        self.recognized_student_gov = float(input("Enter Recognized Student Government Fee: "))
        self.student_activities = float(input("Enter Student Activities Fee: "))
        self.student_nurturance = float(input("Enter Nurturance Fee: "))
        self.technology = float(input("Enter Technology Fee: "))
        self.test_paper = float(input("Enter Test Papers Fee: "))
        self.downpayment = float(input("Enter Downpayment: "))

    # Formulating a Formula for Tuition Fee
    def tuition_fee(self):
        self.tuition = self.total_units * 1500.00
        return self.tuition

    # Formulating a Formula for Total Assessment Amount
    def assessment_amount(self):
        return (self.tuition_fee() + self.chronicle +
                self.athletic_fee + self.audio_visual_lib +
                self.student_government + self.culture +
                self.energy_cost_aircon_classroom + self.guidance +
                self.insurance + self.learning_management_system +
                self.library + self.medical_dental + self.registration +
                self.recognized_student_gov + self.student_activities +
                self.student_nurturance + self.technology + self.test_paper)

    # Formulating a Formula for Total Due
    def total_due(self):
        return self.assessment_amount() - self.downpayment
