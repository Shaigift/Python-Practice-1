

##//
#-For writing prompts that are longer than one line , prompt can be assigned to variable and variable can be assigned to input() function, this allows building prompt over several lines

prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name? : "
name = input(prompt)
print(f"\nHello , {name}!")



##Using int() to Accept Numerical Input
age = input("How old are you? ")
print(age)


age = input("How old are you? ")
age = int(age)
age >= 18