responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("What would be your dream vacation? ")

    responses[name]= response

    repeat = input("Would you like to add another response( yes/ no?) ")
    if repeat == 'no':
        polling_active = False

print("\n--- results are now complete---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

