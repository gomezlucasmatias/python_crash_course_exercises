artemisa = {'name': 'artemisa', 'kind': 'cat', 'owner': 'ame',}

felipe = {'name': 'felipe', 'kind': 'cat', 'owner': 'luz'}

octabio = {'name': 'octabio', 'kind': 'cat', 'owner': 'damaris'}

aurelia = {'name': 'aurelia', 'kind': 'dog', 'owner': 'lili'}

pets = [artemisa, felipe, octabio, aurelia]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']} and {pet['name'].title()} own to {pet['owner'].title()}")

