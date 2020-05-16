favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'cody' : 'c++',
    'zack' : 'react',
}

for name ,language in favorite_languages.items():
    print(f" {name.title()}'s favorite language is {language.title()}")

print("\n")

new_favorite_languages_names = ['cody' , 'sarah' , 'mosely', 'miley', 'kim']
for names in new_favorite_languages_names:
    if names in favorite_languages.keys():
        print(f" {names.title()} have already taken the poll")
    else:
        print(f"{names.title()}, please take the poll")


