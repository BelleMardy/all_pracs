"""
Score between 0 - 100
90 or more excellent
50 or more is pass
below 50 is fail
CP1404/CP5632 - Practical - Broken program to determine score status
"""

# DONE - TO DO: Fix this!

score = float(input("Enter valid score between 0 to 100 (inclusive): "))
while score > 100 or score < 0:
    score = float(input("Invalid score, enter score between 0 to 100: "))
if score < 50:
    print("Fail")
elif score < 90:
    print("Pass")
else:
    print("Excellent")
