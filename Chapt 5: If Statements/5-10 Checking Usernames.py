current_users = ['Pete', 'Kendra', 'Kia' , 'Kourtney' , 'Kiki']
new_users = ['Chris', 'Cody' , 'Carl', 'Charles' , 'Kourtney', 'KIKI']

current_users_lower = [user.lower() for user in current_users]

for name in new_users:
    if name.lower() in current_users_lower:
        print(f' {name} new username required.')
    else:
        print(f' {name} is available for use.')
