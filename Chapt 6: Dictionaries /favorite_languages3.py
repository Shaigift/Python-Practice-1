favorite_langauges = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, langauges in favorite_langauges.items():
    print(f"\n {name.title()}'s favorite languages are:")
    for langauge in langauges:
        print(f"\t {langauge.title()}")


