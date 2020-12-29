# Special print with functions

def writing(txt, k):

    print('-' * (len(txt) + 2 * k))
    print(f"{' ' * k}{txt}{' ' * k}")
    print('-' * (len(txt) + 2 * k))


writing('Djan Magno', 3)
writing('Curso de Python', 4)
writing('Cev', 1)