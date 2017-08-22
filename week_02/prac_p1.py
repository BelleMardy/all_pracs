# Prac example
print("prac example".upper())
number = [0, 50, 100]
for i in range(len(number)):
    print("Numbers are {1:>3}".format(i + 1, number[i]))
print()
print("belle prac test".upper())
numbers = [1, 19, 123, 456, -25]
number_1 = [2, 20, 124, 457, -26]
number_2 = [150, 200, 250]
for i in range(len([numbers, number_1, number_2])):
    print("Number is {:>5}".format(i + 1, numbers[i]))
    print("Number {0} is {1:>10}".format(i + 1, numbers[i]))
    print("Number {1} is {2:>15}".format(i + 2, numbers[i], number_1[i]))
    print('Number {2} is {3:>20}'.format(i + 2, numbers[i], number_1[i], number_2[i]))

print()
