## Writing to a File
#-

##-Writing to an Empty File
#-One of the simplest ways to save data is to write it to a file
##-Writing to an Empty File
#-Writing a text to a file requires to call open() with second argument telling Python that you
#-want to write to the file

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")