"""
A school teacher requires a small program that would allow primary school students to learn about various
number sequences. The teacher is interested in a simple menu-driven program that has the following choices
(where x and y are inputs the user enters once at the start of the program).
"""

x = int(input("Enter a starting number_int: "))
y = int(input("Enter an ending number_int: "))
for i in range(x, y, 2):
    print(i + (i % 2), end=" ")
print()


for i in range(x, y, 2):
    if x % 2 != 0:
        print(i, end=" ")
    else:
        print(i + 1, end=" ")
print()


for i in range(x, y):
    print(i * i, end=" ")
print()
