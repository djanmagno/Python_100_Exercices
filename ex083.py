# Validanting mathmatic expressions

cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "vermelho": '\033[31m', }

expression = input("Please type the expression with parenthesis: ")
lst = []
for n in expression:
    if n == '(' or n == ')':
        lst.append(n)
if lst.count('(') == lst.count(')'):
    print(f'The expression {cor["vermelho"]}{expression}{cor["limpa"]} is correct!!!')
else:
    print(f'The expression {cor["vermelho"]}{expression}{cor["limpa"]} is not correct!!!')