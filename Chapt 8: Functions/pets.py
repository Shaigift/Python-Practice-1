##Passing Arguments
#Arguements can be passed to functions in multiple ways
#-Positional arguements can used which require same order the parameters were written in
#-keyword arguements contain variable names and values;and lists and dictionaries of values

##Positional Arguements
#-Python will match individual arguements in a function call with a parameter in the function definition
#-doing this on the foundation of order is the most efficient way

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet('hamster', 'harry')

##Multiple Function Calls
#Functions can be called as many times as needed. Detailing a second yet varied pet needs another call to describe_pet():

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#The code detailing a pet is coded once in function then after whenever
#-a new pet description is added, function with new pet's information can be called
#-even if code were to expand to 10 lines, description of new pet in one line can be called again & again
#-many positional arguments can be used in functionsas many as needed
#-python will work through the arguments provided when calling the function and match each one with corresponding parameter in tehe functions definition

##Order Matters in Positional Arguments
#-Unexpected results may be result of mixing arguments in a function call when using positional arguements,

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('harry', 'hamster')

##Keyword Arguments
#-keyword arguments are arguments that have name-value pairs which are passed to a function
#-name and values are directly associated within arguments so that when arguements are passed to function
#-there's no confusion. Keyword arguments make it easier to order arguments in the function call
#-and they calrify the role of each value in the function call.

def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"/nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')


##Default Values
#-parameters can be set to default values for each parameter.
#-if an argument for parameterie is provided in the function call, Python uses the argument value.
#-IF not, it uses the parameter's default value. When the default value is defined
#-then the corresponding arguement ususally written can be ignored.
#-Default values may simplify function calls & clarify ways which functions are typically used.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


##Equivalent Function Calls
#-Popularly there can be various ways to call a function


# def describe_pet(pet_name, animal_type='dog'):
# # A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
#
# #A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
##Each of the above outputs will have the same output as previous examples

##Avoiding Argument Errors
#-Errors will be encountered when using functions. When fewer or more arguments are provided then errors will occur.
#-Example below
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.)

describe_pet()