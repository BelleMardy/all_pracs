import random

# in_file = open("cards.txt", "r")
#
# card_options = (in_file.read[1,52])
# for i in range(card_options):
#     print(random.randint(card_options))

def main():
    number = int(input("First numbers: "))
    number2 = int(input("Second number; "))
    i = random.randint(number,number2)
    print("First number {}".format(i))
    while (random.randint(number,number2)) != i:
        number = int(input("First numbers: "))
        number2 = int(input("Second number; "))
        i = (random.randint(number, number2))
        if i == i:
            print("Second number {}.".format(i))
        else:
            print("Forth number {}.".format(i))
    print("Third number {}.".format(i))

main()