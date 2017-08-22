NAME_LENGTH = 0

def main():
    out_file = open("name.txt", "w")
    name = input("Enter name: ")
    valid_name = len(name)
    while valid_name <= NAME_LENGTH:
        name_checked = input("Invalid name: ")
        valid_name = len(name_checked)
        name = name_checked
    print(name, file=out_file)
    print((name[-1::-2]), file=out_file)
    print(name[1::2])
    print(name[-1::-2])
    out_file.close()
    in_file = open("name.txt", "r")
    second_name_read = (in_file.read())
    print(second_name_read)
    in_file.close()


main()