"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0  # need to have this or else there is an error stating, referenced before being defined
while not finished:
    try:
        result = int(input("Enter a number_int: "))  # DONE - TO DO: this line
        finished = True  # DONE - TO DO: this line
    except ValueError:  # DONE - TO DO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
