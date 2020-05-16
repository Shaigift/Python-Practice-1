pets = []

pet = {
    'owners name' : 'Mr Whiskers',
    'type' : 'Bull Terrior',
    'age' : '3 years',
}
pets.append(pet)

pet = {
    'owners name': 'Pat',
    'type' : 'black cat',
    'age' : '1 year',
}
pets.append(pet)

pet = {
    'owners name': 'Mr Siler',
    'type' : 'black mamba',
    'age' : '3',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's all the information about  "
          f"the {pet['type'].title()}:")
    for key, value in pet.items():
        print(f"{key.title()}: {str(value)}")


