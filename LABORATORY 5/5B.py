import laboratory_5
# Initialization and Getting the Values of Student Information
student = laboratory_5.Student()
student.student_subjects()
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
    print(f"{'Section':<{section_width}}{'Subject':^{subject_width}} {'Units':<{unit_width - 1}} | ")
    print(f"{'-' * (section_width + subject_width + unit_width)} | {'-' * (assessment_width + unit_width)}")

def subjects_assessment_fee():
    section, subject, unit = student.subject_info[0]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[1]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[2]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[3]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    section, subject, unit = student.subject_info[4]
    print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width - 2}} | ")
    print(f"{' ':<{section_width + subject_width - 17}} {'TOTAL UNITS:':<{15}} {student.sum_units():<{unit_width}} | ")


student_information()
subjects_assessment_fee()