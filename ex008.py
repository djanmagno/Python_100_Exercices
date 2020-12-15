# Metric conversor

d = int(input("Please type a distance em meters: "))
print("%s meters is the same as\n%s km\n%s Hm\n%s Dam\n%s dm\n%s cm\n%s mm"% (d, d/(10)**3, d/(10)**2, d/(10), d*(10),
                                                                              d*(10)**2, d*(10)**3))