# Anatomizing a variable
variable = input("Please type anything: ")
print("The primitive type of this value is %s" % type(variable))
print("Is this variable has any space? %s" % variable.isspace())
print("Is this variable an number? %s" % variable.isalnum())
print("Is this variable present on the alphabet? %s" % variable.isalpha())
print("Is this variable present on the alphanumeric encoding? %s" % variable.isalnum())
print("Is this variable on upper letters? %s" % variable.isupper())
print("Is this variable on upper letters? %s" % variable.islower())
print("Is this variable capitalized? %s" % variable.istitle())
