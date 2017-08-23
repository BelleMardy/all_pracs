"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of month."""
    incomes = []
    month_number = int(input("How many month? "))
    for month in range(1, month_number + 1):
        income = float(input("Enter income for month {}: ".format(month_number)))
        incomes.append(income)
    print_report(incomes)  #problem


def print_report(running_income):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, len(running_income) + 1):
        income = running_income[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
