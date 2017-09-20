"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_07.car import Car


def main():
    print(("Car fuel and odometer").upper())
    current_fuel_car = int(input("Current fuel car: >>> "))
    my_car = Car("My car", current_fuel_car) #  Pascal shows that this is class "Car"
    current_odometer_car = int(input("Current odometer limo: >>> "))
    my_car.drive(current_odometer_car) #  drive is part of the Car class
    print("Car Fuel: {} ".format(my_car.fuel))
    print("Car Odometer: {} ".format(my_car.odometer))
    print("{}".format(my_car))
    print()
    print()
    print(("Limo fuel and odometer").upper())
    current_fuel_limo = int(input("Current fuel limo: >>> "))
    limo = Car("Limo", current_fuel_limo)
    limo.add_fuel(int(input("Additional fuel: >>> ")))
    current_distance_driven = int(input("Distance driven: >>> "))
    limo.odometer += current_distance_driven
    print("{}".format(limo))

main()