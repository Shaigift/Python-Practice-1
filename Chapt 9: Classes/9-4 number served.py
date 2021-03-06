class Restaurant():

    def __init__(self, name, cuisine_type,):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print(f"{self.cuisine_type} is now serving food")

    def open_restaurant(self):
        print(f"{self.name} is now open")

    def read_served(self):
        print(f"The number of people served are {self.served}")

    def update_served(self, people):
        self.served = people

    def increment_served(self, peoples):
        self.served += peoples
        

restaurant = Restaurant('Beef Burger', 'Good Burgers')
print(restaurant.name)
print(restaurant.cuisine_type)
restaurant.served = 75
restaurant.read_served()
restaurant.update_served(125)
restaurant.read_served()
restaurant.increment_served(100)
restaurant.read_served()

restaurant.describe_restaurant()
restaurant.open_restaurant()
