
import laboratory_5
# Initialization and Getting the Values of Student Information
student = laboratory_5.Student()
student.student_subjects()
assessment = laboratory_5.AssessmentFee(student)
section_width = 10
subject_width = 40
unit_width = 9
assessment_width = 40

# Displaying Student Information
def student_information():
    
    print(" ")
    print(" ")
    print(" ")
    print(f"{"Student Name:":<15} {student.student_name:<60} {"Student Number:":<15} {student.student_number:<10}")
    print(f"{"Student Course:":<15} {student.student_course:<60} {"Academic Year:":<15} {student.academic_year:<10}")
    print("-" * (section_width + subject_width + unit_width), "|", "-" * (assessment_width + unit_width))
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Assessment of Fees':^{assessment_width + unit_width}}")
    print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")

def subjects_assessment_fee():
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Tuition Fee Lecture:':<{assessment_width}} {assessment.tuition_fee():>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'LPU Chronicle:':<{assessment_width}} {assessment.chronicle:>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Athletic:':<{assessment_width}} {assessment.athletic_fee:>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Audio Visual Library:':<{assessment_width}} {assessment.audio_visual_lib:>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'LycesGo:':<{assessment_width}} {assessment.student_government:>{unit_width - 5}}")
    print(f"{' ':<{section_width + subject_width - 17}} {' ':<{15}} {' ':<{unit_width}} | {'Cultural Fee:':<{assessment_width + 1}} {assessment.culture:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Energy Cost, AC Classroom:':<{assessment_width + 1}} {assessment.energy_cost_aircon_classroom:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Guidance Fee:':<{assessment_width + 1}} {assessment.guidance:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Insurance Fee:':<{assessment_width + 1}} {assessment.insurance:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Learning Management System:':<{assessment_width + 1}} {assessment.learning_management_system:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Library Fee:':<{assessment_width + 1}} {assessment.library:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Medical and Dental Fee:':<{assessment_width + 1}} {assessment.medical_dental:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Registration Fee:':<{assessment_width + 1}} {assessment.registration:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Recognized Student Government:':<{assessment_width + 1}} {assessment.recognized_student_gov:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Student Activities:':<{assessment_width + 1}} {assessment.student_activities:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Student Nurturance:':<{assessment_width + 1}} {assessment.student_nurturance:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Technology Fee:':<{assessment_width + 1}} {assessment.technology:<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Test Papers Fee:':<{assessment_width + 1}} {assessment.test_paper:<{unit_width}}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Total Assessment:':<{assessment_width}} {assessment.assessment_amount():<{unit_width}}")
    print(f"{' ':<{section_width + subject_width + unit_width}} | {'Downpayment:':<{assessment_width}} {assessment.downpayment:<{unit_width}}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")
    print(f"{' ' * (section_width + subject_width + unit_width)} | ")

def schedule_of_payment():

    due = round(assessment.total_due() / 3, 2)
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'-' * 47}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'Schedule of Payment':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'of outstanding balance':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'after downpayment prior to: ':^{47}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Prelim:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Midterm:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{' ' * 5}{'Finals:':<{27}} {due:<{14}}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} | |{'-' * 47}|")
    print(f"{' ' * (section_width + subject_width + unit_width)} |  {'*There will be a 6% surcharge p.a.':^{47}} ")
    print(f"{' ':^{section_width + subject_width + unit_width}} |  {'for late payment':^{47}} ")

def date_printed():
     print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
     print(f"{' ':>{30}} {' ':<{28}} | {'THIS IS TEMPORARY ASSESSMENT':^{50}}")
     print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")
     print(f"{' ':^{59}}")



student_information()
subjects_assessment_fee()
schedule_of_payment()
date_printed()