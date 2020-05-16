cities = []

city =  {
        'City': 'Johannesburg',
        'Population': '13 million',
        'Popular spots': 'Soweto',
        'Weather': 'Sunny',
        'Location' : 'South Africa',
        'Fact': 'Gold was discovered at Witswatersrand'
}
cities.append(city)

city = {
        'City': 'Durban',
        'Population': '595000',
        'Popular spots': 'uShaka Marine World',
        'Weather': 'Humid',
        'Fact': 'The Anglo-Zulu war occured on 1879',
        'Location' : 'South Africa',
}
cities.append(city)

city =  {
        'City': 'Cape Town',
        'Population': '433600',
        'Location' : 'South Africa',
        'Popular spots': 'Table Mountain',
        'Weather': 'Sunny',
        'Fact': 'The Castle of Good Hope is located in Cape Town',
}
cities.append(city)

for city in cities:
    print(f"\nHere are interesting things about {city['City'].title()}: ")
    for key, value in city.items():
        print(f"\t {key.title()}: {str(value)}")

