##The __init__() Method for a Child Class
#-Calling the __init__ method from the parent class when writing a new class based on a existing class will be be sometimes necessary
#-This will initiakize any attributes that were defined in the parent __init__() method and make them available in the child class
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            print(f"This car can go about {range} miles on a full charge.")

##Defining Attributes and Methods for the Child Class
#-After having a child class that inherited from a parent class, new attributes and methods
#-neccessary to differentiate the child class from the parent class
#-Example , below the battery size is stored and a new method printing a description of the battery will be written.

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
    print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()



##Overriding Methods from the Parent Class
#-Any method from the parent class which doesnt fit the intention of model with child class.
#-This may be done by defining method in a child class with the same name as the method intended to override in the parent class
#-Python will then disregard parent class methof anf only pay attention to the method you define in the child class.

##Instance as Attributes
#-Breaking a large class into smaller classes that work together will be neccessary, especially
#-When modelling something from the real world in code due to more details being added.
#-Attributes and methods will grow thus files will become lengthy.
