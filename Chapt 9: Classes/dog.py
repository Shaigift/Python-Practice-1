#CLASSES
#-The most effective way to writing software is through Object-oriented programming, Object-oriented programming uses classes
#-Which represent real-world thinfs and situations , programmers can create objects based on these classes
#-classes can represent real life things and situations, and objects based on these classes.
#-Classes define the usual behavior that a whole category of objects can have.
#-Created unique objects from the class, each object is automatically equipped with the general behavior;
#-You can then give each object whatever unique traits desired.
#-An object made from a class is called instantiation ,and i will worj with instances of a class.
#-Undestaind object-oriented programming will help us see the world as programmers do. it will help
#-knowing the logic behind classes that will train us to think logically so that we can write programs
#-that effectively address almost any problem i encounter.

#Creating and Using a Class
#Creating the Dog Class
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

##The __init__()Method
#-Functions forming an item of a class is a method. The __init__ method is a special nethod that Python runs automatically
#-whenever we create a new instance based on the dog class.

#Making an Instance from a Class
my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")


##Creating Multiple Instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()