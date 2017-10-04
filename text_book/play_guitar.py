from prac_07.guitars import Guitar


def main():

    guitars = []
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        # guitars.append(guitar_to_add)
        # #print(guitar_to_add, "added.")
        name = input("Name: ")
    guitars.sort()
    print("These are my guitars:")

    i = 0
    if guitars is not None:
        for guitar in guitars:
            vintage_string = ""
            # i = 0
            if guitar.is_vintage():
                i += 1
                vintage_string = "(vintage)"
                print("""Guitar {}: {:>30} ({:>4}), worth ${:10,.2f} {}""".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
        else:
            print("No guitars :( Quick, go and buy one!")



main()

