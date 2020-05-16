filename = 'programming_poll.txt'

responses = []
while True:
    responese = input("\nWhy do you like programming? ")
    responses.append(responese)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
with open(filename, 'a') as f:
    for responese in responeses:
        f.wrtie(response + "\n")

