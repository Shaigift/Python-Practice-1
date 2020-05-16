##Storing Your Functions in Modules
#-Using detailed names for functions will make main programs much easier to follow.
#-Functions can be stored in seperate files called modukles and then importing that module into your main program.
#-To tell python to make code in module available in the currently running program , import statement.
#-Functions in seperate files allows file details to be hidden and focus on its higher-level logic.
#-Functions stored in seperate files can be shared without having to share entire program.

##Importing an Entire Module
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")