##Passing a List
#-Passing a list to a function might be neccessary whether it's names , objects , names , or complex objects such as dictionaries.
#-When passing a list to a function , function gets direct access to contents to the contents of the list

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', ' margot']
greet_users(usernames)

