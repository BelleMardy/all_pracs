"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH_INT = 5
MAX_LENGTH_INT = 15
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS_STR = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH_INT, "and", MAX_LENGTH_INT,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS_STR)
    password_str = input("> ")
    while not is_valid_password(password_str):
        print("Invalid password!")
        password_str = input("> ")
    print("Your " + str(len(password_str)) + " character password is valid: " + password_str)


def is_valid_password(password_str):
    """Determine if the provided password is valid."""
    if len(password_str) <MIN_LENGTH_INT or len(password_str) > MAX_LENGTH_INT:
        return False
    # DONE - TO DO: if length is wrong, return False

    count_lower_int = 0
    count_upper_int = 0
    count_digit_int = 0
    count_special_int = 0
    for char in password_str:
        if char.isdigit():
            count_digit_int += 1
        elif char.islower():
            count_lower_int += 1
        elif char.isupper():
            count_upper_int += 1
        elif char in SPECIAL_CHARACTERS_STR:
            count_special_int += 1
        # DONE - TO DO: count each kind of character (use str methods like isdigit)
    if count_lower_int == 0 or count_upper_int == 0 or count_digit_int == 0 or count_special_int == 0:
        return False
    # DONE -TO DO: if any of the 'normal' counts are zero, return False


    # DONE - TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    # if we get here (without returning False), then the password must be valid
    return True


main()
