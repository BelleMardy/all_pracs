"""
Score between 0 - 100
90 or more excellent
50 or more is pass
below 50 is fail
CP1404/CP5632 - Practical - Broken program to determine score status blah
"""

# DONE - TO DO: Fix this!


def main():
    score = float(input("Enter valid score between 0 to 100 (inclusive): "))
    print("Your overall grade of {:.2f}, means your level is {}.".format(score, score_level(score)))
    print()


def score_level(score):
    while score > 100 or score < 0:
        score = float(input("Invalid score, enter score between 0 to 100: "))
    if score < 50:
        return "Fail"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


main()
