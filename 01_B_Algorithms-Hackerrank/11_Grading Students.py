# For question go to:
# https://www.hackerrank.com/challenges/grading/problem

no_of_students = int(input())
i = 0
while i < no_of_students:
    grades = int(input())
    grades = grades-grades%5+5 if grades%5>2 and grades>=38 else grades
    print(grades)
    i += 1