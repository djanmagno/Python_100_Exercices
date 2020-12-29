# Creating a dictionary trhough functions

def grades(*n, sit=False):
    """
    Function to analyze grades and tell the situation of thr students
    :param n: one or more grades of the students (it can receive several grades)
    :param sit: optional value, it can indicate or not the situation of the students
    :return: a dictionary with information about the situation of the class
    """
    print('-' * 30)
    classroom = dict()
    classroom['total'] = len(n)
    classroom['bigger'] = max(n)
    classroom['smaller'] = min(n)
    soma = 0
    for i in n:
        soma += i
    classroom['average'] = (soma / len(n))

    if sit:

        if classroom['average'] >= 7:
            classroom['situation'] = 'GOOD'
        elif 5 <= classroom['average'] < 7:
            classroom['situation'] = 'OK'
        elif classroom['average'] < 5:
            classroom['situation'] = 'BAD'
        return classroom

    else:

        return classroom


resp = grades(4.5, 5, 6.5, 5, 4, sit=True)
print(resp)
