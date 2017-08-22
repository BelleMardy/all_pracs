number_int = int(input("Enter a number_int: "))
first_number_int = 2
second_number_int = 3
third_number_int = 6
forth_number_int = 3
print("Answer: {}.".format((int(number_int + first_number_int)*second_number_int - third_number_int)/forth_number_int))
print()
man = 1
wives = 7
sacks = 7
cats = 7
kittens = 7
wives *= man
sacks *= wives
cats *= sacks
kittens *= cats
print("Answer: {}.".format(man + wives + sacks + cats + kittens))
print()
my_int = 5
my_int += 3
print(my_int)
print()
my_var1 = 7.0
my_var2 = 5
print ("11. " + str(my_var1 % my_var2))
print()
x = 4
y = 5
print(x//y)
print()
import datetime
today = datetime.date.today()
print ("Current date {}".format(today))
print()
weight_float = float(input("What is your wegiht: "))
height_float = float(input("What is your height: "))
bmi_float = weight_float / (height_float ** 2)
print(bmi_float)