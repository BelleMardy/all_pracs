"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10
OUTPUT_FILE_NAME_STR = "stock_out.txt"  # copied from solutions as I didn't know what to call the file
output_file_name_str = open(OUTPUT_FILE_NAME_STR, 'w')

price = INITIAL_PRICE
day_counter = 1
print("On day {}, ${:,.2f}".format(day_counter, price), file=output_file_name_str)


while MIN_PRICE <= price <= MAX_PRICE:  # python gave the option to simplify so I took it, hoping it works
    price_change = 0
    day_counter += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_INCREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    percent_adj = price_change * 100
    if percent_adj < 0:
        print("On day {}, ${:,.2f}, decreased {:.2f}%".format(day_counter, price, percent_adj), file=output_file_name_str)
    else:
        print("On day {}, ${:,.2f}, increased {:.2f}%".format(day_counter, price, percent_adj), file=output_file_name_str)
output_file_name_str.close()