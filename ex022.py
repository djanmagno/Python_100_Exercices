# String Manipulation

name = input("Please type your complete Name: ")
print("Your name only with upper letters is: {}".format(name.upper()))
print("Your name only with lower letters is: {}".format(name.lower()))
print('Your name has %s letters.' % (len(name) - name.count(" ")))
print('Your first name has %s letters' % (len(name.split()[0])))
