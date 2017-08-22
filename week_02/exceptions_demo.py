"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        denominator = int(input("You need to enter a number_int greater than 0. >>> "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
#  except ZeroDivisionError:
    #  print("Cannot divide by zero!")
print("Finished.")
print()
print("""When will a ValueError occur?
1. When no number_int is input into either numerator or denominator.

When will a ZeroDivisionError occur.
2. When 0 is entered into denominator.

Could you change the code to avoid the possibility of a ZeroDivisionError.
3. Yes, added a while statement, and changed the except ZeroDivisionError to a comment.""")
