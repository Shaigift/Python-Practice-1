motorcycles = [ 'honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)


motorcycles = ['honda', 'yahama', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)



motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)


motorcycles = ['honda', 'yahama', 'suzuki']
last_owned = motorcycles.pop()
print(f'THe last motorcycle I owned was a {last_owned}.')



motorcycles = ['honda', 'yahama', 'suzuki']
first_owned = motorcycles.pop(0)
print(f'The first motorcycle I owned was a {last_owned.title()}.')


motorcycles = ['honda', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda', 'yahama', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\n {too_expensive.title()} is too expensive for me.')


