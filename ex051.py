# 10 first terms of Arithmetic Progression

cor = {"limpa": '\033[m',
       "amarelo": '\033[33m',
       "vermelho": '\033[31m', }

print("=" * 50)
print("     10 FIRST TERMS OF ARITHMETIC PROGRESSION")
print("=" * 50)

first_term = int(input("Please type the first term of the AP: "))
reason = (int(input("Please type the reason of the AP: ")))
# a = b = c = d = e = f = g = h = i = 0
for k in range(first_term, first_term + (10*reason), reason):
    print("{}{}{}".format(cor["amarelo"], k, cor["limpa"]), end=" -> ")
    """
    a = first_term + reason
    b = a + reason
    c = b + reason
    d = c + reason
    e = d + reason
    f = e + reason
    g = f + reason
    h = g + reason
    i = h + reason
    """
"""
#print("{}{} -> {} -> {} -> {} -> {} -> {} -> {} -> {} -> {} -> {} ->{} {}OVER!{}"
      #.format(cor["amarelo"], first_term, a, b, c, d, e, f, g, h, i, cor["limpa"], cor["vermelho"], cor["limpa"]))
"""
print("{}OVER!{}".format(cor["vermelho"], cor["limpa"]))