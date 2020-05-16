##Defining a Function
#What are functions? Functions are designed to do one specific job. Functions are called to do one specific job , they
#-are called so that there's no need to print the same code for one specific job over and over again.
#-functions are easy to call, read, write & fix.
#-Chapter 8 deals with writing functions whose primary job is to display information and other functions
#-designed to process data & return a value or set of values & learning to store functions in separate files called
#-modules to help organize your main program files.

def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

##Passing Information to a Function
#greet_user() can also tell user Hello! but also greet them by name. Username can be enter in parenthesis of function's
#-definition at def greet_user(). function will accept username value for username each time it's called.
#-Example when greet_user() is called, programmer can pass it a name, such as 'jesse', inside the parenthesis:

def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")

greet_user('Daveyton')