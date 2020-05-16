##Using break to Exit a Loop
#- To exit a while loop instantly whilst running remaining code in loop, despite results any conditional test, use break statement.
#- Break statements outlines flow of program and may be used to control which lines of code are executed and whichever aren't so program executes conde that i want it and when i want


prompt = "\nPlease enter the name of a city you have visited:"
prompt +=  "\nEnter 'quit when you are finished "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")