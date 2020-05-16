##Returning a Dictionary
#-Complicated data structures like lists and dictionaries can be returned by functions.
#-Example below

def build_person(first_name, last_name):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)



def build_person(first_name, last_name, age=None):
    """Return a dictionary of informatio about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
#-None can be thought of as a placeholder value
#-None becomes False in a conditional test. If function call includes a value for age , that value is stored in the dictionary
#-This function always stores a person's name but it can also be modified to store any other information you want about a person

