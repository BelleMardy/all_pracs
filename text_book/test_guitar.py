from prac_07.guitars import Guitar

CURRENT_YEAR = 2017


def test():
    name = "Gibson L-5 CES"
    year = 1990
    cost = 16035.40
    print("My guitar: {:3}, first made in {:3}".format(name, year))
    guitar = Guitar(name, year, cost)
    other = Guitar("leadbelly's guitar", 1920, 500000.00)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 5, other.get_age()))

    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, False, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name, True, other.is_vintage()))


# if __name__ == '__main__':
test()
