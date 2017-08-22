
"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

# The ‘old’ manual way to format text with string concatenation:
print("OLD MANUAL WAY TO FORMAT")
print("My guitar: " + name + ", first made in " + str(year))
print()

# A better way - using str.format():
print("A better way to format".upper())
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
print()

# Formatting currency (grouping with comma, 2 decimal places):
print("Currency formatting".upper())
print("My {} would cost ${:,.2f}".format(name, cost))
print()

# Aligning columns:
print("Alignment - Left, >* is the spaces to the left including the object".upper())
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>5}".format(i + 1, numbers[i]))
print()

# Another (nicer) version of the above loop using the enumerate function
print("BETTER VERSION using 'enumerate' Alignment - Left, >* is the spaces to the left including the object".upper())
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))
print()

# DONE - TO DO: Using a for loop with the range function and string formatting,
# produce the following output:
#   0
#  50
# 100
print("Prac on page 1".upper())
numbers_for_prac = [0, 50, 100]
for i, numbers_for_prac in enumerate(numbers_for_prac):
    print("Numbers {1:>3}".format(i, numbers_for_prac))
print()
print("my Practice from page 1".upper())
numbers_for_prac = [3]
for i, numbers_for_prac in enumerate(numbers_for_prac):
    print("Numbers {3:>10}".format(i, numbers_for_prac, (10000), (50), (10)))
