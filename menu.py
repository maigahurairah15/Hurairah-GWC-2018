from random import *

#Create list of words you want to choose from.
main_course = ["shrimp alfredo", "lobster," "pollo", "cheeseburgers", "steak"]
appetizers = ["ceasar salad","biscuits", "cheese", "buffalo chicken","potato salad"]
sides = ["rice", "french fries", "mashed potato", "noodles"]
dessert = ["cheesecake","red velevet cake", "icecream," "tirimasu"]

 #generates a random integer.
x=randint(0, len(main_course)-1)
print("main_course:", main_course[x])
x=randint(0,len(appetizers)-1)
print("appetizers:", appetizers[x])
x=randint(0,len(sides)-1)
print("sides:", sides[x])
x=randint(0,len(dessert)-1)
print("dessert:", dessert[x])
