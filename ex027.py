# First and Last Name of a person

name = input("What is your full name? ").strip()
splitted_name = name.split()
print("Nice to meet you!")
print("Your first name is {}".format(splitted_name[0]))
print("Your last name is {}".format(splitted_name[len(splitted_name)-1]))