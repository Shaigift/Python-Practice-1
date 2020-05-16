favorite_numbers = {
    'Peter': [5, 7],
    'Luyanda': [6, 8],
    'Eric': [7, 9],
    'Patrica': [8, 12],
}
for name, numbers in favorite_numbers.items():
    print(f"\n {name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t {int(number)}")

