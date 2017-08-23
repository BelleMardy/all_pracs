numbers = ([])
for i in range(5):
    number = float(input("Number: >>> "))
    numbers.append(number)


for i in range(1):
    number_line = 0
    print("Number {}, first number: {}".format(i + 1, (numbers[0])))
    print("Number {}, last number: {}".format(i + 1, numbers[4]))
    print("Number {}, smallest number: {}".format(i + 1, min(numbers)))
    print("Number {}, largest number: {}".format(i + 1, max(numbers)))
    print("Number {}, average number: {:.2f}".format(i + 1, sum(numbers) / (len(numbers))))
