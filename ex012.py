# Discount Calculator

p = float(input("What is the price of the product? R$ "))
d = float(input("What is the discount of the product? "))

print("The product price was R$ {} and the applied discount is {} %.\nThe new price of the product is R$ {}."
      .format(p, d / 100, round(p * (1 - d / 100), 2)))
