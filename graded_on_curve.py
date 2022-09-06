#HackerLand University has the following grading policy:

#Every student receives a grade in the inclusive range from 0 to 100.
#Any grade less than 40 is a failing grade.
#Sam is a professor at the university and likes to round each student's grade according to these rules:

#If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of 5.
#If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

def grading_students(grades):
    rounded_grades = [] # Created a new list to assign updated grades.
    for grade in grades: # Iterate through given array of grades.
        if grade < 38 : # Check for failing grade.
            rounded_grades.append(grade) # No adjustment, add to new list.
        elif (grade + 2) % 5 == 0:
            rounded_grades.append(grade+2) # If adding 1 or 2 to grade makes it divisible by 5, add updated score.
        elif (grade + 1) % 5 == 0:
            rounded_grades.append(grade+1)
        else:
            rounded_grades.append(grade) # If grade already divisible by 5 or can't be bumped up, append.
    return rounded_grades # return updated list.