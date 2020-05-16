number = input('Is the number a multiple of ten or not? :')
number = int(number)
if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")