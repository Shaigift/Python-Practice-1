##Handling the FileNotFoundError Exception
#-If a file is missing or name has been forgotten or file not exisiting at all. All of these can be handled by
#-try-except block

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")