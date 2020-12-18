# Picking a random student to erase a blackboard
from random import choice

student1 = input("First Student: ")
student2 = input("Second Student: ")
student3 = input("Third Student: ")
student4 = input("Fourth Student: ")

student_list = [student1, student2, student3, student4]

print("The chosen student was: %s" %(choice(student_list)))