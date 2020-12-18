# Verifying the first letters of a text

name = input("What is your full name? ")
name_v1 = name.lower().strip()
print("Does your name have 'Silva'? %s" % ("silva" in name_v1))