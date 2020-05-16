dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])




##Tuples are unchangeable
dimensions = (200, 50)
dimensions[0]

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)



dimensions = (200, 50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
dimensions = (400,100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)