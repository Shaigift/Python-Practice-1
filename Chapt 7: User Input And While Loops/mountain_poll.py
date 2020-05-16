##Filling a Dictionary with User Input
#Prompting a user for as much input as necessary is possible via a while loop. Example making a polling program that asks users for
#-participants name. Data will be stored in a dictionary

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

