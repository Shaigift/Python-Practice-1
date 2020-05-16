print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input('Please input a number: ')
        if x == 'q':
            break

        x = int(x)

        y = input('Give me another: ')
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, please enter a valid number.")

    else:
        sum = x + y
        print("The sum of" + str(x) + " and "  + str(y) +  " is " + str(sum) + ".")



