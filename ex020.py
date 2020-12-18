# Choosing the order of the presentation who will present a school project
from random import shuffle

student1 = input("First Student: ")
student2 = input("Second Student: ")
student3 = input("Third Student: ")
student4 = input("Fourth Student: ")

student_list = [student1, student2, student3, student4]

shuffle(student_list)

print("The chosen student was: %s" %(student_list))