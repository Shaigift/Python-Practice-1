Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)

Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars[0])

Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars[0].title())

Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars[1])
print(Cars[2])


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars[-1])


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
message = f'My first car was a {Cars[0].title()}.'
print(message)




Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
Cars[0] = 'Tesla'
print(Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
Cars.append('Tesla')
print(Cars)


Vehicles = []
Vehicles.append('BMW')
Vehicles.append('Yamaha')
Vehicles.append('Suzuki')
print(Vehicles)




Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
Cars.insert(0, 'Ducati')
print(Cars)





Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)

del Cars[0]
print(Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)

del Cars[1]
print(Cars)


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
popped_Cars = Cars.pop()
print(popped_Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
last_owned = Cars.pop()
print(f"The last Car I owned was a {last_owned.title()}.")



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
first_owned = Cars.pop(0)
print(f"The first car i owned was a {first_owned.title()}.")


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
Cars.remove('FORD')
print(Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
too_expensive = 'BMW'
Cars.remove(too_expensive)
print(Cars)
print(f'\nA {too_expensive.title()} is too expensive for me.')


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
Cars.sort()
print(Cars)


Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
Cars.sort(reverse=True)
print(Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']

print("Here is the orignal list:")
print(Cars)

print("\nHere is the sorted list:")
print(sorted(Cars))

Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print("\nHere is the original list again:")
print(Cars)



Cars = ['BMW', 'MAZDA', 'TOYOTA', 'FORD', 'SUZUKI']
print(Cars)
Cars.reverse()
print(Cars)