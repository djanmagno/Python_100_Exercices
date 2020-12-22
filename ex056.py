# People analyzer

list_name = []
age_list = []
gender_list = []

for k in range(1, 5):
    print("----- {} PERSON -----".format(k))
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender [M/F]: ").upper()
    list_name.append(name)
    age_list.append(age)
    gender_list.append(gender)

print("In average of this group is {} years old.".format(sum(age_list)/len(age_list)))

if gender_list.count("M") != 0:
    print("The oldest man is {} years old and his name is {}."
          .format(max(age_list), list_name[age_list.index(max(age_list))]))
else:
    print("There is no man on this group!")

count = 0
if gender_list.count("F") != 0:
    for a, b in zip(gender_list, age_list):
        if a == "F" and b < 20:
           count += 1
else:
    pass
print("In total we have {} women under 20 on this group.".format(count))

