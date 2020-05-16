I love programming.

##-Writing Multiple Lines
#-Write() function doesnt add any newlines to the text you write

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")