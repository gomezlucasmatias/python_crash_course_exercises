ame = {'name': 'ame', 'last_name': 'gomez gerardi', 'age': '11',}

mati = {'name': 'mati', 'last_name': 'gomez', 'age': '37',}

darian = {'name': 'darian', 'last_name': 'gomez gerardi', 'age': '17',}

people = [ame, mati, darian,]

for name in people:
    print(f"{name}'s date are:")
    for value in name.values():
        print(f'\n\t\t{value}')
