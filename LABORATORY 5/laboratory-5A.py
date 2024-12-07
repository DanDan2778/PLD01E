
import laboratory_5
# Initialization and Getting the Values of Student Information
student = laboratory_5.Student()
student.student_subjects()
assessment = laboratory_5.AssessmentFee(student)
section_width = 10
subject_width = 40
unit_width = 10

# Displaying Student Information
def display_student_information():

    print(f"\n\n\nStudent Name: {student.student_name:<30} Student Number: {student.student_number:<15}")
    print(f"Student Course: {student.student_course:<30} Academic Year: {student.academic_year:<15}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(F"{'Section':<{section_width}}{'Subject':<{subject_width}} {'Unit':<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

    for section , subject, unit in student.subject_info:
        print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{' ':<{section_width + subject_width}} Total Units: {student.sum_units():<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"Date Printed: {student.date_printed}".center(section_width + subject_width + unit_width + 15))
    print('-' * (section_width + subject_width + unit_width + 15))

# Displaying Assessment Fee
def display_assessment_fee():
    print("\n")
    print("-" * (section_width + subject_width + unit_width + 15))
    print("Assessment Fee")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"Tution Fee Lecture: {assessment.tuition_fee():<{unit_width}}")
    print(f"LPU Chronicle: {assessment.chronicle:<{unit_width}}")
    print(f"Athletic: {assessment.athletic_fee:<{unit_width}}")
    print(f"Audio Visual Library: {assessment.audio_visual_lib:<{unit_width}}")
    print(f"LycesGo: {assessment.student_government:<{unit_width}}")
    print(f"Cultural Fee: {assessment.culture:<{unit_width}}")
    print(f"Energy Cost, Aircon Classroom: {assessment.energy_cost_aircon_classroom:<{unit_width}}")
    print(f"Guidance Fee: {assessment.guidance:<{unit_width}}")
    print(f"Insurance Fee: {assessment.insurance:<{unit_width}}")
    print(f"Learning Management System: {assessment.learning_management_system:<{unit_width}}")
    print(f"Library Fee: {assessment.library:<{unit_width}}")
    print(f"Medical and Dental Fee: {assessment.medical_dental:<{unit_width}}")
    print(f"Registration Fee: {assessment.registration:<{unit_width}}")
    print(f"Recognized Student Government: {assessment.recognized_student_gov:<{unit_width}}")
    print(f"Student Activities: {assessment.student_activities:<{unit_width}}")
    print(f"Student Nurturance: {assessment.student_nurturance:<{unit_width}}")
    print(f"Technology Fee: {assessment.technology:<{unit_width}}")
    print(f"Test Papers Fee: {assessment.test_paper:<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print(f"Total Assessment: {assessment.assessment_amount():<{unit_width}}")
    print(f"Downpayment: {assessment.downpayment:<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print(f"Total Due: {assessment.total_due():<{unit_width}}")
    print('-' * (section_width + subject_width + unit_width + 15))
    print("\n")

def display_schedule_of_payment():
    print('=' * (section_width + subject_width + unit_width + 15))
    print("Schedule of Payment of outstanding balance after downpayment prior for: ".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print(f"Prelim:, {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print(f"Midterm: {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print(f"Final: {assessment.total_due() / 3}".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print("*There will be a 60% surcharge for late payment.".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))
    print("THIS IS A TEMPORARY ASSESSMENT".center(section_width + subject_width + unit_width + 15))
    print('=' * (section_width + subject_width + unit_width + 15))

display_student_information()
display_assessment_fee()
display_schedule_of_payment()