import json

number = input('Please enter number: ')
filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f" I know your favorite number it is, {number}")
