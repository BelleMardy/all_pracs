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
    if choice == "H":
        print("Hello", name)
        print()
        choice = input("Pick again: " + MENU).upper()
        print()
    elif choice == "G":
        print("Goodbye", name)
        print()
        choice = input("Pick again: " + MENU).upper()
        print()
    else:
        choice = input("Error, you need to input, H, G, Q: " + MENU).upper()
        print()

print("Thank you for playing", name)
