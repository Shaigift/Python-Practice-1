with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
        print(line.rstrip())

##Reading Line by Line
#-A for loop may be utilized to examine each line from a file one at a time.

