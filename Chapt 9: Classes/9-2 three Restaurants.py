class Restaurant():

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.cuisine_type} is now serving food")

    def open_restaurant(self):
        print(f"{self.name} is now open")

restaurant = Restaurant('Beef Burger', 'Good Burgers')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

Pablos_foods = Restaurant('Pablos food', 'fishy food')
Pablos_foods.describe_restaurant()

Beckys_food = Restaurant('Becks place', 'Thai food')
Beckys_food.describe_restaurant()

Lloyds_food = Restaurant('Lloyds place', 'Taiwainese food')
Lloyds_food.describe_restaurant()