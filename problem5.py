# Write a program to accept marks of 6 students and display them in a sorted 
# manner.
marks1=input(int("Enter the marks of student 1 :\n"))
marks2=input(int("Enter the marks of student 2 :\n"))
marks3=input(int("Enter the marks of student 3 :\n"))
marks4=input(int("Enter the marks of student 4 :\n"))
marks5=input(int("Enter the marks of student 5 :\n"))
marks6=input(int("Enter the marks of student 6 :\n"))
list=[marks1,marks2,marks3,marks4,marks5,marks6]
list.sort()
print(list)