##Using a while Loop with Lists and Dictionaries
#-To keep track of many users and pieces of information we'll beed to use lists and dictionaries with while loops
#-Never modify a ,ist inside a for loop because Python will have trouble keeping track of items in the list, instead to modify a list, a while loop must be used

##Moving Items from One List to Another

#Start with users that need to be verified,
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

