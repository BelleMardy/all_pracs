"""
A shop requires a small program that would allow them to quickly work out total price for a number of items,
each with different prices.
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to the total before the amount is displayed on the
screen.
IF the number of items is less than zero, the message "Invalid number of items!" should be displayed and this quantity
must be re-entered by the user UNTIL it is valid."
"""

DISCOUNT_PERCENT = .1  # 10% Discount
DISCOUNT_ON_SALES_OVER = 100  # Sales over $100.00
APPLIED_DISCOUNT = 0  # Initial discounted amount
purchases = 0  # Initial purchases
total_saless = 0  # Initial sales

number_of_items = int(input("Enter total number_int of items purchased ie. 0 or more: "))


while number_of_items < purchases:
    number_of_items = int(input("Error {}, please enter total of items purchased ie. 0 or more: ".format(number_of_items)))


for i in range(number_of_items):
    price = float(input("Cost of item: $"))
    total_saless += price


if total_saless > DISCOUNT_ON_SALES_OVER:
    APPLIED_DISCOUNT = total_saless * DISCOUNT_PERCENT
    total_saless -= APPLIED_DISCOUNT


print("Total items {}, total sales ${:.2f}, including the discount of ${:.2f}.".format(number_of_items, total_saless,
                                                                                       APPLIED_DISCOUNT))
