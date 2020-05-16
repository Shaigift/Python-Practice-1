sandwich_orders = ['Tuna Sandwich', 'Beef Sandwich', 'Chicken Sandwich','Salami Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Your sandwiches : {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche.title())

