try:
    x = input('Please input a number: ')
    x = int(x)

    y = input('Please input a number:')
    y = int(y)

except ValueError:
    print("Sorry, please enter a valid number.")

else:
    sum = x + y
    print("The sum of" + str(x) + " and "  + str(y) +  " is " + str(sum) + ".")



