# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # bass class
    pass

class FlightVehicle(Vehicle):
    # Vehicle
    pass

class Starship(FlightVehicle):
    # FlightVehicle -> Vehicle
    pass

class Airplane(FlightVehicle):
    # FlightVehicle -> Vehicle
    pass

class GroundVehicle(Vehicle):
    # Vehicle
    pass

class Car(GroundVehicle):
    # GroundVehicle -> Vehicle
    pass

class Motorcycle(GroundVehicle):
    # GroundVehicle -> Vehicle
    pass
