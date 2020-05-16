##If Statement Example
cars = ['audi', 'bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


##Checking for Equality , this checks if value of variable is equal to value of interest
car = 'bmw'
car == 'bmw'
True

##This returns false because value of audi is differemt to 'bmw'
car = 'audi'
car == 'bmw'
False

##Ignoring Case When Checking for Equality
#Two values with different capitilization are not considered equal
car = 'Audi'
car == 'audi'
False


car = 'Audi'
car.lower() == 'audi'
True


car = 'Audi'
car.lower() == 'audi'
True
car
'Audi'


