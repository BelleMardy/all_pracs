MENU = ("""
H = Hello
G = Goodbye
Q = Quit""")

name = input("Please enter name: ")
print(MENU)
print()
choice = input("Enter H, G, Q: ").upper()
print()
while choice != "Q":
    if choice.upper() == "H":
        print("Hello {}".format(name))
        print()
        choice = input("Pick again: {}".format(MENU).upper())
        print()
    elif choice.upper() == "G":
        print("Goodbye {}".format(name))
        print()
        choice = input("Pick again: ".format(MENU).upper())
        print()
    else:
        choice = input("Error, you need to input, H, G, Q: ").upper()
        print()

print("Thank you for playing {}".format(name))
