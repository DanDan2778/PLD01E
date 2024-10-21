import laboratory_5

student = laboratory_5.Student()
student.student_subjects()
section_width = 10
subject_width = 40
unit_width = 10


def display_student_information():
    print(f"\n\n\nStudent Name: {student.student_name:<30} Student Number: {student.student_number:<15}")
    print(f"Student Course: {student.student_course:<30} Academic Year: {student.academic_year:<15}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(F"{'Section':<{section_width}}{'Subject':<{subject_width}} {'Unit':<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))


    for section, subject, unit in student.subject_info:
        print(f"{section:<{section_width}} {subject:<{subject_width}} {unit:<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))
    print(f"{' ':<{section_width + subject_width}} Total Units: {student.sum_units():<{unit_width}}")
    print("-" * (section_width + subject_width + unit_width + 15))

display_student_information()
