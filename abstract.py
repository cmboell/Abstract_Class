"""
Assignment name: Abstract Class Assignment
Program: abstract.py
Author: Colby Boell
Last date modified: 04/12/2022

The purpose of this program is to  us an abstract class Rider with ride and riders methods and create
subclasses  Bicycle, Motorcycle, and Car that implement the abstract methods.
"""
# import
from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    def riders(self):
        pass


class Bicycle(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())


class Motorcycle(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())


class Car(Rider):
    def __init__(self, power, enclosed, num_riders):
        self.power = power
        self.enclosed = enclosed
        self.num_riders = num_riders

    # overrides abstract method with implementation
    def ride(self):
        return str(self.power) + ", " + str(self.enclosed)

    def riders(self):
        return str(self.num_riders)

    def __str__(self):
        return str(self.ride())


# Driver code
if __name__ == '__main__':
    rider_b = Bicycle('Human powered', 'not enclosed', '1 or 2 if tandem or a daredevil')
    print(rider_b.ride())
    print(rider_b.riders())
    rider_m = Motorcycle('Engine powered', 'not enclosed', '1 or 2')
    print(rider_m.ride())
    print(rider_m.riders())
    rider_c = Car('Engine powered', 'enclosed', '1 plus comfortably')
    print(rider_c.ride())
    print(rider_c.riders())
