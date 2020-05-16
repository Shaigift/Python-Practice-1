##Return Values
#-Functions can return a value or set of values. It doesn't always have to display its output directly.
#-The return statement takes a value from inside a function and sends it back to the line that called the function
#-Return values simolify body of program

##Returning a Simple Value

def get_formatted(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted('jimi', 'hendrix')
print(musician)


##Making an Argument Optional
#-If extra information is to be provided than arguments can be optional.vDefault values can be used to
#-make an argument optional

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
        return full_name.title()
musician = get_formatted('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


