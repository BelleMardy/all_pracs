"""
Create an electricity bill estimator
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928


def main():
    tariff = int(input("Enter which tariff, 11 or 31?: "))
    daily_use_of_kWh = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of days in billing days: "))
    if tariff == 11:
        print("Estimated bill: ${:.2f}.".format((TARIFF_11 * daily_use_of_kWh) * billing_days))
    else:
        print("Estimated bill: ${:.2f}.".format((TARIFF_31 * daily_use_of_kWh) * billing_days))

main()