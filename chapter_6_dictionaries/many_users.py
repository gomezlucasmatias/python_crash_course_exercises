users = {'aeinstein': {'name': 'albert', 'lastname': 'einstein', 'location': 'princeston',},
         'mcurie': {'name': 'marie', 'lastname': 'curie', 'location': 'paris',}
         }

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f'{user_info['name']} {user_info['lastname']}'
    location = f'{user_info["location"]}'

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")
