# Fuction to determine if someone can vote or not
import datetime

print('-' * 30)

now = datetime.datetime.now().year
birth = int(input('When did you born? '))


def vote(year):
    """
    Function to return the
    :param year: Birth year to be analyzed
    :return: The vote situation of a person based on the age
    """
    age = now - year
    if age < 18:
        print(f'Being {age} years old: YOU DO NOT VOTE.')
    elif 18 <= age <= 65:
        print(f'Being {age} years old: YOU MUST VOTE.')
    else:
        print(f'Being {age} years old: IT IS OPTIONAL TO VOTE.')


vote(birth)
