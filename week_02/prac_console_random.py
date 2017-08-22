print("""help(random.randint)
Help on method randint in module random:
randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
    
    """)

print("""help(random.randrange)
Help on method randrange in module random:
randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
    Choose a random item from range(start, stop[, step]).
    
    This fixes the problem with randint() which includes the
    endpoint; in Python this is usually not what you want.
    
    """)

print("""help(random.uniform)
Help on method uniform in module random:
uniform(a, b) method of random.Random instance
    Get a random number_int in the range [a, b) or [a, b] depending on rounding.
""")

print("""
print(random.randint(5, 20))
18

What did you see on line 1.
    A random number_int between and inclusive of 5 and 20.

What was the smallest number_int you could have seen.
    5

What was the largest number_int you could have seen.
    20
    
______________________________________________________________

print(random.randrange(3, 10 , 2))
7

What did you see on line 2.
    A random number_int between and inclusive of 3 and 9, excluding 10.
    Starting at 3
    3
    (3+2)
    5
    (5+2)
    7
    (7+2)
    9

What was the smallest number_int you could have seen.
    3

What was the largest number_int you could have seen.
    9
    
______________________________________________________________

NOT SURE ABOUT THIS ONE

print(random.uniform(2.5, 5.5))
4.487295499375918

help(random.uniform)
Help on method uniform in module random:
uniform(a, b) method of random.Random instance
    Get a random number_int in the range [a, b) or [a, b] depending on rounding.


What did you see on line 3.
    A random number_int between and inclusive of 2.5 and 5.5, depending on rounding, however it seems the rounding
    goes to 15 decimal points.

What was the smallest number_int you could have seen.
    2.500000000000000

What was the largest number_int you could have seen.
    5.500000000000000
    
______________________________________________________________

""")

import random #  should be at top, however for this exercise keeping module close to program

print(random.randint(1, 4))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))
