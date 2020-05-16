favorite_place = {
    'Mpho': ['spain', 'barcelona', 'japan'],
    'Dayne':['greece', 'china','cuba'],
    'Danny':['brazil', 'indonesia', 'green land'],
}
for name, places in favorite_place.items():
    print(f"\n{name.title()}'s favorite are:")
    for place in places:
        print(f"\t {place.title()}")





