prompt = ("\nPlease enter your age: ")

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 12:
        print("Your ticket costs $10.")
    elif  age > 12 :
        print("Your tickets costs $15.")