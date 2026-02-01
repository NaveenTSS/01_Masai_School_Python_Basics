# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 03:06:59 2026

@author: Naveen
"""
import sys

student_name=input("Enter student name:")

maths_marks=int(input("Enter Maths marks:"))

if maths_marks<0 or maths_marks>100:
    print("Invalid marks entered")
    sys.exit("Stopping the program")

science_marks=int(input("Enter Science marks:"))

if science_marks<0 or science_marks>100:
    print("Invalid marks entered")
    sys.exit("Stopping the program")

english_marks=int(input("Enter English marks:"))

if english_marks<0 or english_marks>100:
    print("Invalid marks entered")
    sys.exit("Stopping the program")

average_marks=(maths_marks+science_marks+english_marks)/3

print(f"Student Name:{student_name}")

print(f"Total Marks:{maths_marks+science_marks+english_marks}")

print(f"Percentage:{((maths_marks+science_marks+english_marks)/300)*100}")

if maths_marks<40 or science_marks<40 or english_marks<40:
    print("Status: FAIL")
else:
    print("Status: PASS")

if average_marks>=75:
    print("Grade: A")
elif average_marks>=60:
    print("Grade: B")
elif average_marks>=40:
    print("Grade: C")

print("Program executed successfully")