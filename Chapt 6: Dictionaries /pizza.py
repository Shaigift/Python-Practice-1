
##A List in a Dictionary
#-It may be useful to store a list in a dictionary as you may be able to store many aspects of that thing.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\n" + topping)




