##Exception
#-Special objects called 'exceptions' to manage errors that arise during a program
#-Exceptions are handled with try-except blocks. a try-except block asks Python to do something
#-but it also tells Python what to do if an exception is raised. Using try-except blocks will make programs
#-continue running even if things start to go wrong.

##Handling the ZeroDivisionError Exception
print(5/0)

##Using try-except Blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


##Using Exceptions to Prevent Crashes
#-Handling errors is important when program has additional work to do after error occurs.
#-This usually occurs in programs that asks users for input
#-If the program responds to invalid input appropriately, it can prompt for more valid inpit instead of crashing

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

##The else Block
#-The above code was made more resistance by wrapping the line that produce errors in a try-except block.
#-Since the  error occurs on the line that peforms the division, that's where the try-except block will be put

