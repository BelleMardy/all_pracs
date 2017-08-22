"""Files
The solutions for these programs are at the bottom of the practical, to help you get going - or to confirm that your
solution was valid. Note: when you execute a Python program that contains a line like open('data.txt', 'w') the new
file “data.txt” is created in the same folder as the Python file in your PyCharm project.
Do all of the following in a single file called files.py:
1. Write a program that asks the user for their name, then opens a file called “name.txt” and writes that name to it.
2. Write a program that opens “name.txt” and reads the name (as above) then prints,
“Your name is Bob” (or whatever the name is in the file).
3. Create a text file called “numbers.txt”
(You can create a simple text file in PyCharm with Ctrl+N, choose “File” and save it in your project).
Put the numbers 17 and 42 on separate lines in the file and save it:
17
42
Write a program that opens “numbers.txt”, reads the numbers and adds them together then prints the result, which should
be… 59.
4. Extended (perhaps only do this if you’re cruising… if you are struggling, just read the solution) …
Now extend your program so that it can print the total for a file containing any number of numbers."""



"""name = input("What is your name? ")
print(name, file=out_file_name_str)  # or outFile.write(name)
out_file_name_str.close()"""


"""IN_FILE_NAME = "name.txt"
in_file_name_str = open(IN_FILE_NAME, "r")
name_1_str = in_file_name_str.read().strip()
print("Your name is: {}".format(name_1_str.upper()))
in_file_name_str.close()"""

"""in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()"""

"""IN_FILE_NUMBER_INT = "number.txt"
in_file_number_int = open(IN_FILE_NUMBER_INT, "r")
number_1_int = int(in_file_number_int.readline())
number_2_int = int(in_file_number_int.readline())
print("First number {}, second number {}, totals {}.".format(number_1_int, number_2_int, int(number_1_int + number_2_int)))
in_file_number_int.close()"""


"""in_file = open("number_int.txt")  # dont know what the r is for
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
print(number_1 + number_2)
in_file.close()
print()"""


"""OUT_FILE_NUMBER_INT = "number.txt"  # not sure about this one..... need help
out_file_number_int = open(OUT_FILE_NUMBER_INT, "w")
IN_FILE_NUMBER_INT = "number.txt"
in_file_number_int = open(IN_FILE_NUMBER_INT, "r")
number_1_int = ("Input first number_int: ")
number_2_int = ("Input second number_int: ")
total = 0
for line in in_file_number_int:
    number = int(line)
    total += number
    number = int(line)
print(total)
out_file_number_int.close()
in_file_number_int.close()"""

"""OUTPUT_FILE_NAME_STR = "name1.txt"
out_file_name_str = open(OUTPUT_FILE_NAME_STR, "w")  # dont know what the w is for
name_str = input("Enter your name: ".upper())
print("Your name is: {}".format(name_str.upper()), file=out_file_name_str)
out_file_name_str.close()
print()

IN_FILE_NUMBERS_INT = "numbers.txt"
in_file_number_int = open(IN_FILE_NUMBERS_INT, "r")
number1 = int(in_file_number_int.readline())
number2 = int(in_file_number_int.readline())
print(number1 + number2)"""

OUT_FILE_NUMBER_INT = "prac_extended.txt"
out_file_number_int = open(OUT_FILE_NUMBER_INT, "w")
in_file_number_int = open(OUT_FILE_NUMBER_INT, "r")
number_int = int(input("Enter a number: "))
number_returned_int = int(in_file_number_int.readline())
count_digit_int = 0
for char in number_returned_int:
    if char.isdigit():
        number_int += count_digit_int
        print("Total {}.".format(number_int), file=in_file_number_int)
    else:
        print("Total {}.".format(number_int), file=in_file_number_int)
print("Game over")
out_file_number_int.close()
in_file_number_int.close()