# Data Validation


gender = input("Please type your gender: [M/F] ").upper()

acronyms = "MF"

while gender not in acronyms:
    gender = input("Invalid data. Please type your gender: [M/F] ").upper()
print("Gender {} was registered!".format(gender))


