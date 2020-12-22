# Palindrome phrases and word

cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "verde": '\033[32m',
       "vermelho": '\033[31m',
       "azul": '\033[34m'}

string = input("Please Type a phrase or word in order to find out if it is a palindrome or not: ").strip(" ").upper()

new_string = ""
for k in list(string):
    if k != " ":
        new_string += k
    else:
        pass

inv_new_string = new_string[::-1]

print("The inverse of {} is {}.".format(new_string, inv_new_string))

if new_string == inv_new_string:
    print("{}We HAVE a Palindrome!{}".format(cor["verde"], cor["limpa"]))
else:
    print("{}We DONT have a Palindrome!{}".format(cor["vermelho"], cor["limpa"]))
