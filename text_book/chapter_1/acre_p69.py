AREA_FLOAT = 43560
ONE_CUBIC_FEET_TO_GALLONS_FLOAT = 7.48051945
DEPTH_FLOAT = 12
inches_float = float(input("Enter number_int of inches that fell: "))
area_float = float(input("Enter number_int of aches: "))

volumn_float = (inches_float/DEPTH_FLOAT) * AREA_FLOAT
gallons_float = volumn_float * ONE_CUBIC_FEET_TO_GALLONS_FLOAT
print("{:.2f} inches rain on 1 acre is {:.2f} gallons.".format(inches_float, gallons_float))
