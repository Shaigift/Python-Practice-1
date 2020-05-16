sandwich_orders = ['Tuna Sandwich', 'Beef Sandwich', 'Chicken Sandwich','Salami Sandwich', 'Pastrami', 'Pastrami', 'Pastrami']

print("The shop has run out of Pastrami")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

print(sandwich_orders)
