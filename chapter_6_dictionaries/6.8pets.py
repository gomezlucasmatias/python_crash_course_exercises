artemisa = {'kind': 'cat', 'owner': 'ame',}

felipe = {'kind': 'cat', 'owner': 'luz'}

octabio = {'kind': 'cat', 'owner': 'damaris'}

aurelia = {'kind': 'dog', 'owner': 'lili'}

pets = [artemisa, felipe, octabio, aurelia]

for item, item_date in pets:
    print(f'{item} and its owner {item_date}')
