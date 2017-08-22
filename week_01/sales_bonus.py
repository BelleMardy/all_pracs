"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%
"""

BONUS_1 = .1
BONUS_2 = .15

sales = float(input("Enter sales amount: $"))
while sales >= 0:
    if sales < 1000:
        bonus = float((sales * BONUS_1))
    else:
        bonus = float((sales * BONUS_2))
    print("Bonus on ${:.2f} is ${:.2f}.".format(sales, bonus))
    sales = float(input("Enter sales amount: $"))
print("Good-bye")
