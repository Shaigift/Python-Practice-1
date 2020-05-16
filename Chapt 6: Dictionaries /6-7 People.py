people = {
    'Mpho': {
        'age' : 23,
        'profession': 'Programmer',
        'sex': 'Male',
        'interests': 'Female',
        'city': 'Johannesburg'
        },

    'Dayne': {
        'age' : 23,
        'profession': 'Dancer',
        'sex': 'Female',
        'interests': 'Travelling',
        'city': 'Johannesburg'
        },

    'Danny': {
        'age' : 43,
        'profession': 'Lawyer',
        'sex': 'Male',
        'interests': 'Biking',
        'city': 'Los Angeles'
        },
    }

for username, user_info in people.items():
    print(f"\nUsername: {username}")
    profession = f"{user_info['profession']}"
    interests = f"{user_info['interests']}"
    city = f"{user_info['city']}"
    age = f"{user_info['age']}"
    sex = f"{user_info['sex']}"

    print(f"\tsex: {sex.title()}")
    print(f"\tprofession: {profession.title()}")
    print(f"\tinterests: {interests.title()}")
    print(f"\tcity: {city.title()}")
    print(f"\tage: {age.title()}")
