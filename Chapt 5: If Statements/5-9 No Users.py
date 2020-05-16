usernames = []
if usernames:
    for name in usernames:
        if name == 'admin':
            print("Hello admin, here is the list of the top five gamers.")
    else:
        print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need to find some users!")




