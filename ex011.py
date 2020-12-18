# Paint a wall
l = float(input("Wall Width: "))
a = float(input("Wall Height: "))

print("The dimensions of your wall is %s m x %s m and its area is %s m2.\nIn order to paint this wall you need %s l "
      "of paint "
      % (l, a, l*a, (l*a)/2))