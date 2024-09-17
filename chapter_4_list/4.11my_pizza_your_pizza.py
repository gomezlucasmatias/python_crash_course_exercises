pizzas = ['fugazetta', 'tropical', 'Napolitana', 'Muzarella']

friend_pizzas = pizzas[:]

pizzas.append('Calabreza')

friend_pizzas.append('Bacon & onion')

print('My favorite pizzas are: ')
for pizza in pizzas:
    print(pizza)

print('\nMy friends favorinte pizzas are: ')
for pizza in friend_pizzas:
    print(pizza)
