##Numerical Comparisons

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
age < 21
True
Age <= 21
True
age > 21
False
age >= 21
False


##Checking Multiple Conditions
#More than one condition can be checked, keywords and and or can help

##using and to Check Multiple Conditions

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
False
age_1 = 22
age_0 >= 21 and age_1 >= 21
True
#Parenthesis can also be used to improve readability
(age_0 >= 21) and (age_1 >= 21)

##Using or tp Check Multiple Conditions
age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21
True
age_0
age_0 >= 21 or age_1 >= 21
False



##Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
True
'pepperoni' in requested_toppings
False


