# Creating a option menu

first = int(input("First Value: "))
second = int(input("Second Value: "))


print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
option = int(input("Which is your choice? "))



while option != 5:

    if option == 1:
       print("The result of {} + {} is {}".format(first, second, first + second))
       print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
       option = int(input("Which is your choice? "))

    elif option == 2:
        print("The result of {} x {} is {}".format(first, second, first * second))
        print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
        option = int(input("Which is your choice? "))

    elif option == 3:
        lst = [first, second]
        print("The biggest number between {} and {} is {}.".format(first, second, max(lst)))
        print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
        option = int(input("Which is your choice? "))
    elif option == 4:
        print("Please tell me the new numbers:")
        first = int(input("First Value: "))
        second = int(input("Second Value: "))
        print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
        option = int(input("Which is your choice? "))
    else:
        print("{} is not an option!".format(option))
        print("  [ 1 ] Sum\n  [ 2 ] Multiplication\n  [ 3 ] Bigger\n  [ 4 ] New Numbers\n  [ 5 ] Leave the Program")
        option = int(input("Which is your choice? "))

print("End of the program! Back another time!")