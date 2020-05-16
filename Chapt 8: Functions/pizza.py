##Passing an Arbitary Number of Arguments
#-If you won't know what kind of information will be passed to the function, arbitary number of arguments may be passed
#-The function below has one parameter *toppings, but the parameter collects as many arguments as the calling line provides
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """Summarize the pizza we about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

##Mixing Positional and Arbitrary Arguments
#-For functions to accept arbitrary numbet of arguments, the referred to parameter must be placed last in function definition
#-Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter

def make_pizza(size, *toppings):
    """Summarize the pizza we about to make"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12,'mushroom', 'green peppers', 'extra cheese')
