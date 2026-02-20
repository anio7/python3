student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = student_scores
for i in student_scores:
    if  100>= student_scores[i] >=91:
     student_scores[i] = "Outstanding"
    elif 90>= student_scores[i] >=81:
        student_scores[i] = "Exceeds Expectations"
    elif 80>= student_scores[i] >=71:
        student_scores[i] = "Acceptable"
    else:
        student_scores[i] = "Fail"

print(student_grades)