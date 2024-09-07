# Getting the Student's Name, Final quizzes, Final Research/Assignment, Final Project, and Final Exam

students_name = input("Student's Name: ")
final_quiz = float(input("Final Quiz: "))
final_research = float(input("Final Research/Assignment: "))
final_project = float(input("Final Project: "))
final_exam = float(input("Final Exam:"))

# Setting the Formula for Ginal Grade Using the Inputted Values of Final Quizzes, Final Research/Assignment, Final Project, and Final Exam

final_grade = round(0.30 * final_quiz + 0.10 * final_research + 0.40 * final_exam +  0.20 * final_project)

# Determining the Equivalent Final Grade for the Numerical Value Obtained.

if 98 <= final_grade <= 100:
    remark = 4.00
elif 95 <= final_grade <= 97:
    remark = 3.75
elif 92 <= final_grade <= 94:
    remark = 3.50
elif 89 <= final_grade <= 91:
    remark = 3.25
elif 86 <= final_grade <= 88:
    remark = 3.00
elif 83 <= final_grade <= 85:
    remark = 2.75
elif 80 <= final_grade <= 82:
    remark = 2.50
elif 77 <= final_grade <= 79:
    remark = 2.25
elif 74 <= final_grade <= 76:
    remark = 2.00
elif 71 <= final_grade <= 73:
    remark = 1.75
elif 68 <= final_grade <= 70:
    remark = 1.50
elif 64 <= final_grade <= 67:
    remark = 1.25
elif 60 <= final_grade <= 63:
    remark = 1.00
elif final_grade < 60:
    remark = 0.00
else:
    remark =    "Final Grade Exceeded 100"

# Displaying the Student's Name, Final Quizzes, Final Research/Assignment, Final Project, Final Grade, and Equivalent Grading Remark

print("Student's Name:", students_name)
print("Final Quizzes:", final_quiz)
print("Final Research/Assignments: ", final_research)
print("Final Project:", final_project)
print("Final Grade:", f"{final_grade:.2f}")
print("Equivalent Grading Remark:", remark)