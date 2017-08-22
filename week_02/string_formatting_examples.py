
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
# The ‘old’ manual way to format text:
print("The ‘old’ manual way to format text:".upper())
print("My guitar: " + name + ", first made in " + str(year))
print()
# A better way - using str.format():
print("A better way - using str.format():".upper())
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
print()
# Formatting currency:
print("Formatting currency".upper())
print("My {} would cost ${:,.2f}".format(name, cost))
print()
# Aligning columns:
print("Aligning columns".upper())
numbers = [1, 19, 123, 456, -25]
for i in range(len(numbers)):
    print("Number {0} is {1:>4}".format(i + 1, numbers[i]))
print()
