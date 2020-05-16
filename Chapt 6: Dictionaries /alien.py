##A Simple Dictionary

alien_0 = {'color' : 'green', 'points':5}
print(alien_0['color'])


##Working with Dictionaires
#A Dictionary in Python is a collection of key-value pairs. Individual keys are connected to a value

##Accesing Values in a Dictionary
alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points':5}

new_points = alien_0['points']
print(f'You just earned {new_points} points!')


##Adding New Key-Value Pairs
#-Dictionaries are dynamic structures, new key-value pairs can be added at any time.

alien_0 = {'color': 'green', 'points':5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

##Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)


##Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")







alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #This must be a fat alien.
    x_increment = 3

    # The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")



##Removing Key-Value Pairs
#-key value pairs that are removed are deleted permanently
alien_0 = {'color': 'green', 'points':5}
print(alien_0)

del alien_0['points']
print(alien_0)



##A Dictionary of Similar Objects

favorite_langauges = {
    'jen' : 'python',
    'sararh': 'c',
    'edward': 'ruby',
    'phil': 'python',
}