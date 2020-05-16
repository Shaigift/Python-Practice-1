##Storing Data
#-Json module allows dumping simple Python data structures into a file and load the data from the next time the program runs
#-Json can also be used to share data between various Python programs

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)


##The JSON (JavaScript Object Notation) format was originally developed for
##JavaScript. However, it has since become a common format used by many
##languages, including Python.