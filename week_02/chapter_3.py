"""letter_str = input("What letter are you asking about? ")
vowels_str = "aeiou".upper()
if letter_str.upper() in vowels_str.upper():
    print("Your letter {}, and it is a vowel, position {}.".format(letter_str.upper(), vowels_str.find(letter_str) + 1))
else:
    print("Your letter {}, and it is a consonant, and at position {}.".format(letter_str.upper(), letter_str.find(letter_str) + 1))

found_vowels_str = vowels_str.find(letter_str)
print(found_vowels_str)"""

"""my_str = " Mardy Molly"

print("The word {} has {} letters.".format("Mississippi", len("butter")))
print("One number is {}: the other is {}.".format(4, 3.5))
month = "June"
day = 5
year = 2011
print("The date is {} {}, {}.".format(month, day, year))
print("Interest rate is {:.2f} for your".format(2.7))
print("{:.>15s}: {:.<18.1f}".format("Length", 23.875))
print()
dog = "Mardy"
print(len(dog))
print()
for i in range(len(dog)):
    print(i)"""

"""sentence_str = "skduaelkdk".lower()
target_str = input("Enter a letter: ").lower()
yes_str = "yes"
for i, bunny in enumerate(sentence_str):
    if bunny == target_str:
        print("Is your letter {}, in the sentence {}, at position {}.".format(target_str.upper(), yes_str, i +1))
    else:
       print("Your letter {}, is not in {}.".format(target_str.upper(), sentence_str))
print(len(sentence_str))"""
import string
original_str = input('Input a string: ').lower()

bad_chars = string.whitespace + string.punctuation
for char in original_str:
    if char in bad_chars:
        original_str = original_str.replace(char, '')

if original_str == original_str[::-1]:
    print(\
        'The original string is: {}\n\
        the modified string      {}\n\
        the reversal is:         {}\n\
        String is a palindrome'.format(original_str, original_str.upper(), original_str[::-1]))
else:
    print( \
        'The original string is: {}\n\
        the modified string      {}\n\
        the reversal is:         {}\n\
        String is a palindrome'.format(original_str, original_str.upper(), original_str[::-1]))

"""first, second, third = 'Mardy, and, Molly'.split(",")
print(second[::-1], third[2::-1], first[::-2]

op1, op2 = "A+B".split("+")
print(op2, op1)"""

