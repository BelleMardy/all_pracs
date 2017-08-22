"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
MENU = """
Enter the temperature type you want converted, ie. C = Celsius, F = Fahrenheit

C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    print()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("_" * 90)
            print("Result Celsius to Fahrenheit: {:.2f} F".format(fahrenheit))
            print()
        elif choice == "F":  # Done - Write this section to convert F to C and display the result
            fahrenheit = float(input("Fahrenheit: "))
            print("_" * 90)
            print("Result Fahrenheit to Celsius: {:.2f} C".format(celsius))
            print()
            # Done - Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius():
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def fahrenheit():
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

main()