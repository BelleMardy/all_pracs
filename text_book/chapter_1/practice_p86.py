"""import random

guess = random.randint(1, 1000)
tires = 0
while guess >= 50:
    tires += 1
    print("Line {}, number is: {}".format(tires, guess))
    guess = random.randint(1, 1000)
print("Line {}, Game over your number is: {}".format(tires + 1, guess))
print()
print("banana")
team_ahead_int = in
t(input("The team is ahead by: "))
team_ahead_int -= 3
team_has_ball = random.randint(1, 2)  # 1 = team has ball, 2 does not have ball
if team_ahead_int != 2:
    team_ahead_int += .5
    team_ahead_int += abs(team_ahead_int)
    if team_ahead_int > 0:
        team_ahead_int *= team_ahead_int
        print("Game is safe because the score will be: {}".format(abs(team_ahead_int)))
    else:
        print("Game is not safe because the score will be: {}".format(abs(team_ahead_int)))
else:
    print("Game is not safe because the score will be: {}".format(abs(team_ahead_int)))
print()
first_int = random.randint(1, 100)
second_int = random.randint(1, 100)
line = 0
while first_int > second_int:
    line += 1
    print("{}. First number {} is bigger than the second number {}.".format(line, first_int, second_int))
    first_int = random.randint(1, 100)
    second_int = random.randint(1, 100)
print("{}. First number {} is smaller than the second number {}.".format(line + 1, first_int, second_int))

line = 0
for the_char in "hi mardy".upper():
    line += 1
    print(("{}.".format(line), the_char))
print()
for the_char in "hi mardy".upper():
    line += 1
    print((the_char), end="   ")

number_int = int(input("Enter number: "))

divisor_int = 1
sum_of_divisors_int = 0
while divisor_int < number_int:
    if number_int % divisor_int == 0:
        sum_of_divisors_int = sum_of_divisors_int + divisor_int
    divisor_int = divisor_int + 1

if number_int == sum_of_divisors_int:
    print("Number is perfect!")
else:
    print("Number is not perfect!")

top_number_int = int(input("What is the upper number_int for the range: "))
number_int = 2
line_int = 0

while number_int <= top_number_int:
    divisor_int = 1
    sum_of_divisors_int = 0
    line_int += 1
    while divisor_int < number_int:
        if number_int % divisor_int == 0:
            sum_of_divisors_int = sum_of_divisors_int + divisor_int
        divisor_int = divisor_int + 1
    if number_int == sum_of_divisors_int:
        print("{}. {} is perfect".format(line_int, number_int))  # equals the sum of its divisors
    elif number_int < sum_of_divisors_int:
        print("{}. {} is abundant".format(line_int, number_int))  # greater than the sum of its divisors
    else:
        print("{}. {} is deficient".format(line_int, number_int))  # less than the sum of its divisors
    number_int += 1

import random

generated_number_int = random.randint(0, 101)
guessed_number_int = int(input("Enter a number between and inclusive of 0 - 100: "))
line = 0 + 1
while 0 <= guessed_number_int <= 100:
    if generated_number_int > guessed_number_int:
        guessed_number_int = int(input("{}. Number to low, try again: ".format(line)))
    elif generated_number_int < guessed_number_int:
        guessed_number_int = int(input("{}. Number to high, try again: ".format(line)))
    else:
        print("{}. {} you got the number correct.".format(line, guessed_number_int))
        generated_number_int = random.randint(0, 101)
        guessed_number_int = int(input("Enter a number between and inclusive of 0 - 100: "))
    line += 1
print("{}. game over, the number was {}".format(line, generated_number_int))

number = 0
line = 0

for number in range(1, 10, 2):
    line += 1
    print("{}. nunmber: {} - ".format(line, number), end=" ")
    print(sum(range(number)))
    total = (sum(range(number)))

print()
print("{}. nunmber: {}, {}".format(line, number, total), end='')"""

"""bunny = []
for puppies in range(1, 100, 7):
    bunny.append(puppies * 5)
print(bunny)
print(len(bunny))"""

"""number_list = []
line_int = 0
number_int = int(input("Number to check: "))

for division_list in range(100, 1000):
    if division_list % number_int == 0:
        line_int += 1
        number_list.append(division_list // number_int)
        print("{}. number: {}".format(line_int, division_list))
print(len(number_list))"""

"""user_str = "abcdef"
index_int = 0
print(user_str[index_int])
print(user_str[(index_int + 2)])"""

"""cameron_test_str = "Trick or treat"
for cameron_test_str in reversed(cameron_test_str):
    print(cameron_test_str)"""
"""line = 0
for a in "abce":
    line +=1
    print(line,a)"""

"""my_str = input("Input a string: ")
index_int = 0
result_str = ''
while index_int < (len(my_str)):
    if my_str[index_int] > my_str[index_int + 1]:
        result_str += my_str[index_int]
    else:
        result_str *= 2
    index_int += 1
print(result_str)"""

my_str = 'Mardy'
my_str = 'o' + my_str[2]
print(my_str)

string = "trick or treat"
for character in string[::-1]:
    print(character)

cameron_test_str = "Trick or treat"
for cameron_test_str in reversed(cameron_test_str):
    print(cameron_test_str)