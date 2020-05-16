magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)


##Choose meaningful variable names



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cannot wait to see your next trick, {magician.title()}.\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cannot wait to aee your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")



##Forgetting to indent will always leave errors.


##Identing Unncessarily After the Loop indent

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I cannot wait to aee your next trick, {magician.title()}.\n")
    print("Thank you, everyone. That was a great magic show!")


##Forgetting The Colon will give an error
magicians = ['alice', 'david', 'carolina']
for magician in magicians #Colon is meant to go here
    print(magician)







