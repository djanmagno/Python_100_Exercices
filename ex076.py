# Price list using tupple

lst = ('Pencil', 1.75,
       'Eraser', 2,
       'Notebook', 15.90,
       'Pencil Bag', 25,
       'Ruller', 4.20,
       'Compass', 9.99,
       'Backpack', 120.32,
       'Pen', 22.30,
       'Book', 34.90)
print('-' * 50)
title = 'Listagem de Preço'
print(title.center(50))
print('-' * 50)

for n in lst:
    if lst.index(n) % 2 == 0:
        print(f'{n:.<30}', end='')
    else:
        print(f'R$ {n:>7.2f}')
print('-' * 50)