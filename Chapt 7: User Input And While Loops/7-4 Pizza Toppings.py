prompt = "\nPlease enter pizza topping that you would like: "


while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    else:
        print(f"Now adding {pizza_topping.title()} to your pizza")