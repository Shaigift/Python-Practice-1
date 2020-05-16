##Removing All Instances of Specific Values from a List
#To remove all values in a list we can run a while loop until items is no longer in the list as shown here with 'cat'
pets = ['dog', 'cat', ' dog', 'goldfish', 'cat', ' rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

