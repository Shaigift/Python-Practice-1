Guests = ['Anele', 'Ezile', 'Mamello']
print(f"Hello {Guests[0]}, you're invited to dinner.")
print(f"Hello {Guests[1]}, you're invited to dinner.")
print(f"Hello {Guests[2]}, you're invited to dinner.")
print(f'Unfortunately {Guests[0]} cannot make it')


##Modified List
del Guests[0]
Guests.insert(0, 'Paul')



##Second Invitation
print(Guests)
print(f"Hello {Guests[0]}, you're invited to dinner.")
print(f"Hello {Guests[1]}, you're invited to dinner.")
print(f"Hello {Guests[2]}, you're invited to dinner.")